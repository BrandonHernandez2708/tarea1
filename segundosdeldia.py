#convertir horas a segundos y minutos a segundos en formato 24 horas
haseg=3600
minaseg=60
hora=int(input("ingrese la hora que tiene (en formato 24 horas): "))
minutos=int(input("ingrse los minutos: "))
segundos=(haseg*hora)+(minutos*minaseg)
print("los segundos que han transcurrido en el dia son:  ",segundos)
