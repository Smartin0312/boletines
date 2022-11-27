""" Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1.

Diseñe un método llamado computeDaysInMonth que devuelva el número de días para
el mes y el año que se reciben como argumentos. Puede utilizar el método
año bisiesto anterior. Si los valores no son válidos, el método debería devolver -1.

"""
nombreMes=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def isLeapYear(yyyy):
    return yyyy%4==0 and (yyyy%100!=0 or yyyy%400==0)


def computeDaysInMonth(mm, yyyy):
    diaDelMes=31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    if mm==2 and isLeapYear(yyyy):
        diaDelMes=29
            
    else:
        diaDelMes=diaDelMes[mm-1]
        
    return diaDelMes

mes=1
while mes>0:
    mes=int(input("Enter a month(mm): "))
    
    año=int(input("Enter a year(yyyy): "))

    if mes<=0 or año<=0:
        mensaje=-1
    else:
        mensaje=f"the nombreMes{[mes-1]} of {año}, have a {computeDaysInMonth(mes,año)} days"
        
    print(mensaje)
    print(" ")
