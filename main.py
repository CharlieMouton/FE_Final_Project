import pygame
from pygame.locals import *
import time

from fe_model import *
from fe_view import *
from fe_controller import *

if __name__ == '__main__':
    pygame.init()
    
    #Setup.
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pyre Emblem')
    
    model = Model()
    view=View(model,screen)
    controller = Controller(model,view)
     
    while model.running:

        model.update()
        view.draw()
        controller.control()
        
        time.sleep(.01)

    pygame.quit()