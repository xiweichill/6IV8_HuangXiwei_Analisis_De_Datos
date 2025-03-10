import pandas as pd

##Escribir un programa que pregunte al usuario por la ventas de un rango de años y muestrelos datos en ventasindexadas pro lso años, antes u despues de aplicarles un descuento
inicio = int(input('Introduce el año de ventas inicial: '))
fin = int(input('Introduce el año final de ventas :'))

ventas = {}

for i in range(inicio,fin+1):
    ventas[i] = float(input('introduce las ventas del año ' + str(i) + ': '))

ventas = pd.Series(ventas)
print('Ventas \n ', ventas)
print('Ventas con descuento\n',ventas*0.9)


