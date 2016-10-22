import numpy
import matplotlib.pyplot as plt
import math as m
import sys

#---------definicje funkcji:----------

#f(x)=exp(x)
def licz_f1():
    for wart in x:
        y.append((m.exp(wart)))
        y1.append((m.exp(wart+h)-m.exp(wart))/h)
        y2.append((m.exp(wart+h)-m.exp(wart-h))/(2*h))
    return 0

#f(x)=exp(-x**2)
def licz_f2():
    for wart in x:
        y.append( (-2)*wart*m.exp(-(wart**2)) )
        y1.append( (m.exp(-((wart+h)**2))-m.exp(-(wart**2)))/h )
        y2.append( (m.exp(-((wart+h)**2))-m.exp(-((wart-h)**2)))/(2*h) )
    return 0

#f(x)=(x**2)*log(x)
def licz_f3():
    for wart in x:
        y.append( wart+2*wart*m.log(wart) )
        y1.append( (((wart+h)**2)*m.log(wart+h)-((wart**2)*m.log(wart)))/h )
        y2.append( ((wart+h)**2*m.log(wart+h)-(wart-h)**2*m.log(wart-h))/(2*h) )
    return 0

#f(x)=(x**2)*log(x)
def licz_f4():
    for wart in x:
        y.append( (-wart)/((m.sqrt(1+wart**2))**3) )
        y1.append( (1/(m.sqrt(1+(wart+h)**2))-1/(m.sqrt(1+wart**2)))/h )
        y2.append( (1/(m.sqrt(1+(wart+h)**2))-1/(m.sqrt(1+(wart-h)**2)))/(2*h) )
    return 0

def rysuj():
    plt.figure(1)
    plt.subplot(311)
    plt.grid(True)
    plt.plot(x, y)
    plt.ylabel("f'(x)")
    plt.subplot(312)
    plt.grid(True)
    plt.plot(x, y1)
    plt.ylabel("f'^(x)")
    plt.subplot(313)
    plt.grid(True)
    plt.plot(x, y2)
    plt.ylabel("f'^^(x)")
    plt.xlabel("x")
    plt.figure(2)
    plt.grid(True)
    plt.plot(x, z1, x, z2)
    plt.show()
    return 0

#---------main:----------

y = [] #podstawienie x do pochodnych policzonych analitycznie
y1 = [] #liczenie pochodnej 1 sposob z dokladnioscia do O(h)
y2 = [] #liczenie pochodnej 2 sposob z dokladnoscia do O(h^2)
z1 = [] #blad pierwszego sposobu
z2 = [] #blad drugiego sposobu
h=0.000001

print ("Podaj dolna granice przedzialu, dla ktorego wykonac test:")
dol=float(raw_input()) #zmiana na float, bo domyslnie string
print ("Podaj gorna granice przedzialu, dla ktorego wykonac test:")
gora=float(raw_input())

if gora < dol:
    print("Zle dobrana granica.")
    sys.exit(0)

#metoda arange(arg1,arg2,arg3) - tworzy wektor arg1-dolna granica przedzialu
#arg2 - element nastepny po ostatnim
#arg3 - skok
x=numpy.arange(dol,gora+0.01,0.1) #definicja zakresu

print("Prosze wybrac, dla ktorej funkcji przeprowadzic test:")
print("1. f(x)=exp(x)")
print("2. f(x)=exp(-x**2)")
print("3. f(x)=(x**2)*log(x)")
print("4. f(x)=1/sqrt(1+x**2)")
wybor=int(raw_input())

if wybor==1:
    licz_f1()
elif wybor==2:
    licz_f2()
elif wybor==3:
    licz_f3()
elif wybor==4:
    licz_f4()
else :
    print("Wybrano niepoprawna opcje.")
    sys.exit(0)

#liczenie bledu wynikajacego z 1 oraz 2 przyblizenia
i=0
while i < len(y):
    z1.append(m.log(m.fabs(y[i]-y1[i])))
    z2.append(m.log(m.fabs(y[i]-y2[i])))
    i+=1

#wyrysowanie wykresu
rysuj()
