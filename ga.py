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

class Model():
    def __init__(self, popSize, targetVal):
        self.TARGET = targetVal
        self.CURRENT_POPULATION = self.initialPopulation(popSize)

    def initialPopulation(self, popSize):
        population = []

        for i in range(0, popSize):
            newElement = self.sequenceListFromValues(self.createSequence(len(self.TARGET)))
            population.append(newElement)

        return population

    def createSequence(self, targetLength):
        sequence = random.sample(string.ascii_lowercase, targetLength)
        return sequence

    def sequenceListFromValues(self, values):
        returnSequenceList = []
        for letter in values:
            returnSequenceList.append(SequenceElement(letter))
        return returnSequenceList

    def rankSequences(self, population, targetSequence):
        sequenceList = {}
        rankedSequences = {}
        for index, element in enumerate(population):
            sequenceList[index] = Fitness(element, targetSequence).sequenceFitness()

        return sorted(sequenceList.items(), key = operator.itemgetter(1), reverse = True)

    def selection(self, popRanked, eliteSize):
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

    def MatingPool(self, population, selectionResults):
        matingPool = []

        for i in range(len(selectionResults)):
            index = selectionResults[i]
            matingPool.append(population[index])
        return matingPool

    def breed(self, parent1, parent2):
        child = ''
        splicePoint = int(random.random() * len(parent1))
        child = parent1[0:splicePoint] + parent2[splicePoint:]
        return self.sequenceListFromValues(child)

    def breedPopulation(self, matingPool, eliteSize):
        children = []
        length = len(matingPool) - eliteSize
        pool = random.sample(matingPool, len(matingPool))

        for i in range(0, eliteSize):
            children.append(matingPool[i])
        for i in range(0, length):
            child = self.breed(pool[i], pool[len(matingPool) - i - 1])
            children.append(child)

        return children

    def mutate(self, sequence, mutationRate):
        for swapped in range(len(sequence)):
            if(random.random() < mutationRate):
                swappedWith = int(random.random() * len(sequence))

                sequence1 = sequence[swapped]
                sequence2 = sequence[swappedWith]

                sequence[swapped] = sequence2
                sequence[swappedWith] = sequence1

        return sequence

    def mutatePopulation(self, population, mutationRate):
        mutatedPop = []

        for ind in range(len(population)):
            mutatedInd = self.mutate(population[ind], mutationRate)
            mutatedPop.append(mutatedInd)

        return mutatedPop

    def nextGeneration(self, eliteSize, mutationRate):
        popRanked = self.rankSequences(self.CURRENT_POPULATION, self.TARGET)
        selectionResults = self.selection(popRanked, eliteSize)
        matingPool = self.MatingPool(self.CURRENT_POPULATION, selectionResults)
        children = self.breedPopulation(matingPool, eliteSize)
        self.CURRENT_POPULATION = self.mutatePopulation(children, mutationRate)
        self.BEST_SPECIES = self.CURRENT_POPULATION[self.rankSequences(self.CURRENT_POPULATION, self.TARGET)[0][0]]
        return self.CURRENT_POPULATION
