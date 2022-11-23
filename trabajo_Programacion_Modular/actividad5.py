'''
Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
'''
lista=["Di","buen","dia", "a", "papa"]
lista.reverse()
print(lista)
lista=["Di","buen","dia", "a", "papa"]

def listaAlreves(lista):
    cadena=" "
    for i in range (len(lista)):
        cadena+=lista[(i+1)*-1]+" "
    return cadena
print(listaAlreves(lista))
lista=["Di","buen","dia", "a", "papa"]

def listaAlreves(lista):
    listainversa=[]
    for i in range (len(lista)):
        listainversa.append(lista[(i+1)*(-1)])
    return listainversa

print(listaAlreves(lista))