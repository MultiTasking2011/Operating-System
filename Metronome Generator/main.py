import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import simpleaudio as sa
import time
import wave

root = tk.Tk()
root.title("Music Settings")
root.geometry("300x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TCheckbutton", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

play_beep = False
play_obj = None

def validate_inputs():
    bpm = bpm_entry.get()
    length = length_entry.get()
    time_signature = time_signature_var.get()
    
    try:
        if not bpm or not length or not time_signature:
            raise ValueError("All fields must be filled!")
        
        bpm = int(bpm)
        length = int(length)  
        
        if bpm < 10 or bpm > 1000:
            raise ValueError("BPM must be between 10 and 1000!")
        
        if length <= 0:
            raise ValueError("Length (Bars) must be a positive number!")
        
        if time_signature not in ["2/4", "3/4", "4/4"]:
            raise ValueError("Time Signature must be one of the options: 2/4, 3/4, or 4/4!")
        
        return bpm, length, time_signature
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def play_beep_sound(frequency=852, duration=0.05, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave_data = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
    return sa.play_buffer(wave_data, num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)

def start_metronome(bpm, bars, time_signature):
    global play_beep
    global play_obj
    play_beep = True
    beats_per_bar = int(time_signature.split("/")[0])
    duration_per_beat = 60 / bpm
    total_beats = beats_per_bar * bars
    for i in range(total_beats):
        if not play_beep:
            break
        if accent_var.get() and (i % beats_per_bar == 0):
            play_obj = play_beep_sound(frequency=852)
        else:
            play_obj = play_beep_sound(frequency=600)
        time.sleep(duration_per_beat)

def stop_metronome():
    global play_beep
    global play_obj
    play_beep = False
    if play_obj is not None:
        play_obj.stop()

def export_metronome(bpm, bars, time_signature):
    beats_per_bar = int(time_signature.split("/")[0])
    duration_per_beat = 60 / bpm
    total_beats = beats_per_bar * bars
    sample_rate = 44100
    sound_data = np.array([], dtype=np.int16)
    
    for i in range(total_beats):
        if accent_var.get() and (i % beats_per_bar == 0):
            beep = np.sin(2 * np.pi * 852 * np.linspace(0, duration_per_beat, int(sample_rate * duration_per_beat), endpoint=False)) * 32767
        else:
            beep = np.sin(2 * np.pi * 600 * np.linspace(0, duration_per_beat, int(sample_rate * duration_per_beat), endpoint=False)) * 32767
        sound_data = np.append(sound_data, beep.astype(np.int16))
    
    with wave.open("metronome.wav", "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(sample_rate)
        file.writeframes(sound_data.tobytes())
    messagebox.showinfo("Success", "Metronome exported as metronome.wav")

def on_listen_button_pressed():
    bpm, length, time_signature = validate_inputs()
    if bpm and length and time_signature:
        start_metronome(bpm, length, time_signature)

def on_stop_button_pressed():
    stop_metronome()

def on_download_button_pressed():
    bpm, length, time_signature = validate_inputs()
    if bpm and length and time_signature:
        export_metronome(bpm, length, time_signature)

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="nsew")

for i in range(5):
    main_frame.grid_rowconfigure(i, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

ttk.Label(main_frame, text="BPM:").grid(row=0, column=0, padx=10, pady=3, sticky="e")
bpm_entry = ttk.Entry(main_frame, width=15)
bpm_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ttk.Label(main_frame, text="Length (Bars):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
length_entry = ttk.Entry(main_frame, width=15)
length_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

accent_var = tk.BooleanVar()
accent_checkbox = ttk.Checkbutton(main_frame, text="First Note Accented", variable=accent_var)
accent_checkbox.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

ttk.Label(main_frame, text="Time Signature:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
time_signature_var = tk.StringVar(value="4/4")
time_signature_dropdown = ttk.Combobox(main_frame, textvariable=time_signature_var, values=["2/4", "3/4", "4/4"], width=12)
time_signature_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="w")

check_button = ttk.Button(main_frame, text="Listen", command=on_listen_button_pressed)
check_button.grid(row=4, column=0, columnspan=2, pady=10)

stop_button = ttk.Button(main_frame, text="Stop", command=on_stop_button_pressed)
stop_button.grid(row=5, column=0, columnspan=2, pady=10)

submit_button = ttk.Button(main_frame, text="Download", command=on_download_button_pressed)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()

#fix exporting
#make polyrythm generator