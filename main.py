import pygame
from pygame.locals import *
import time
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
        # VIEW
        view.draw()

        # CONTROLLER
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # MODEL
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)

        time.sleep(.01)

    pygame.quit()