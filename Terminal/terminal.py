import pygame 
import sys 
pygame.init()  
clock = pygame.time.Clock() 
screen = pygame.display.set_mode([600, 600]) 
base_font = pygame.font.Font("Terminal/Consolas.ttf", 12) 
user_text = ''
user_text += """New OS Terminal Session
""" 
user_text += ">> "
user_text_dict = dict()
input_rect = pygame.Rect(0, 0, 600, 600)
color_passive = pygame.Color('black') 
color = color_passive 
  
active = False
  
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                user_text = user_text[:-1] 
            else: 
                user_text += event.unicode
            if event.key == pygame.K_KP_ENTER:
                user_text += "\n"
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, color, input_rect) 
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
    input_rect.w = max(100, text_surface.get_width()+10) 
    pygame.display.flip() 
    clock.tick(60) 