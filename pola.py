''' napiszesz progrma liczący pola '''

import math
from enum import IntEnum

def PoleProstokąta(a,b):
    return a*b

def PoleKwadratu(a):
    return a**2

def PoleTrójkąta(a,h):
    return a*h/2

def PoleKoła(r):
    return (math.pi)*r**2

def PoleTrpezu(a,b,h):
    return (a+b)*h/2

Menu_Funkcji = IntEnum('Menu_Funkcji', 'Prostokat, Kwadrat, Trojkat, Kolo, Trapez, Koniec')

while(True):

    print(" Poniżej znajdują się pewne możliwosści, dokonaj wyboru: ")
    print(" 1 - Oblicz pole prostokąta ")
    print(" 2 - Oblicz pole kwadratu ")
    print(" 3 - Oblicz pole trójkąta ")
    print(" 4 - Oblicz pole koła ")
    print(" 5 - Oblicz pole trapezu ")
    print(" 6 - Zakończ program ")

    wybor = int(input(" Wybierz co chcesz zrobić: "))

    if wybor == Menu_Funkcji.Prostokat:
        print(" WYbrano liczenie pola protstokąta ")
        a = float(input(" Popdaj wartość boku a: "))
        b = float(input(" Podaj wartość boku b: "))
        if (a or b) < 0:
            print(" Długości bokó nie mogą być ujemne! ")
        else:
            Pole = PoleProstokąta(a,b)  
            print(" Pole prostokąta wynosi: ", Pole)

    if wybor == Menu_Funkcji.Kwadrat:
        print(" WYbrano liczenie pola kwadratu ")
        a = float(input(" Popdaj wartość boku a: "))
        if a < 0:
            print(" Długości boków nie mogą być ujemne! ")
        else:
            Pole = PoleKwadratu(a)  
            print(" Pole kwadratu wynosi: ", Pole)
        
    if wybor == Menu_Funkcji.Trojkat:
        print(" WYbrano liczenie pola trójkąta ")
        a = float(input(" Popdaj wartość boku a: "))
        h = float(input(" Podaj wartość boku h: "))
        if (a or h) < 0:
            print(" Długości boków nie mogą być ujemne! ")
        else:
            Pole = PoleTrójkąta(a,h)  
            print(" Pole trójkąta wynosi: ", Pole)

    if wybor == Menu_Funkcji.Kolo:
        print(" WYbrano liczenie pola kołą ")
        r = float(input(" Popdaj wartość promienia r: "))
        if r < 0:
            print(" Długości bokó nie mogą być ujemne! ")
        else:
            Pole = PoleKoła(r)  
            print(" Pole koła wynosi: ", Pole)

    if wybor == Menu_Funkcji.Trapez:
        print(" WYbrano liczenie pola trapezu ")
        a = float(input(" Popdaj wartość boku a: "))
        b = float(input(" Podaj wartość boku b: "))
        h = float(input(" Podaj wartość wysokości h:  "))
        if (a or b or h) < 0:
            print(" Długości boków  nie mogą być ujemne! ")
        else:
            Pole = PoleTrpezu(a,b,h)  
            print(" Pole trapezu wynosi: ", Pole)

    if wybor == Menu_Funkcji.Koniec:
        print(" WYbrano wyłączenie programu ")
        break
    else:
        break