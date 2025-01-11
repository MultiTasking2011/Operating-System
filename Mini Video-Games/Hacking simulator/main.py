import sys
import time
from tqdm import tqdm
from rich.progress import Progress
from rich.console import Console
import random
from tabulate import tabulate

BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def progress_bar(current, total, bar_length=40):
    progress = current / total
    bar = '=' * int(bar_length * progress) + '-' * (bar_length - int(bar_length * progress))
    sys.stdout.write(f'\r|{bar}| {current}/{total} ({progress * 100:.2f}%)')
    sys.stdout.flush()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

def delay_print_2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

device_names = [
    "John's iPhone", "Emma's MacBook", "Sophie's iPad", "Mike's Galaxy", "Liam's Dell Laptop",
    "Olivia's Surface Pro", "Noah's Lenovo ThinkPad", "Ava's Chromebook", "Isabella's iPhone 13",
    "James's iMac", "Ella's Pixel Phone", "Benjamin's Asus ZenBook", "Mia's HP Pavilion",
    "Charlotte's Huawei MateBook", "Lucas's Samsung Tab", "Amelia's Acer Aspire",
    "Ethan's Razer Blade", "Mason's OnePlus Phone", "Harper's Kindle Fire", "Logan's MacBook Air",
    "Aria's iPhone XR", "Jack's Alienware Laptop", "Sophia's Sony Xperia", "Elijah's Toshiba Satellite",
    "Emily's Moto G", "Oliver's Xiaomi Redmi", "Jacob's iPad Mini", "Layla's iPhone 12",
    "Henry's Microsoft Studio", "Zoe's Chromebook Plus", "Daniel's Asus ROG", "Evelyn's Lenovo Yoga",
    "Matthew's Galaxy Note", "Grace's iPhone 14", "Jackson's Surface Book", "Scarlett's LG Gram",
    "Sebastian's Mac Mini", "Victoria's HP Spectre", "Aiden's Sony Vaio", "Hannah's Oppo Reno",
    "Carter's Nokia Lumia", "Leah's Dell Inspiron", "Julian's iPad Pro", "Natalie's Pixel Slate",
    "Luke's Galaxy S21", "Chloe's iPhone SE", "Wyatt's Lenovo Legion", "Penelope's Huawei P30",
    "Dylan's Acer Swift", "Riley's Kindle Paperwhite", "Nathan's iPhone X", "Aubrey's Galaxy A12",
    "Caleb's Asus VivoBook", "Lillian's MacBook Pro", "Ryan's Surface Go", "Eleanor's OnePlus 9",
    "Samuel's Dell XPS", "Audrey's iPad Air", "Isaac's Samsung Tab S7", "Samantha's Pixel 6",
    "Levi's iPhone 11", "Skylar's Razer Phone", "Gabriel's Lenovo IdeaPad", "Genesis's Moto Edge",
    "Christian's HP Envy", "Stella's Acer Nitro", "Anthony's Galaxy Z Fold", "Nora's Huawei MatePad",
    "Andrew's Sony Walkman", "Hazel's Chromebook Flip", "Joshua's Alienware Aurora", "Paisley's iPhone 15",
    "Christopher's Mac Studio", "Ellie's Samsung Galaxy Book", "Thomas's iPhone 8", "Claire's iPad Gen 9",
    "Jaxon’s Xiaomi Mi Pad", "Lucy’s Surface Laptop", "Ezra's LG Velvet", "Violet's Kindle Oasis",
    "Isaiah's iPhone 6", "Aurora's Oppo Find", "Aaron's Samsung Note 20", "Caroline's Pixelbook Go",
    "Hudson's Nokia 3310", "Brooklyn's Dell G3", "Asher's iPhone 13 Pro", "Anna's Surface Pro 7",
    "Hunter's iMac Pro", "Madison's iPhone 7", "Nolan's MacBook M2", "Luna's Galaxy Flip",
    "Adrian's Lenovo ThinkCentre", "Eva's iPhone 5C", "Easton's Razer Blade 16", "Elena's iPad Gen 6"
]

# Generate 100 random IP addresses
ip_addresses = [
    f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
    for _ in range(100)
]

def pick_random_devices_and_ips(device_list, ip_list, min_count=10, max_count=30):
    count = random.randint(min_count, max_count)
    selected_devices = random.sample(device_list, count)
    selected_ips = random.sample(ip_list, count)
    return selected_devices, selected_ips


total = 300
for i in range(total + 1):
    progress_bar(i, total)
    time.sleep(0.01)  # Simulate work
print("")

delay_print(" _   _ ______ _________          ______  _____  _  __    _____ _   _ _____ ______ ______ ______ _____ \n")
delay_print("| \ | |  ____|__   __\ \        / / __ \|  __ \| |/ /   / ____| \ | |_   _|  ____|  ____|  ____|  __ \ \n")
delay_print("|  \| | |__     | |   \ \  /\  / / |  | | |__) | ' /   | (___ |  \| | | | | |__  | |__  | |__  | |__) |\n")
delay_print("| . ` |  __|    | |    \ \/  \/ /| |  | |  _  /|  <     \___ \| . ` | | | |  __| |  __| |  __| |  _  / \n")
delay_print("| |\  | |____   | |     \  /\  / | |__| | | \ \| . \    ____) | |\  |_| |_| |    | |    | |____| | \ \ \n")
delay_print("""|_| \_|______|  |_|      \/  \/   \____/|_|  \_\_|\_\   _____/|_| \_|_____|_|    |_|    |______|_|  \_\ \n""")
print("")
time.sleep(1)
delay_print_2("Current wifi: ")
time.sleep(0.5)
print("\033[31mCAFÉ FREE WIFI\033[0m")
time.sleep(1)
selected_devices, selected_ips = pick_random_devices_and_ips(device_names, ip_addresses)
# Display results
table_data = []
for name, ip in zip(selected_devices, selected_ips):
    table_data.append([
        f"{BLUE}{name}{RESET}",        # Name in blue
        f"{RED}{ip}{RESET}",          # IP in red
        f"{GREEN}Connected{RESET}"    # Status in green
    ])

# Display the table
delay_print(tabulate(table_data, headers=["Name", "IP", "Status"], tablefmt="grid") + "\n")
