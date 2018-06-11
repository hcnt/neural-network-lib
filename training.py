import neuralNetwork
import population as pop
import kik_tui_ai as kik
import math


def wygenerujRuch(plansza, nn):
    plansza1 = []
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            plansza1.append(plansza[i][j])
    #print(plansza1)
    #print(nn.weights_ih)
    wynik = math.floor(nn.feedforward(plansza1)[0] * 100)
    wynik = wynik % 9
    #print(wynik)
    i = 0
    j = 0
    while (True):
        if (plansza[i][j] == 0):
            wynik -= 1
            if (wynik <= 0):
                return i, j
        j += 1
        if (j > 2):
            j = 0
            i += 1
        if (i > 2):
            i = 0
            j = 0


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


population = pop.Population(500, 9, 27, 1)

wynik = population.train(obliczFitness, 500)
print(wynik)
