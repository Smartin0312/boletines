def contar_vocales(palabra):
    n1=""
    n2=""
    for i in range(len(palabra)):
        if ("a" in palabra[i]) or ("e" in palabra[i])or ("i" in palabra[i])or ("o" in palabra[i])or ("u" in palabra[i]):
            n1+=palabra[i]
        if not( ("a" in palabra[i]) or ("e" in palabra[i])or ("i" in palabra[i])or ("o" in palabra[i])or ("u" in palabra[i])) and (" " not in palabra[i]):
            n2+=palabra[i]
    ordenada=n1+n2        
    
return ordenada

print(contar_vocales("hola mundo"))