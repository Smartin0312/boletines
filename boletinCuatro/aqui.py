pago=10
i=2
print(f" tiene que pagar en el mes 1,  {pago} euros")
for i in range (2, 21 ):
    print(f" tiene que pagar en el mes {i},  {pago*2} euros")
    pago*=2

print(f" el total es {pago*2-10} euros")
    