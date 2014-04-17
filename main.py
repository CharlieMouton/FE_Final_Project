import pygame
from pygame.locals import *
import time
from fe_model import *
from fe_view import *
from fe_controller import *

num_of_char=2   

if __name__ == '__main__':
    pygame.init()
    
    #Setup.
    model = Model()
    screen = pygame.display.set_mode(size)
    view=View(model,screen)
    controller = Controller(model,view)
     
    running = True
    while running:
        # VIEW
        view.draw()

        '''
        for i in range(num_of_char):
    
            inputBox=InputBox()
            view.draw()
          
            #Adds characters
            charType=inputBox.ask(screen, "Type")
            view.draw()
            noCoor=True       
        '''
        # CONTROLLER
        #    while noCoor:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # MODEL
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)
                #noCoor=False
                
       # self.model.character=model.setupChar(charType,coor[1],coor[2])
        time.sleep(.01)

    pygame.quit()