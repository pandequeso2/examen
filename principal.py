import os, time
from funciones import *
while True:
    os.system('cls')
    print('Menu de opciones: ')
    print('1. Asignar sueldos aleatorios. ')
    print('2. Clasificar sueldos. ')
    print('3. Ver estadisticas. ')
    print('4. Reporte de sueldos. ')
    print('5. Salir.')
    opc=input('Ingrese una de las opciónes: ')
    os.system('cls')
    if opc=='1':
        asignar_sueldo()
    elif opc=='2':
        clasificar_sueldo()
    elif opc=='3':
        ver_estadisticas()
    elif opc=='4':
        reporte_sueldo()
    elif opc=='5':
        salir()
    else:
        print('ERROR, No esta dentro de las opciónes...')
    time.sleep(1)     