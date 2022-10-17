"""
1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""


cateto_1=int(input("Dime el primer cateto"))
cateto_2=int(input("Dime el segundo cateto"))
suma=cateto_1+cateto_2
print(suma**0.5)





"""
2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""

valor=int(input("Dime un valor en grados Fahrenheit"))

print(valor-32)

    

"""
3. Calcular la media de tres números pedidos por teclado
"""

numero_uno=int(input("Dime un  numero"))
numero_dos=int(input("Dime otro  numero"))
numero_tres=int(input("Dime un tercer  numero"))

print((numero_uno+numero_dos+numero_tres) /3)



"""
4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea sabercuanto deberá pagar finalmente por su compra.
"""

total=int(input("¿Cual es el precio total?"))
print(total*15/100)







"""
5. Pide al usuario dos números y muestra la "distancia" entre ellos
 (el valor absoluto de sudiferencia, de modo que el resultado sea siempre positivo).
"""

numero_1=int(input("Dime el primer numero"))
numero_2=int(input("Dime el segundo numero"))   
diferencia=numero_1-numero_2
if diferencia>0:
    print("%s es la diferencia" %(diferencia))
elif diferencia<0 :
    print(diferencia *-1)("%s es la diferencia" %(diferencia))



 
   
        
    

"""
6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen
 dos puntos en el plano.Calcula y muestra la distancia entre ellos.
"""

x1=12
x2=34
y1=21
y2=65
distancia=((x1-x2)**2 + (y1-y2)**2)**0,5
print(f" La distancia es la {distancia}")




"""
7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su
raíz cúbica.Python no tiene ninguna función predefinida que permita calcular
la raíz cúbica, ¿cómo sepuede calcular?
"""

numero=int(input("Dime un numero"))
print(numero**0.5)                         
print(numero**0.25)







"""
8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos,
20 céntimos o 10 céntimos)
"""

moneda2e=int(input("Dime cuantas monedas de 2 euro tienes"))
moneda1e=int(input("Dime cuantas monedas de 1 euro tienes"))
moneda50cent=int(input("Dime cuantas monedas de 50 centimos tienes"))
moneda20cent=int(input("Dime cuantas monedas de 20 centimos tienes"))
moneda10cent=int(input("Dime cuantas monedas de 10 centimos tienes"))

total=moneda2e*200+moneda1e*100+moneda50cent*50+moneda20cent*20+moneda10cent*10
total_euros=total//100
total_centimos=total%100


print(f" tienes {total_euros} euros y {total_centimos} centimos ")








"""
9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
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
A=7
B=7
C=16
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




"""
12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

"""
tipo=(input("Dime el tipo de uva"))
tamaño=int(input("Dime el tamaño"))
precio_inicial=float(input("Dime el precio"))
if tipo=="a" and tamaño==1:
    print (precio_inicial+0.20)
elif tipo=="a" and tamaño==2:
    print(precio_inicial+0.30)
elif tipo=="b" and tamaño==1:
    print(precio_inicial-0.30)
elif tipo=="b" and tamaño==2:
    print(precio_inicial-0.50)
else:
    print("Error")
    






"""
13. El director de una escuela está organizando un viaje de estudios, y requiere
 determinarcuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes
 por elservicio. La forma de cobrar es la siguiente: si son 100
 alumnos o más, el costo por cadaalumno es de 65 euros; de 50 a 99 alumnos,
 el costo es de 70 euros, de 30 a 49, de 95 euros,y si son menos de 30, el
 costo de la renta del autobús es de 4000 euros, sin importar elnúmero de alumnos.
 Realice un algoritmo que permita determinar el pago a la compañía deautobuses y
 lo que debe pagar cada alumno por el viaje.
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
minutos=float(input("dime cuantos minutos de llamada has hecho"))
dia=input("que dia llamas")
horario=(input("¿en que franga horaria lo realizas ?"))
if minutos<=5 and horario=="mañana"and dia!="domingo":
    print(f"el impuesto es de { 1+(1*0.15) }")  
elif minutos<=5 and horario=="tarde"and dia!="domingo":
    print(f"el impuesto es de { 1+(1*0.10) }") 
elif minutos<=5 and dia=="domingo":
    print(f"el impuesto es de { 1+(1*0.03) }") 
elif minutos<=8 and minutos>6 and horario=="mañana"and dia!="domingo":
    print(f"el impuesto es de { 0.80+(0.80*0.15) }") 
elif minutos<=8  and minutos>6 and horario=="tarde"and dia!="domingo":
    print(f"el impuesto es de { 0.80+(0.80*0.15) }")
elif minutos<=8 and minutos>6 and dia=="domingo":
    print(f"el impuesto es de { 0.80+(0.80*0.03) }")    
elif minutos>=10 and horario=="mañana"and dia!="domingo":
    print(f"el impuesto es de { 0.50+(0.50*0.15) }")  
elif minutos>=10 and horario=="tarde"and dia!="domingo":
    print(f"el impuesto es de { 0.50+(0.50*0.10) }") 
elif minutos>=10  and dia=="domingo":
    print(f"el impuesto es de { 0.50+(1*0.03) }")    








"""
15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error.
"""

dia=int(input("Dime un dia de la semana(del 1 al 7)"))

if dia==1:
    print("Es lunes")
elif dia==2:
    print("Es martes")
elif dia==3:
    print("Es miercoles")
elif dia==4:
    print("Es jueves")
elif dia==5:
    print("Es viernes")
elif dia==6:
    print("Es sabado")
elif dia==7:
    print("Es domingo")
else:
    print("Error")




"""
16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente.
"""

numero=int(input("Dime un numero del 1 al 12"))

if numero==1:
    print("Tiene 31 dias")
elif numero==2:
    print("Tiene 28 dias")
elif numero==3:
    print("Tiene 31 dias")
elif numero==4:
    print("Tiene 30 dias")
elif numero==5:
    print("Tiene 31 dias")
elif numero==6:
    print("Tiene 30 dias")
elif numero==7:
    print("Tiene 31 dias")
elif numero==8:
    print("Tiene 31 dias")
elif numero==9:
    print("Tiene 30 dias")
elif numero==10:
    print("Tiene 31 dias")
elif numero==11:
    print("Tiene 30 dias")
elif numero==12:
    print("Tiene 31 dias")
else:
    print("Error")








