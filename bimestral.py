from sys import float_info
print("------------------------------------")
print("----------Elije tu grafica----------")
print("------------------------------------")
import numpy as np
import matplotlib.pyplot as plt
import math as m
from matplotlib import pyplot
from numpy import linspace, pi, sin 
from matplotlib.pyplot import plot, show, xlim,ylim,xticks
 
# input
bandera = False 


print("¿Cual funcion deseas realizar?: \n")
print("1. Lineal ")
print("2. cuadratica")
print("3. cubica")
print("4. Logaritmica")
print("5. Exponencial ")
print("6. Trigonometrica")

opcion = int(input(" Dame la opcion que deseas: "))

if (opcion == 1):
  N = 100
  def f(m,x,b):
    return m*x + b

  m = int(input("Digite el valor de la pendiente: "))
  b = int(input("Digite el valor de el punto de corte con el eje y: "))
  x = np.linspace(-10, 10, num = N)
  y = f(m,x,b)
  pyplot.plot(x,y, color = "r")
  pyplot.xlabel("x")
  pyplot.ylabel("y")
  pyplot.title("Funcion lineal: y =mx + b")
  pyplot.grid()
  pyplot.axhline(y=0, color ="b")
  pyplot.axvline(x =0, color = "b")
  pyplot.show()
  pyplot.savefig("funcion_lineal.png")


elif (opcion == 2): # Cuadratica 
  a =float(input("ingrese el valor de (a):\n"))
  b=float(input("ingrese el valor de (b):\n"))
  c=float(input("ingrese el valor de (c):\n"))
  disc=(b**2)-(4*a*c)
  raiz=(disc)**(0.5)

  if(disc>0):
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("x1= ",x1)
    print("x2= ",x2)

  elif(disc==0):
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("x1= ",x1)
    print("x2= ",x2)
  else:
    print("Solucion imaginaria")

  def f(x):
    return a*(x**2)+b*x+c

  x = np.linspace(-100,50+np.pi,100)

  pyplot.plot(x,[f(i)for i in x])

  pyplot.axhline(0, color= "black")
  pyplot.axvline(0, color= "black")

  pyplot.xlim(-50,50)
  pyplot.ylim(-50,50)

  pyplot.show()


elif(opcion == 3): # Cubica
  def funcion(a,b,c,d, x):
   return a*x**3 +b*x**2+c*x+d
  N=100
  a =float(input("ingrese el valor de (a): "))
  b =float(input("ingrese el valor de (b): "))
  c =float(input("ingrese el valor de (c): "))
  d =float(input("ingrese el valor de (c): "))


  x = np.linspace(-10, 10, num = N)
  y= funcion(a,b,c,d, x)
  pyplot.plot(x,y, color = "r")
  pyplot.axhline(0, color= "black")
  pyplot.axvline(0, color= "black")

  pyplot.show()
  
elif(opcion == 4): #Logaritmica 
  N = 100
  x = np.linspace(-10, 10, num = N)
  y = np.log(x)
  
  pyplot.plot(x,y)
  pyplot.axhline(0, color= "black")
  pyplot.axvline(0, color= "black")
  pyplot.show()

elif(opcion == 5): # Exponencial 
  a = float(input(" Dame el valor de a: "))
  x= np.linspace(-10,10,100)
  y = a**x                  
  pyplot.plot(x,y, color = "r")
  pyplot.axhline(0, color= "black")
  pyplot.axvline(0, color= "black")
  pyplot.show()

elif(opcion == 6):
  op=int(input("\nDigite 1 para el Seno, 2 Para el Coseno,  Digite: "))
  if op==1:
    x= np.linspace(-np.pi, np.pi, 256)
    y=np.sin(x)

    plt.plot(x,y)
    plt.ylim(-2,2)
    plt.show()


  elif op==2:
    x= np.linspace(-np.pi, np.pi, 256)
    y=np.cos(x)

    plt.plot(x,y)
    plt.ylim(-2,2)
    plt.show()