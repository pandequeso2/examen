import random,time,msvcrt,os

sueldos=[]

trabajadores=['Juan Pérez','Maria García','Carlos lópez','Ana Martínez','Pedro Rodrígez','Laura Hernández','Miguel Sámchez','Isabel Gómez','Fransico Díaz','Elena Fernández']
#Funciones principales: 
def asignar_sueldo():
    print('Asignar sueldos: ')
    sueldo_trabajador = 0
    for x in range(1,11):
       while True:
            os.system('cls')
            sueldo_azar=random.randint(300000,2500000)
            sueldo_trabajador=sueldo_azar
            print(f'trabajador: {trabajadores[x-1]} y su usueldo es de: ${sueldo_trabajador}')
            print('Presione una tecla para continuar...')
            sueldo=[sueldo_trabajador]
            sueldos.append(sueldo)
            sueldo_trabajador=0
            msvcrt.getch()
            os.system('cls')
            break    
    time.sleep(1)
def clasificar_sueldo():
    print('Clasificar sueldo:')
    

def ver_estadisticas():
    print('Ver estadisticas')
    pass
    print('Sueldo mas bajo: 4$',)
def reporte_sueldo():
    pass
def salir():
    print('Finalizando programa...')
    print('Desarrollado por: Benjamín Araya')
    print('Rut: 21.997.376-4')
    exit()

    