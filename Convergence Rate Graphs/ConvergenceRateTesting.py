from ga import *
import ImageMake
from math import floor
import matplotlib.pyplot as plt

def generateCurrentImage(toSave = 'False', toShow = 'False', imName = 'output.jpg'):
    a = []
    for row in grid:
        elements = [str(item) for item in row.BEST_SPECIES]
        a.append(elements)
    ImageMake.makeImage(a, show = toShow, save = toSave, name = imName)


def runTest(populationSize, mutationRate, eliteSize, k):
    print("Initializing population", k)
    grid = [Model(populationSize, "a" * 20) for i in range(20)]
    print("\tPopulation initialized")

    finished = [False]  * len(grid)
    gridRows = len(grid)

    results = []

    for i in range(1000):
        generationError = 0
        print('\tGeneration {:<30}'.format(str(i)))

        for index, a in enumerate(grid):
            if finished[index] == False:
                a.nextGeneration(eliteSize, mutationRate)
                error = a.BEST_ERROR
                generationError += error
                if error == 0.0:
                    finished[index] = True
                percentComplete = int((index / gridRows) * 30) + 1
                print('\r\t|{:<30}|'.format('*'*percentComplete), end='')

        print('\r\t     {:<28}'.format(str(floor(generationError))),end='\n')
        results.append(generationError)

        if not False in finished:
            return i, results

    return 1000, results

testVals = range(0,50,10)
data = []

#for y in testVals:
    convergenceTime, results = runTest(50 ,.3, y, y)

#    data.append(results)

#dataFrames = [pd.DataFrame(data = {'{}'.format(x * .05) : data[x]}) for x in range(len(testVals))]#

#axis1 = dataFrames[0].plot()
#[x.plot(ax = axis1) for x in dataFrames[1:]]
#plt.show()
