import neuralNetwork as nn
import numpy as np


class Population:
    def __init__(self, size, inputNum, hiddenNum, outputNum):
        self.size = size
        self.population = []
        self.fitness = []
        for i in range(size):
            self.population.append(
                nn.NeuralNetwork(inputNum, hiddenNum, outputNum))
            self.fitness.append(0)

    def createMatingPool(self):
        self.population = np.random.choice(
            self.population, size=self.size, p=self.fitness)

    def pickRandomParent(self):
        return self.population[np.random.randint(0, self.size)]

    def crossover(self):
        for i in range(self.size):
            self.population[i] = nn.NeuralNetwork.crossover(
                self.pickRandomParent(), self.pickRandomParent())

    def mutate(self):
        for i in range(self.size):
            self.population[i].mutate(0.01, 0.01)

    def train(self, calculateFitnessFunc, epochs):
        for i in range(epochs):
            wygrane = 0
            remisy = 0
            print("epoch: " + str(i))
            for j in range(self.size):
                w = 0
                r = 0
                self.fitness[j], w, r = calculateFitnessFunc(
                    self.population[j])
                wygrane += w
                remisy += r
            wygrane = wygrane / self.size
            remisy = remisy / self.size
            print("śr wygrane:" + str(wygrane))
            print("śr remisy:" + str(remisy))
            print("---------------------")
            self.fitness = self.fitness / np.sum(self.fitness)
            # print(self.fitness)
            self.mutate()
            self.createMatingPool()
            self.crossover()
        return self.population


#pop = Population(10, 2, 2, 1)
#pop.train(xD, 10)
