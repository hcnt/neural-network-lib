#import neuralNetwork as nn
#import population as pop
import kik_tui_ai
import math



#population = pop.Population(10,2,2,1) 

#wynik = population.train(zagraj,20)

def wygenerujRuch(plansza):
    plansza1 = []
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            plansza1.append(plansza[i][j])
    print(plansza1)
    wynik = math.(nn.feedforward(plansza1)[0] * 10)
    print(wynik)
        
    

wygenerujRuch([[1,1,1],[0,0,0],[0,1,0]])
