'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

lista_nombres=["Salva","Santi","Sergio","Miguel","Negu","Marta"]
letra_nombre="A"


def filtroLetras(lista, letra):
    filtrado=[]
    for i in range(len(lista)):
        if lista[i][0]==letra:
            filtrado.append(lista[i])
    return filtrado


print (filtroLetras(lista_nombres, letra_nombre))

