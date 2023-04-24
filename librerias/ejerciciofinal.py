import math
print(math.pi)
print(math.cos(math.pi/4))

import random
cursos=["PYTHON","JAVA","NET"]
print(random.choice(cursos))
print(random.random())
print(random.randrange(1000))

import statistics
datos = [2.90,10.5,5,14,7,23.7]
#Hallando la media Aritmetica
statistics.mean(datos)
#Hallando e valor medio
statistics.median(datos)
#Hallando la moda
statistics.mode(datos)
#Hallando la variance
statistics.variance(datos)

#Trabajar con fechas
from datetime import date
hoy = date.today()
print(hoy)




