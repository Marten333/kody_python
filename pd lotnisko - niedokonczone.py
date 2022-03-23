import matplotlib.pyplot as plt
import random

def stworz_macierz(n, ran,w,kol):
    M=[[4]*n for i in range(n)]
    for i in range(ran):
        k=random.randint(0,w)
        l=random.randint(0,kol)
        M[k][l]=1
    return M

def dod(M1,M2,w,k):
    n=w*k
    DOD=[[0]*n for i in range(n)]
    for i in range(w):
        for j in range(k):
            if(M1[w][k]==1 and M2[w][k]==1):
                DOD[w][k]=1
            else:
                DOD[w][k]=M1[w][k]+M2[w][k]
    return DOD

def odej(M1,M2,w,k):
    n=w*k
    ODEJ=[[0]*n for i in range(n)]
    for i in range(w):
        for j in range(k):
            if((M1[w][k]==0 and M2[w][k]==1) or (M1[w][k]==1 and M2[w][k]==0)):
                ODEJ[w][k]=1
            else:
                ODEJ[w][k]=M1[w][k]-M2[w][k]
    return ODEJ

n=int(input("Podaj ilosc miejsc w samolocie: "))
w=int(input("Podaj ilosc wierszy: "))
k=int(input("Podaj ilosc kolumn: "))
ran=int(input("Podaj ilosc losowych miejsc poczatkowych w pierwszym samolocie: "))

samolot1 = stworz_macierz(n,ran,w,k)

czy=0
while(czy==0):
    opcje=input("Podaj co chcesz zrobic(1-sprawdz czy dane miejsce jest zajete, 2-zajmij dane miejsce, 3-exit): ")
    if(opcje=='1'):
        wi=int(input("Podaj wiersz: "))
        ko=int(input("Podaj kolumne: "))
        if(samolot1[wi][ko]==1):
            print("To miejsce jest zajęte")
        else:
            print("To miejsce jest wolne")
    elif (opcje=='2'):
        wi=int(input("Podaj wiersz: "))
        ko=int(input("Podaj kolumne: "))
        if(samolot1[wi][ko]==1):
            print("To miejsce jest zajęte")
        else:
            samolot1[wi][ko]==1
    elif (opcje=='3'):
            czy+=1

ran1=int(input("Podaj ilosc losowych miejsc poczatkowych w drugim samolocie: "))

samolot2 = stworz_macierz(n,ran1,w,k)

DOD = dod(samolot1,samolot2,w,k)
ODEJ = odej(samolot1,samolot2,w,k)













