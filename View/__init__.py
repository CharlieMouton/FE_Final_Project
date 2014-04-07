class View:
    """
    Game viewer in pygame window.
    """
    def __init__(self,world,screen):
        self.model= world
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
            point2 = (point[0]+ref,point[1])
            point3 = (point[0]+ref,point[1]+ref)
            point4 = (point[0],point[1]+ref)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1]),CartToIso(point2[0],point2[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1]),CartToIso(point3[0],point3[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1]),CartToIso(point4[0],point4[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1]),CartToIso(point1[0],point1[1]),1)

        pygame.display.update()