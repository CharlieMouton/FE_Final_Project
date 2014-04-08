import pygame

size = (1024,768)

def CartToIso(x,y,z=10):
    """Takes an x and y pair and converts them to isometric position."""
    centerx = 640/2
    centery = 480/2
    isox = x - y+centerx 
    isoy = (x+y)/2 - z
    return (isox,isoy)

def IsoToCart(x,y):
    """Takes an isometric position and converts them to an x and y pair."""
    isox = isox - centerx
    cartX = (2 * (isoY+z) + isoX) / 2
    cartY = (2 * (isoY+z) - isoX) / 2
    return (cartX, cartY)

class View:
    """
    Game viewer in pygame window.
    """
    def __init__(self, model, screen):
        self.size = size
        self.centerx = size[0]/2
        self.centery = size[1]/2
        self.model= model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
        MAP_WIDTH =  4
        MAP_HEIGHT =  4
        TILE_WIDTH =  64
        TILE_HEIGHT =  32
        for point in self.model.grid:
            # Please refactor into something more intuitive.
            point1 = (point[0],point[1])
            point2 = (point[0] + self.model.ref,point[1])
            point3 = (point[0] + self.model.ref,point[1] + self.model.ref)
            point4 = (point[0],point[1] + self.model.ref)
            pygame.draw.line(self.screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1]),CartToIso(point2[0],point2[1]),1)
            pygame.draw.line(self.screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1]),CartToIso(point3[0],point3[1]),1)
            pygame.draw.line(self.screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1]),CartToIso(point4[0],point4[1]),1)
            pygame.draw.line(self.screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1]),CartToIso(point1[0],point1[1]),1)

        pygame.display.update()