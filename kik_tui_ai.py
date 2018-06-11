from kik_plansza import *
from kik_kom import *
from kik_ai_los import *
import os


def wyswietl_plansze(plansza):
    print("-------------------")
    for i in range(len(plansza)):
        print("|  " + pionek(plansza[i][0]) + "  |  " + pionek(plansza[i][1]) +
              "  |  " + pionek(plansza[i][2]) + "  |")

        print("-------------------")


# tryb 0 - człowiek vs człowiek
# tryb 1 - człowiek vs komputer
# tryb 2 - komputer vs komputer


def partia(symbol_gracza, zaczynajacySymbol, aiGenerujRuch, nn):

    plansza = nowa_pusta_plansza()
    czy_ruch_wykonany = False
    czy_gra_skonczona = False
    gracz = zaczynajacySymbol
    wygrany_gracz = 0
    while (not czy_gra_skonczona):
        #print()
        # wyswietl_plansze(plansza)
        if (gracz == symbol_gracza):
            #  print(kom_ruch(gracz))
            wiersz, kolumna = aiGenerujRuch(plansza, nn)
        else:
            wiersz, kolumna = wybierz_ruch(plansza, gracz)
        # print(kom_ruch_przeciw(gracz, wiersz, kolumna))

        czy_ruch_wykonany, plansza, gracz = wykonaj_ruch(
            plansza, gracz, wiersz, kolumna)

        czy_gra_skonczona, wygrany_gracz = koniec_gry(plansza)
    #wyswietl_plansze(plansza)
    #print(kom_koniec(wygrany_gracz))
    return (wygrany_gracz)


def zamienZaczynajacySymbol(symbol):
    if (symbol == -1):
        return 1
    else:
        return -1
