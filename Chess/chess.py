import pygame as p
import sys
p.init()

scr_w = 640
scr_h = 640
clock = p.time.Clock()


p.display.set_caption("2 Player Chess")
screen = p.display.set_mode((scr_w,scr_h))
run=True

while run:
    screen.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
    clock.tick(60)
    p.display.update()

p.quit()
sys.exit()


