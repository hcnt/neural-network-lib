import neuralNetwork
import population as pop
import kik_tui_ai as kik
import numpy as np
import math
import pickle


def wygenerujRuch(plansza, nn):
    plansza1 = []
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            plansza1.append(plansza[i][j])
    #print(plansza1)
    #print(nn.weights_ih)
    wynik = nn.feedforward(plansza1)
    while (True):
        print(wynik)
        maximum = np.argmax(wynik)
        print(maximum)
        if (plansza[maximum // 3][maximum % 3] == 0):
            return maximum // 3, maximum % 3
        else:
            wynik[maximum] = 0


def obliczFitness(nn):
    fitness = 0
    czyZaczyna = 1
    wygrane = 0
    remisy = 0
    for i in range(5000):
        wynik = kik.partia(1, czyZaczyna, wygenerujRuch, nn)
        if wynik == 1:
            wygrane += 1
            fitness += 10
        elif (wynik == 0):
            remisy += 1
            fitness += 10

        czyZaczyna *= -1
    #print("Wygrane:" + str(wygrane))
    # print("Remisy:" + str(remisy))
    # print()
    return fitness**3, wygrane, remisy


population = pop.Population(500, 9, 27, 9)

wynik = population.train(obliczFitness, 500)

with open('wynik.pkl', 'wb') as output:
    pickle.dump(wynik, output, pickle.HIGHEST_PROTOCOL)
