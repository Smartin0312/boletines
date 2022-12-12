
def contar_palabras(frase):
    contador=0
    espacio=0
    for i in range(len(frase)):
        if (" " in frase[i]):
            contador+=1
    for i in range(len(frase)-1):
        if (" " in frase[i]and " " in frase[i+1]):
           espacio+=1  
        if (" " in frase[-1]):
            contador-=1
        if " " in frase[0]:
            contador-=1
    return contador+1-(espacio)

print (contar_palabras("voy a aprobar programacion"))
