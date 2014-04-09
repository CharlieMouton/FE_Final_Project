import math

ref = 50
swidth = 15 * ref
sheight = 15 * ref
size = (1024, 768)
SQUARELENGTH=50
WHITE = (255, 255, 255)
centerx = size[0]/2
centery = size[1]/2

def CartToIso(x,y,z=10):
    """Takes an x and y pair and converts them to isometric position."""
    
    isox = x - y+centerx 
    isoy = (x+y)/2 - z
    return (isox,isoy)

def IsoToCart(isoX,isoY):
    """Takes an isometric position and converts them to an x and y pair."""
    isoX = isoX - centerx
    cartX = (2 * (isoY) + isoX) / 2  
    cartY = (2 * (isoY) - isoX) / 2
    return (cartX, cartY)