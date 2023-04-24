from base_de_datos import empleados

#Realizar un indicador que me permita sumar el sueldo de toda un Area

def suma_sueldos_area(bd):
    existe=False
    suma=0
    try:
        area_buscar = input("Ingrese el Area a totalizar el Sueldo:")
        for item in bd:
            if area_buscar == item['area']:
                #Acumulando el sueldo de un Area especfica
                suma=suma+item['sueldo']
                existe=True
        if existe == False:
            print("El Area no Existe")        
        print(f'El Total de la Planilla del Area es {area_buscar} es {suma}')   
    except:
        print("Ha Ocurrido un Error")         


suma_sueldos_area(empleados)
