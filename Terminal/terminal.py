import pygame 
import sys 
pygame.init()  
clock = pygame.time.Clock() 
screen = pygame.display.set_mode([600, 600]) 
base_font = pygame.font.Font("Terminal/Consolas.ttf", 12) 
user_text = '>> '
user_text_dict = dict()
color_passive = pygame.Color('black')
color = color_passive
  
active = False
  
while True: 
    starting_rect = pygame.Rect(0, 0, 600, 10)
    input_rect = (pygame.Rect(0,15,600,20))
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, color, starting_rect) 
    text_surface = base_font.render("New OS terminal session", True, (255, 255, 255)) 
    screen.blit(text_surface, (starting_rect.x+5, starting_rect.y+5)) 
    input_rect.w = max(100, text_surface.get_width()+10) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_BACKSPACE: 
                user_text = user_text[:-1] 
            else: 
                user_text += event.unicode
            if event.key == pygame.K_RETURN:
                pygame.draw.rect(screen, color, pygame.Rect(0,30,600,10)) 
                textalso = base_font.render("Incorrect command", True, (255, 255, 255)) 
                screen.blit(textalso, (pygame.Rect(0,30,600,10).x+5, pygame.Rect(0,30,600,10).y+5)) 

    pygame.draw.rect(screen, color, input_rect) 
    textinput = base_font.render(user_text, True, (255, 255, 255)) 
    screen.blit(textinput, (input_rect.x+5, input_rect.y+5)) 
    # input_rect.w = max(100, textalso.get_width()+10) 
    # screen.blit(textalso, (pygame.Rect(0,30,600,10).x+5, pygame.Rect(0,30,600,10).y+5)) 

    pygame.display.flip() 
    clock.tick(60) 