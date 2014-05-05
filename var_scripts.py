import math

ref = 50
swidth = 14 * ref
sheight = 14 * ref
size = (1280, 720)
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

def empty(seq):
    try:
        return all(map(empty, seq))
    except TypeError:
        return False