import pygame
from pygame.locals import *
import time

from Scripts import *
from Global_variables import *
from Model import *
from View import *
from Controller import *

if __name__ == '__main__':
    pygame.init()
    
    model = Model()
    screen = pygame.display.set_mode(size)
    running = True
    view=View(model,screen)
    controller = Controller(model)
    
    while running:
        screen.fill(pygame.Color(255,255,255))       
        view.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)
            # KEYBOARDBUTTON is probably a lie. Fix below.
            # elif event.type == KEYBOARDDOWN:
            #     controller.handle_keyboard_event(event)
        time.sleep(.01)

    pygame.quit()