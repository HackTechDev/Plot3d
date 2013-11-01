# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
import webbrowser
import time
import sqlite3 as lite

sys.path.append('./package')

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

class Point(pygame.sprite.Sprite):
    posx = 0
    posy = 0

    def __init__(self, color, posx, posy, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy
       
        self.posx = self.rect.x 
        self.posy = self.rect.y

       

def main():

    pygame.init()

    screen_width = 1280
    screen_height = 800
    screen=pygame.display.set_mode([screen_width,screen_height])

    pygame.display.set_caption("Plot3d")

    done = False

    clock=pygame.time.Clock()


    point_list = pygame.sprite.RenderPlain()
    all_sprites_list = pygame.sprite.RenderPlain()


    for i in range(20):
        point = Point(black, random.randrange(1280), random.randrange(800), 10, 10)
        point_list.add(point)
        all_sprites_list.add(point)

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 

        screen.fill(white)


        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

#Run the script if executed
if __name__ == "__main__":
    main()
