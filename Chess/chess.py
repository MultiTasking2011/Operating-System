#importing
import pygame as p
import sys

######
p.init()
######

#important variables
scr_w = 640
scr_h = 640
clock = p.time.Clock()

#game variables
placement = [
    5,4,3,2,6,3,4,5,
    1,1,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    7,7,7,7,7,7,7,7,
    11,10,9,8,12,9,10,11
]
incheck = False
stalemate = False
checkmate = False
capture = False
move = False

#setup
p.display.set_caption("2 Player Chess")
screen = p.display.set_mode((scr_w,scr_h))
run=True

#loop
while run:
    screen.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
    clock.tick(60)
    p.display.update()

#ending
p.quit()
sys.exit()
############