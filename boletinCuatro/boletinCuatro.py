"""1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
from math import sqrt
from _ast import In
from boletinTres.boletinCuatro import numero1

catetoUno=int(input("dime cuanto mide un cateto" ))
catetoDos=int(input("dime cuanto mide otro cateto" ))
hipotenusa=(catetoUno**2+catetoDos**2)
print(hipotenusa**0.5)

"""2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""

celsius=int(input("dime cuantos grados celsius hay " ))
print(celsius*1.8 + 32)

"""
3. Calcular la media de tres números pedidos por teclado"""


numeroUno=int(input("dime un numero  " ))
numeroDos=int(input("dime otro numero  " ))
numeroTres=int(input("dime otro numero  " ))
media =(numeroDos+numeroTres+numeroUno)/3
print(media)



"""


4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra."""
precioTotal = 40
print(40-precioTotal*0.40)


"""5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""

from math import sqrt
xUno=float(input("dime x1"))
xDos=float(input("dime x2"))
yUno=float(input("dime y1"))
yDos=float(input("dime y2"))
d=sqrt((xDos-xUno)**2+(yDos-yUno)**2)
print(d)


"""6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos."""

from math import sqrt
xUno=float(input("dime x1"))
xDos=float(input("dime x2"))
yUno=float(input("dime y1"))
yDos=float(input("dime y2"))
d=sqrt((xDos-xUno)**2+(yDos-yUno)**2)
print(d)


"""7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?"""

from math import sqrt
numero=int(input("dime un numero"))
raizDos=sqrt(numero)
raizTres=(numero**(1/3))
print("la raiz cuadrada es %s" %(raizDos))
print("la raiz cubica es %s" %(raizTres))

"""8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos)."""

dosEuros=int(input("dime cuantas monedas de dos euros tienes"))
unEuros=int(input("dime cuantas monedas de un euros tienes"))
cincuenta=int(input("dime cuantas monedas de 50 centimos tienes "))
vente=int(input("dime cuantas monedas de 20 centimos tienes"))
diez=int(input("dime cuantas monedas de 10 centimos tienes"))
Total= (dosEuros*200)+(unEuros*100)+(cincuenta*50)+(vente*20)+(diez*10)
eurosTotal=Total//100
centimosTotal=eurosTotal%100
print("Tienes %s euros y %s centimos"% (eurosTotal,centimosTotal))


"""9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
base=int(input("Dime una base"))
exponente=int(input("Dime un exponente"))
potencia=base**exponente
if exponente>0:
    print(base**exponente)
elif exponente==0:                        
    print("El resultado es 1")
else:
    print((1/potencia)*-1)


"""
10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.

"""
A=5
B=5
C=10
if (A**2+B**2)*0.5==C:
    print("es un triangulo rectangulo")
if A==B and A==C and B==C:
    print("es un triangulo equilatero")
if A==B or A==C or B==C:
    print("es un triangulo isoleles")
else:
    print("es un triangulo escaleno")
    


"""
11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400.
"""
año=int(input("dime el numero de dais que tiene tu año"))
if año%4==0 and año%100==0 and año%400==0:
    print("Es un año biciesto")
elif  año%4==0 and año%100!=0:
    print("Es un año biciesto")
else:
    print("No es un año biciesto") 


"""12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
"""
A=
B=




"""
13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje."""
"""
"""
alumno=int(input("¿Cuantos alumnos va a ir?"))

if alumno>=100:
    print("Cada alunmo debe pagar 65 euros ")
elif alumno<=99 and alumno>=50:
    print("Cada alumno debe pagar 70 euros")
elif alumno<=49 and alumno>=30:
    print("Cada alumno debe de pagar 95 euros")
    
if alumno>=100:
    print(alumno*65)
    pago_total=alumno*65
    if pago_total>=4000:
        print("Si se realiza el viaje")
    else:
        print("No se realizara el viaje")
elif alumno<=99 and alumno>=50:      #terminar
    print(alumno*70)
    pago_total=alumno*70
    if pago_total>=4000:
        print("Si se realiza el viaje")
    else:
        print("No se realizara el viaje")
elif alumno<=49 and alumno>=30:
    print(alumno*95)
    pago_total=alumno*95
    if pago_total>=4000:
        print("Si se realiza el viaje")
    else:
        print("No se realizara el viaje")

"""
14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
"""

    



"""15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error."""


"""16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente"""



"""17. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""
numero1=int(input("dime un numero"))
numero2=int(input("dime otro numero"))
for i in range(numero1,numero2,2):
    print(i)






"""18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo."""

pago=10
i=2
print(f" tiene que pagar en el mes 1,  {pago} euros")
for i in range (2, 21 ):
    print(f" tiene que pagar en el mes {i},  {pago*2} euros")
    pago*=2

print(f" el total es {pago*2-10} euros")
    







"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""


"""20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
"""
pago=10
for i in range (1, ,numero):
    print(pago*i)
    i=pago





"""
21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
números primos que queremos mostrar"""






















