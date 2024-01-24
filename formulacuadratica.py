from math import sqrt
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
determinante=(b**2)-(4*a*c)
if(determinante<=0):
    print("La raiz es negativa")
else:
    x1=(-b+sqrt(determinante))/(2*a)
    x2=(-b-sqrt(determinante))/(2*a)
    print("Los resultados son: ",x1,"y: ",x2)
