import math

ref = 50
swidth = 15 * ref
sheight = 15 * ref
SQUARELENGTH=50
WHITE = (255, 255, 255)
centerx = 640/2
centery = 480/2

def CartToIso(x,y,z=10):
    """Takes an x and y pair and converts them to isometric position."""
    
    isox = x - y+centerx 
    isoy = (x+y)/2 - z
    return (isox,isoy)

def IsoToCart(isoX,isoY):
    """Takes an isometric position and converts them to an x and y pair."""
    cartX = (2 * (isoY) + isoX) / 2 + centerx 
    cartY = (2 * (isoY) - isoX) / 2 + centery
    return (cartX, cartY)