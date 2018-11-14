import numpy as np
import scipy.misc as smp
from PIL import Image

def makeImage(numberMat, name = 'Output.jpg', show = False, save = False):
    width = len(numberMat[0])
    height = len(numberMat)

    data = np.zeros( (height, width,3), dtype=np.uint8 )

    for y in range(len(numberMat)):
        for x in range(len(numberMat[y])):
            pixel = [numberMat[y][x] , numberMat[y][x], numberMat[y][x]]
            data[y, x] = pixel

    img = smp.toimage( data )       # Create a PIL image
    img = img.resize((50*width, 50*height))
    if show:
        img.show()                      # View in default viewer
    if save:
        img.save(name)

def generateMat(name = 'creeper.jpg'):
    im = Image.open(name)
    width, height = im.size
    blocksPerSide = 20
    mat = []

    for x in range(blocksPerSide):
        row = []
        for y in range(blocksPerSide):
            stepX = 25
            offsetX = stepX // 2

            stepY = 25
            offsetY = stepY // 2

            pixel = im.getpixel((offsetY + stepY*y, offsetX + stepX*x))
            row.append(pixel[1])
        mat.append(row)
    return mat
