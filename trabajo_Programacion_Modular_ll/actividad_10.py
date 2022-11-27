def darNumero(number, number2):
    divisors=0
    sonAmigos=False
    for i in range(1, number):
        if number%i==0:
            divisors+=i
    
    if divisors==number2:
        sonAmigos=True 
        
    return sonAmigos    
    
print(darNumero(220,284))
print(darNumero(1184, 1210))
print(darNumero(300,356))