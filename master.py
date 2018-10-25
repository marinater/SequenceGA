from ga import *
<<<<<<< HEAD
=======
grid = [Model(200, "hello") for i in range(3)]
>>>>>>> b0215e1cdfd722d207c59a247351e40dbc12808e

grid = [Model(200, "a" * 200) for i in range(200)]
finished = [False]  * len(grid)

for i in range(1):
#    print('Generation {:2d} '.format(i))
    for index, a in enumerate(grid):
        if finished[index] == False:
            a.nextGeneration(30, .1)
            error = a.BEST_ERROR
            if error == 0.0:
                finished[index] = True
            print('----------------------------------')
            print(
            '''Generation: {}
            Error     : {:g}
            Sequence  : {}'''.format(i, error, a.BEST_SPECIES))
    if not False in finished:
        break

a = []
for row in grid:
    elements = [str(item) for item in row.BEST_SPECIES]
    a.append(elements)

import ImageMake
ImageMake.makeImage(a)
