'''
Diseñe una función llamada numberInString que reciba una cadena de caracteres como
parámetro y devuelve cuántos de ellos son números.
'''
def lowCaseInString(number):
    num="0123456789"
    counter=0
    
    for i in range(len(number)):
        if number[i] in num:
            counter+=1
    return counter

print(lowCaseInString("hola1932314 3sper0 qu3 3st3s g3n1al"))