from Global_variables import *

def CartToIso(x,y):
	"""Takes an x and y pair and converts them to isometric position."""
	isox = x - y + centerx
	isoy = (x + y) / 2
	return (isox, isoy)

def IsoToCart(x,y):
    """Takes an isometric position and converts them to an x and y pair."""
    isox = isox - centerx
    cartX = (2 * isoY + isoX) / 2
    cartY = (2 * isoY - isoX) / 2
    return (cartX, cartY)