'''
Diseñe una función llamada lowCaseInString que tenga como 
parámetro una cadena de caracteres, eldebe devolver cuántos 
de esos caracteres son mayusculas
'''


def lowCaseInString(string):
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    counter=0
    
    for i in range(len(string)):
        if string[i] in abc:
            counter+=1
    return counter

print(lowCaseInString("Hola Mundo Que Tal "))