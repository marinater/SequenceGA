from ga import *
import ImageMake

def generateCurrentImage(name):
    a = []
    for row in grid:
        elements = [str(item) for item in row.BEST_SPECIES]
        a.append(elements)
    ImageMake.makeImage(a, name)

print("Initializing population")
grid = [Model(200, "aaaaazzzzz" * 2) for i in range(10)]
print("Population initialized")

finished = [False]  * len(grid)
gridRows = len(grid)


for i in range(1):
    generationError = 0
    print('Generation {:<30}'.format(str(i)))
    for index, a in enumerate(grid):
        if finished[index] == False:
            a.nextGeneration(30, .1)
            error = a.BEST_ERROR
            generationError += error
            if error == 0.0:
                finished[index] = True
            percentComplete = int((index / gridRows) * 30) + 1
            print('\r|{:<30}|'.format('*'*percentComplete), end='')
    print('\r',end='')
    if not False in finished:
        break

generateCurrentImage('initalized.jpg')

for i in range(100):
    generationError = 0
    print('Generation {:<30}'.format(str(i)))
    for index, a in enumerate(grid):
        if finished[index] == False:
            a.nextGeneration(30, .1)
            error = a.BEST_ERROR
            generationError += error
            if error == 0.0:
                finished[index] = True
            percentComplete = int((index / gridRows) * 30) + 1
            print('\r|{:<30}|'.format('*'*percentComplete), end='')
    print('\r',end='')
    if not False in finished:
        break

generateCurrentImage('output.jpg')
