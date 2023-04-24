total_plato = int(input("Total A Pagar:...?"))
personas=int(input("¿Entre Cuantas personas se dividira la cuenta..?"))
propina=int(input('Porcentaje de propina(Digite un Numero)..?'))
impuesto=0.19
porc_propina=propina/100

total_cuenta = print(f'''{'*'*30}
El Total de la cuenta es:
Plato:\t\t $total_plato
Impuesto:\t {impuesto*100} % (${impuesto*total_plato})
Propina:\t {propina} % (${porc_propina*total_plato})
Total a Pagar:\t $ {total_plato+impuesto+total_plato+porc_propina*total_plato}

Dividido en:\t\t {personas} personas
Total Por Persona:\t ${round(((total_plato+impuesto+porc_propina)/personas),2
)}
{'*'*30}
''')

