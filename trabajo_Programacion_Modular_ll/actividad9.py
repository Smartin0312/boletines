

def esPrimo(number):
    esPrimo=True
    
    for i in range(2, number):
        if number%i==0:
            esPrimo=False
   
        
    return esPrimo

def obtenerPrimosDivisores(number):
    divisors=[]
    count=0
    count2=1
    if number<0:
        divisors=None
    else:
        if esPrimo(number):
            divisors=[1, number]
        else:
            while count<=2:
                if esPrimo(count2) and number%count2==0:
                    divisors.append(count2)
                    count+=1
                count2+=1
        
    return divisors

print(obtenerPrimosDivisores(2))
print(obtenerPrimosDivisores(500))
print(obtenerPrimosDivisores(97))