import pygame
from pygame.locals import *
import time

from scripts import *
from fe_model import *
from fe_view import *
from fe_controller import *

if __name__ == '__main__':
    pygame.init()
    
    model = Model()
    screen = pygame.display.set_mode(size)
    view=View(model,screen)
    controller = Controller(model)
    
    running = True
    while running:
        screen.fill(pygame.Color(255,255,255))       
        view.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)

        time.sleep(.01)

    pygame.quit()