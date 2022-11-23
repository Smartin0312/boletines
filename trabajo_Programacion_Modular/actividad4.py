'''
Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
'''
numero=6

lista=[]

while numero>0:
    num=int(input("Introduce numero: "))
    lista.append(numero)

def numMayor (lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def numerosPares (lista):
    pares=[]
    for i in range(len(lista)):
        if lista[i]%2==0 and lista[i]>0:
            pares.append(lista[i])
    return pares
print(f"De la lista{lista}; estos numeros {numerosPares(lista)} son pares y {numMayor(lista)} es el numero mayor")
