ref = 50
swidth = 15 * ref
sheight = 15 * ref
SQUARELENGTH=50
WHITE = (255, 255, 255)

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