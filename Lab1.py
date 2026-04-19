import numpy as np
from numpy.linalg import matrix_rank
import matplotlib.pyplot as plt

#Zad 2.1
a=3**12-5
print("Odpowiedz do zadania 2.1a to ",a)


macierz1=np.array([[2 ,0.5]])
macierz2=np.array([[1,4],[-1,3]])
macierz3=np.array([[-1],[-3]])
b= int(macierz1@macierz2@macierz3)
print("Odpowiedz do zadania 2.1b to ",b)


c=np.array([[1,-2,0],[-2,4,0],[2,-1,7]])    
print("Odpowiedz do zadania 2.1c to,", matrix_rank(c))
dmacierz1=np.array([[-1],[2]])
dmacierz2=np.array([[1,2],[-1, 0]])


#d
wynikd=np.linalg.solve(dmacierz2,dmacierz1)
wynikd2=np.linalg.inv(dmacierz2)@dmacierz1
print("Odpowiedz do zadania 2.1d",wynikd)
print(wynikd2)


# Zad2.2

a2=np.array([1,1,-129,171,1620])
x1=-46
x2=14
odp1=np.polyval(a2, x1)
odp2=np.polyval(a2,x2)
print("Odpwoiedz do zadana 2.2 to ", odp1,odp2)

#Zad3.1
tabela=[]
tabelka=[]
for i in range(-46,15):
    tabelka.append(i)
    odp3=np.polyval(a2, i)
    print("dla i=",i,"odp to", odp3)
    tabela.append(odp3)
argmin=np.argmin(tabela)
argmax=np.argmax(tabela)
print("Max wynik to",max(tabela),"dla x=",tabelka[argmax])
print("Min wynik to",min(tabela),"dla x=",tabelka[argmin])


#Zad 3.2
tabela2=[]
dokladnosc=0.1
tabelka2=[]
for i in np.arange(-46,15,dokladnosc):
    odp4=np.polyval(a2, i)
    print("dla i=",i,"odp to", odp4)
    tabela2.append(odp4)
    tabelka2.append(i)
argmin1=np.argmin(tabela2)
argmax1=np.argmax(tabela2)
print("Max wynik to",max(tabela2),"dla x=",tabelka2[argmax1])
print("Min wynik to",min(tabela2),"dla x=",tabelka2[argmin1])


# Zad 4.1
def zad41(wspolczynniki,a3,b3,dokladnosc3):
    tabelka3=[]
    if dokladnosc3<0:
        return 0
    else:
        wspolczynniki=np.array(wspolczynniki)
        tabela5= []
        for i in np.arange(a3,b3+1,dokladnosc3):
            tabelka3.append(i)
            odp5=np.polyval(wspolczynniki, i)
            print("dla i=",i,"odp to", odp5)
            tabela5.append(odp5)
    argmin2=np.argmin(tabela5)
    argmax2=np.argmax(tabela5)
    print("Max wynik dla zad 4 to",max(tabela5),"dla x=",tabelka3[argmax2])
    print("Min wynik dla zad 4 to",min(tabela5),"dla x=",tabelka3[argmin2])
    return np.array([min(tabela5),max(tabela5)])
print(zad41([1, 1, -129, 171, 1620], -46,15, 0.1))


# Zad 4.2 / 5.1 / 5.2

def zad42(wspolczynniki2,a4,b4,dokladnosc4):
    tabelka4=[]
    if dokladnosc4<0:
        return 0
    if len(wspolczynniki2)==0:
        return 0
    else:
        wspolczynniki2=np.array(wspolczynniki2)
        stopien=len(wspolczynniki2)-1
        tabela7= []
        for i in np.arange(a4,b4+1,dokladnosc4):
            tabelka4.append(i)
            odp6=np.polyval(wspolczynniki2, i)
            print("dla i=",i,"odp to", odp6)
            tabela7.append(odp6)
    argmin3=np.argmin(tabela7)
    argmax3=np.argmax(tabela7)
    print("Wielomian jest stopnia", stopien)
    print("Max wynik dla zad 4 to",max(tabela7),"dla x=",tabelka4[argmax3])
    print("Min wynik dla zad 4 to",min(tabela7),"dla x=",tabelka4[argmin3])
    #rysowanie
    plt.figure()
    plt.plot(tabelka4,tabela7,label="P(x)",linewidth=2,color="tab:cyan")
    plt.scatter(tabelka4[argmin3],tabela7[argmin3],s=60,marker='o',label='min')
    plt.scatter(tabelka4[argmax3],tabela7[argmax3],s=60,marker='o',label='max')
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.title(f"Wielomian stopnia {stopien} na przedziale [{a4},{b4}]")
    plt.grid(linestyle="--",alpha=0.3)
    plt.legend()
    plt.savefig("wielomian2.pdf")
    plt.show()
    return np.array([min(tabela7),max(tabela7)])

print(zad42([1, 1, -129, 171, 1620], -46,15, 0.1))
 
def wielomian(wspolczynniki5,a5,b5,dokladnosc5):
    wspolczynniki5=np.array(wspolczynniki5)
    tabelka5=[]
    for x in np.arange(a5,b5,dokladnosc):
        for i in wspolczynniki5:
            if len(wspolczynniki5)==5:
                tabelka5.append(wspolczynniki5[0]*pow(x,4)+wspolczynniki5[1]*pow(x,3)+wspolczynniki5[2]*pow(x,2))
print(pow(2,2))