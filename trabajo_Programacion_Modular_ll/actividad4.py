"""Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
You can use the following algorithm to get a number between 0 (Sunday) and 6
(Saturday) corresponding to the day in the week for a given date:
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7

Diseñe un método llamado getDayOfWeek que reciba una lista que contenga tres enteros
(día, mes y año) y devuelve el día de la semana para esa fecha (lunes,
Martes Miércoles Jueves Viernes Sábado Domingo).

Puede usar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha dada:
a = (14 - mes) / 12
y = año – un
m = mes + 12 * a – 2
d = (día + y + y/4 - y/100 + y/400 + (31*m)/12) módulo 7

"""
def getDayOfWeek(dia, mes, año):
    a=(14-mes)//12
    
    y=año-a
    
    m=mes+12*a-2
    
    return(int(dia+y+y//4-y//100+y//400+(31*m)//12)%7)

nombreDias=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dia=1
while dia>0:
    dia=int(input("Enter a number of day: "))
    mes=int(input("Enter a number of month: "))
    año=int(input("Enter a number of year: "))
    if dia>0:
        text=nombreDias[getDayOfWeek(dia, mes, año)]
        
    else:
        text: "ERROR!"
        
    print("\n",text,"\n")    