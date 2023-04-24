import csv


def data_source_csv():
    with open('Libro1.csv','r') as data:
        csv_read = csv.reader(data)
        #Casteando de Objeto a Lista
        list_precios = list(csv_read)
        return list_precios

        
def indicador_producto_activo(data):
    #Seteando una Lista para almacenar los valores requeridos
    productos_activos=[]
    for codigo,producto,precio,stock,estado in data:
        if estado==1:
            #Añadiendo elementos a la nueva lista
            productos_activos.append((codigo,producto,precio,stock,estado))
    return productos_activos        
        
print(data_source_csv())
print(indicador_producto_activo(data_source_csv()))

#print(data_source_csv())

