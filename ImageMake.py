import numpy as np
import scipy.misc as smp

def makeImage(letterMat):
    width = len(letterMat[0])
    height = len(letterMat)

    data = np.zeros( (height, width,3), dtype=np.uint8 )

    for y in range(len(letterMat)):
        for x in range(len(letterMat[y])):
            data[y, x] = [((ord(letterMat[y][x]) - 80) * 200),((ord(letterMat[y][x]) - 80) * 200),((ord(letterMat[y][x]) - 80) * 200)]

    img = smp.toimage( data )       # Create a PIL image
    img.show()                      # View in default viewer
