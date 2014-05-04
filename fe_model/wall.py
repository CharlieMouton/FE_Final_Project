import block
class Wall(block.Block):
    """ A basic wall structure that stops the character."""
    def __init__(self, model, x, y):
        Block.__init__(self, wallcolor, x, y)
        self.image = pygame.image.load('fe_model/images/wall.png')
