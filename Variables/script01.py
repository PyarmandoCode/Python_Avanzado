print("Python Avanzado")

# Tipo de datos Primitivas

eda_per=28  #int
nom_per="Juan Perez" #str
pre_prod=29.80 #float
est_prod=True #bool

#Type te devuelve el tipo de datos que almacena la variable
print(type(eda_per))
print(type(nom_per))
print(type(pre_prod))

est_prod="Cancelado"
print(type(est_prod))


#Colleciones

Listas_Personas=["juan","pedro","ramon",18,20.90,True,["Peras","Manzanas"]] #List
Empleados_Sis = {'codigo':'a100','nombre':'ramon'} #dic
datos_ips =('100.200.80.90','100.200.80.91','100.200.80.96') #tuplas inmutables
prec_prod = {'1200','1800','1560'} #sets ordenables


#Calcular el Area de un Circulo
radio = 10
area_of_circle= 3.14 * radio ** 2 #**Exponente
print('Area del Circulo',area_of_circle)
print('Area del Circulo' + str(area_of_circle))
print(f' El Area del Circulo  {area_of_circle}') #Dale Like

#Calcular el Total a Pagar por un Producto
#Funcion Input me permite ingresar valores por consola a las variables
pre_prod = float(input("Ingrese el Precio del Producto:"))
can_prod= int(input("Ingrese la Cantidad del Producto:"))
sub_tot = pre_prod*can_prod
imp= sub_tot * 0.18
neto_pag = sub_tot + imp
print(f'El Impuesto es  {imp} El Total a Pagar es {neto_pag}')


#Operadores Matematicos
print(2 + 2)
print(4 * 8)
# todo Division decimal
print(5 / 3)
# todo Division Entera
print(5 // 3)
# todo Residuo de la division
print(23 % 2)

#Operadores Logicos

# " >Mayor "
# "< Menor "
# " >= Mayor Igual "
# " <= Menor Igual
# " != Diferente "
# " == " Igual
# " And " y
# " OR "  o
# " NOT" negacion

#Conversiones de datos

# Conversion de tipo de datos
# De numerico a cadena
print(str(23))
# De Numerico a decimal
print(float(23))
# De Logico a Cadena
print(str(True))
# de String a Numerico
print(int('123'))
# de Numerico a Logico
print(bool(0))

#Concatenacion
#Comentarios en Varias Lineas DocStrings

""" %s  STRING
 %d  INTEGER
 %f  FLOAT """

mentor = "Armando"
curso = "Python"
edad = 43
salario = 1700
print ("%s tiene %d" %(mentor,edad))
print (mentor,"tiene",edad)
print(mentor + "tiene"+ str(edad))

#Formato a Decimales
precio = 2.57777777777777
print("El Nuevo valor del precio es %.5f" %precio)


#Separadores Tabuladores y saltos de Linea
print("hola","mundo",sep='<->')
print("hola",end="")
print("mundo")
print("Saltos de linea, Viene un salto \n\n")
print("\t tabulador \n\n")

#Palabras Reservadas 
import keyword
print(keyword.kwlist)