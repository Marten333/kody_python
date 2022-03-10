# FUNKCJA KWADRATOWA

import matplotlib.pyplot as plt
from math import *

def wykres(d_x,d_y,a,b,c,rozwiazania,zera):
    # tworzenie y-kow dla ktorych ma sie narysowac funkcja
    for x in range(-100,100,1):
        y=a*(x**2)+b*x+c
        d_x.append(x)
        d_y.append(y)

    fig= plt.figure()
    axes=fig.add_subplot(111)
    axes.plot(d_x,d_y)
    # wyrysowanie miejsc zerowych
    plt.scatter(rozwiazania,zera)
    # pokazanie funkcji
    plt.show()


def main():
    d_x=[]
    d_y=[]

    a=float(input("Podaj a: "))
    b=float(input("Podaj b: "))
    c=float(input("Podaj c: "))

    # tworzenie tablicy z ktorej pozniej zaleznie od ilosci rozwiazan wyrysuje sie tyle miejsc zerowych
    rozwiazania=[]

    delta=b**2-4*a*c
    print("Delta jest rowna: ",delta)
    if(delta<0):
        print("Funkcja nie ma rozwiazan")
        zera=[]
    elif(delta==0):
        x0=((-1)*b)/(2*a)
        zera=[0]
        rozwiazania.append(x0)
        print("Funkcja ma jedno rozwiazanie x0 rowne: ",round(x0,2))
    elif(delta>0):
        zera=[0,0]
        x1=((-1)*b-sqrt(delta))/(2*a)
        x2=((-1)*b+sqrt(delta))/(2*a)
        rozwiazania.append(x1)
        rozwiazania.append(x2)
        print("Funkcja ma dwa rozwiazania, x1=",round(x1,2)," , x2=",round(x2,2))

    czy=input("Czy chcesz by program wyrysowal wykres funckji?(TAK/NIE): ")
    if(czy=="TAK"):
        wykres(d_x,d_y,a,b,c,rozwiazania,zera)
    elif(czy=="NIE"):
        return 1

main()
