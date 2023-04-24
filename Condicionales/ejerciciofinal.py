#Resumen condicionales

precio = int(input("Ingrese el precio del Producto:"))
if precio>=200 and precio<=500:
    print("El Producto debe tener descuento")
elif precio>=600 and precio>=1000:    
    print("El Producto debe tener descuento")
elif precio>=1200 and precio>=1400:    
    print("El Producto debe tener descuento")
elif precio>=1450 and precio>=1900:    
    print("El Producto debe tener descuento")        
else:
    print("El Producto NO debe tener descuento")

#Resumen Bucles
#For -  While

Listas_Personas=["juan","pedro","ramon",18,20.90,True,["Peras","Manzanas"]] #List

for x in Listas_Personas:
    print(x)
    print("Estoy fuera de l bucle")    


for _ in range(10):
    print("Mensaje")

for x in range(2,10,2):
    if x == 5:
        #Salir del Bucle
        break
    print("Mensaje",x)


#While

contraseña="admin123"
cont=0
while True:
    con = input("Ingrese la Contraseña:")
    if con ==contraseña:
        print("Contraseña Correcta")
        break #True
    else:
        print("Contraseña erroenea")
        cont +=1
        if cont==3:
            print("Supero los intentos , vuelva en 24 horas")        
            break


    