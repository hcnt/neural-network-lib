import numpy as np
import math


def addRandomValue(x, chance, value):
    random = np.random.rand()
    if (random < chance):
        return x + ((np.random.rand() * value) - (value / 2))
    else:
        return x


addRandomValueVectorized = np.vectorize(addRandomValue)


class NeuralNetwork:
    def __init__(self, inputNum, hiddenNum, outputNum):
        self.inputNum = inputNum
        self.hiddenNum = hiddenNum
        self.outputNum = outputNum
        self.fitness = 0

        self.weights_ih = np.random.uniform(-1, 1, (hiddenNum, inputNum))
        self.weights_ho = np.random.uniform(-1, 1, (outputNum, hiddenNum))
        self.biases_ih = np.random.uniform(-1, 1, hiddenNum)
        self.biases_ho = np.random.uniform(-1, 1, outputNum)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feedforward(self, input):
        hidden = np.matmul(self.weights_ih, input)
        hidden += self.biases_ih
        hidden = self.sigmoid(hidden)

        output = np.matmul(self.weights_ho, hidden)
        output += self.biases_ho
        output = self.sigmoid(output)

        return output

    @staticmethod
    def crossover(nn1, nn2):
        nn = NeuralNetwork(nn1.inputNum, nn1.hiddenNum, nn1.outputNum)
        # print(nn1.weights_ih)
        # print(nn2.weights_ih)
        nn.weights_ih = np.mean([nn1.weights_ih, nn2.weights_ih], axis=0)
        nn.weights_ho = np.mean([nn1.weights_ho, nn2.weights_ho], axis=0)
        nn.biases_ho = np.mean([nn1.biases_ho, nn2.biases_ho], axis=0)
        nn.biases_ho = np.mean([nn1.biases_ho, nn2.biases_ho], axis=0)

        return nn

    def clone(self):
        nn = NeuralNetwork(self.inputNum, self.hiddenNum, self.outputNum)
        nn.weights_ih = np.copy(self.weights_ih)
        nn.weights_ho = np.copy(self.weights_ho)
        nn.biases_ih = np.copy(self.biases_ih)
        nn.biases_ho = np.copy(self.biases_ho)

        return nn

    def mutate(self, mutationRate, maxValue):
        # print(self.weights_ih)
        self.weights_ih = addRandomValueVectorized(self.weights_ih,
                                                   mutationRate, maxValue)
        # print(self.weights_ih)
        # print()


nn1 = NeuralNetwork(2, 2, 1)
print(nn1.weights_ih)
