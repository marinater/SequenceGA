import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
import string

class SequenceElement:
    def __init__(self, val):
        self.value = str(val)

    def error(self, targetVal):
        return abs(ord(targetVal) - ord(self.value))

    def __repr__(self):
        return self.value

class Fitness:
    def __init__(self, sequence, targetSeq):
        self.targetSequence = targetSeq
        self.sequence = sequence
        self.error = 0
        self.fitness = 0

    def sequenceError(self):
        if self.error == 0:
            errorSum = 0

            for index, sequenceElement in enumerate(self.sequence):
                errorSum += self.sequence[index].error(self.targetSequence[index])

            self.error = errorSum

        return self.error

    def sequenceFitness(self):
        if self.fitness == 0:
            if self.sequenceError() == 0:
                return 99999999999999999999999
            self.fitness = 1 / float(self.sequenceError())

        return self.fitness

def initialPopulation(popSize, targetLength):
    population = []

    for i in range(0, popSize):
        newElement = sequenceListFromValues(createSequence(targetLength))
        population.append(newElement)

    return population

def createSequence(targetLength):
    sequence = random.sample(string.ascii_lowercase, targetLength)
    return sequence

def sequenceListFromValues(values):
    returnSequenceList = []
    for letter in values:
        returnSequenceList.append(SequenceElement(letter))
    return returnSequenceList

def rankSequences(population, targetSequence):
    sequenceList = {}
    rankedSequences = {}
    for index, element in enumerate(population):
        sequenceList[index] = Fitness(element, targetSequence).sequenceFitness()

    return sorted(sequenceList.items(), key = operator.itemgetter(1), reverse = True)

def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns= ["Index", "Fitness"])
    df['cumulativeSum'] = df.Fitness.cumsum()
    df['cumulativePercentages'] = 100 * df.cumulativeSum / df.Fitness.sum()

    for i in range(eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def MatingPool(population, selectionResults):
    matingPool = []

    for i in range(len(selectionResults)):
        index = selectionResults[i]
        matingPool.append(population[index])
    return matingPool

def breed(parent1, parent2):
    child = ''
    splicePoint = int(random.random() * len(parent1))
    child = parent1[0:splicePoint] + parent2[splicePoint:]
    return sequenceListFromValues(child)

def breedPopulation(matingPool, eliteSize):
    children = []
    length = len(matingPool) - eliteSize
    pool = random.sample(matingPool, len(matingPool))

    for i in range(0, eliteSize):
        children.append(matingPool[i])
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingPool) - i - 1])
        children.append(child)

    return children

def mutate(sequence, mutationRate):
    for swapped in range(len(sequence)):
        if(random.random() < mutationRate):
            swappedWith = int(random.random() * len(sequence))

            sequence1 = sequence[swapped]
            sequence2 = sequence[swappedWith]

            sequence[swapped] = sequence2
            sequence[swappedWith] = sequence1

    return sequence

def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)

    return mutatedPop

def nextGeneration(currentGeneration, eliteSize, mutationRate, targetSequence):
    popRanked = rankSequences(currentGeneration, targetSequence)
    selectionResults = selection(popRanked, eliteSize)
    matingPool = MatingPool(currentGeneration, selectionResults)
    children = breedPopulation(matingPool, eliteSize)
    return mutatePopulation(children, mutationRate)

def geneticAlgorithm(targetSequence, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, len(targetSequence))
    progress = []

    print("Initial minimum is:                          ", pop[rankSequences(pop, targetSequence)[0][0]])
    print("Initial error is", (1/rankSequences(pop, targetSequence)[0][1]) )

    progress.append(1 / rankSequences(pop, targetSequence)[0][1])
    plt.ylabel('Error')
    plt.xlabel('Generation')

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate, targetSequence)
        progress.append(1 / rankSequences(pop, targetSequence)[0][1])
    plt.plot(progress)
    plt.show()

    print("After, 1000 generation, the final sequence is: ", pop[rankSequences(pop, targetSequence)[0][0]])
    print("Final error is", 1 / rankSequences(pop, targetSequence)[0][1])
geneticAlgorithm("fuckthisshit", 200, 30, 0.105, 1000)
