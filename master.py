from ga import *
import ImageMake
from math import floor
import matplotlib.pyplot as plt
from collections import deque

convergencePicture = ImageMake.generateMat('convergencePictures/checkerboard.jpg')

models = [Model(80, row) for row in convergencePicture]
s = [[int(str(x)) for x in a.BEST_SPECIES] for a in models]
ImageMake.makeImage(convergencePicture, show=True)
ImageMake.makeImage(s, name = 'EvolutionSnapShots/Initialized.jpg', save=True)

convergedRows = [False] * len(models)
mutationRates = [.1] * len(models)
eliteSizes = [40] * len(models)

for generation in range(10000):
    for rowIndex in range(len(models)):
        if not convergedRows[rowIndex]:
            mutationRate = mutationRates[rowIndex]

            model = models[rowIndex]
            model.nextGeneration(eliteSizes[rowIndex], mutationRate)

            error = model.BEST_ERROR

            print('\rGeneration {:3d}: Row {:2d}: {:.2f}'.format(generation, rowIndex, error), end='')

            if error < 800:
                convergedRows[rowIndex] = True

    s = [[int(str(x)) for x in a.BEST_SPECIES] for a in models]
#    ImageMake.makeImage(s, name='EvolutionSnapShots/{}.jpg'.format(generation), save=True)
    ImageMake.makeImage(s, name='EvolutionSnapShots/0.jpg', save=True)

    if not False in convergedRows:
        break
