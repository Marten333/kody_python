# REGRESJA LINIOWA

import matplotlib.pyplot as plt

def wczytaj_dane(dane_x,dane_y,n):

    # wczytywanie x-ow i y-ow z ktorych pozniej oblicze a i b
    print("Podaj dane funkcji: ")
    for i in range(n):
        x=float(input())
        dane_x.append(x)
        y=float(input())
        dane_y.append(y)

def oblicz_a(dane_x,dane_y,n):

    # obliczanie a
    licznik=0
    mianownik=0
    suma_xy=0
    suma_x=sum(dane_x)
    suma_y=sum(dane_y)
    suma_xkw=0
    for i in range(n):
        suma_xy+=dane_x[i]*dane_y[i]
        suma_xkw+=dane_x[i]**2
    licznik=(n*suma_xy)-(suma_x*suma_y)
    mianownik=(n*suma_xkw)-(suma_x**2)
    return licznik/mianownik

def oblicz_b(dane_x,dane_y,n):

    # obliczanie b
    srednia_y=sum(dane_y)/n
    srednia_x=sum(dane_x)/n
    a=oblicz_a(dane_x, dane_y, n)
    wynik=srednia_y-(a*srednia_x)
    return wynik

def oblicz_wynik(key,a,b):

    # obliczanie wyniku dla podanego argumentu funkcji
    y=a*key + b
    return y

def wykres(dane_x,dane_y,a ,b):

    #wyrysowanie wykresu
    plt.scatter(dane_x,dane_y)
    naj=max(dane_x)
    plt.plot([0, naj], [b+a*(0), b+a*naj], color="red")
    plt.show()

def main():
    dane_x=[]
    dane_y=[]
    n=int(input("Podaj ilosc posiadanych danych funkcji: "))
    wczytaj_dane(dane_x,dane_y,n)
    a=oblicz_a(dane_x,dane_y,n)
    b=oblicz_b(dane_x,dane_y,n)
    key=float(input("Podaj argument dla ktorego chcesz wyznaczyc wynik: "))
    wynik=oblicz_wynik(key,a,b)
    print("Wynik dla podanego argumentu to ok.: ", round(wynik,2))
    dane_x.append(key)
    dane_y.append(wynik)

    czy=int(input("Czy chcesz zeby program wyrysowal wykres regresji?(1 - TAK, 0 - NIE): "))
    if(czy==1):
        wykres(dane_x,dane_y,a,b)
    else:
        return 1

main()