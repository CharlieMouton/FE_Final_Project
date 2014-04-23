import pygame
from pygame.locals import *
import time
from fe_model import *
from fe_view import *
from fe_controller import *

if __name__ == '__main__':
    pygame.init()
    
    #Setup.
    model = Model()
    screen = pygame.display.set_mode(size)
    view=View(model,screen)
    controller = Controller(model,view)
     
    running = True
    while running:

        # View
        model.update()
        view.draw()
        
        # Controller
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Model
            if event.type == MOUSEBUTTONDOWN:
                if controller.charselected != None:
                    controller.move(event,controller.charselected)
                else:
                    controller.charselect(event)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    controller.char_reset(controller.charselected)

        time.sleep(.01)

    pygame.quit()