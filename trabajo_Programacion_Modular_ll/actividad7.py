def esPrimo(numero):
    es_primo=True
    if numero>0:
        for i in range(2, numero):
            if numero%i==0:
                es_primo=False
    else:
        es_primo=None
        
    return f"{es_primo}"

print(esPrimo(-9))
print(esPrimo(7))
print(esPrimo(3))