'''
Diseñe una función llamada palíndromo que tenga una cadena de caracteres como parámetro de entrada,
y devuelve True si es un palíndromo o False en otros casos. Una palabra es un palíndromo si
se puede leer igual de izquierda a derecha o de derecha a izquierda, ignorando los blancos. Por ejemplo:
"anilina" o "Dabale arroz a la zorra el abad" Para simplificar el problema, se puede suponer
que se utilicen caracteres simples, es decir, sin tildes ni diresis.
'''
def palindromo(cadena):
    letra=""
    letra2=""
    a=0
    for i in (cadena):
        a+=1
        letra+=i
        letra2+=(cadena[-a])
    
    return (letra,(letra2))

print(palindromo("hola"))
if letra == letra2:
    




