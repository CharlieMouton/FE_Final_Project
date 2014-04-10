import pygame
from pygame.locals import *
import time
from fe_model import *
from fe_view import *
from fe_controller import *

num_of_char=2

if __name__ == '__main__':
    pygame.init()
    
    #Setup
    model = Model()
    screen = pygame.display.set_mode(size)
    view=View(model,screen)
    controller = Controller(model)
    
    
    
    
    
    running = True
    while running:
        # VIEW
        view.draw()


        for i in range(num_of_char):
    
            inputBox=InputBox()
            view.draw()
            #Adds characters
            charType=inputBox.ask(screen, "Type")
            view.draw()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    corr=controller.handle_mouse_event(event)
            self.model.character=model.setupChar(charType,coor[1],coor[2])        
        
        # CONTROLLER
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # MODEL
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)

        time.sleep(.01)

    pygame.quit()