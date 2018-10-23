from ga import *
from 
grid = [Model(200, "hello") for i in range(3)]

for i in range(50):
    for a in grid:
        a.nextGeneration(30, .1)

[print(a.BEST_SPECIES) for a in grid]
