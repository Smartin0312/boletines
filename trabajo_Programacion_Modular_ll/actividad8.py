def darOrden(a, b, c):
    x=0
    y=0
    valid=[0,1,2,3,4,5,6,7,8,9]
    if (a not in valid) or (b not in valid) or (c not in valid) or (a <=0)or (b <=0)or (c <=0):
        x=None
        y=None  
    else:
        x1=(b**2)-(4*a*c)
        x3=x1**(1/2)
        x2=(b)+(x3)
        x=x2/(2*a)
        y1=(b**2)-(4*a*c)
        y3=y1**(1/2)
        y2=(b)-(y3)
        y=y2/(2*a)
    return x, y   
 
 

print(darOrden(1,3,2))
print(darOrden(2,45,15))
