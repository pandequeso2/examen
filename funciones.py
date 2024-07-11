import random,time,msvcrt,os

sueldos=[]

trabajadores=['Juan Pérez','Maria García','Carlos lópez','Ana Martínez','Pedro Rodrígez','Laura Hernández','Miguel Sámchez','Isabel Gómez','Fransico Díaz','Elena Fernández']
#Funciones principales: 
def asignar_sueldo():
    sueldo_trabajador = 0
    for x in range(1,11):
       while True:
            os.system('cls')
            print('Asignar sueldo.')
            sueldo_azar=random.randint(300000,2500000)
            sueldo_trabajador=sueldo_azar
            print(f'Trabajador: {trabajadores[x-1]} y su usueldo es de: ${sueldo_trabajador}')
            print('Presione una tecla para continuar...')
            sueldo=[sueldo_trabajador]
            sueldos.append(sueldo)
            sueldo_trabajador=0
            msvcrt.getch()
            os.system('cls')
            break    
    time.sleep(1)
def clasificar_sueldo():
    if not sueldos:
        print('Error, la lista esta vacia...')
    else:
        total_sueldo=0
        print('Clasificar trabajadores: ')
        for x in range(1,11):
            for t in trabajadores:
                for s in sueldos[x-1]:
                    if s < 800000:
                        print(f'{t} Gana: ${s}')
                    elif s >=800000 and s <=2000000:
                        print(f'{t} Gana: ${s}')
                    elif s > 2000000:
                        print(f'{t} Gana: ${s}')
                    time.sleep(1)
            break
    total_sueldo+=s
    print('El total es: $',total_sueldo)
    total_sueldo=0                
def ver_estadisticas():
    if not sueldos:
        print('Lista vacia...')
    else:
        print('Ver estadisticas')
        sueldo_bajo=0
        sueldo_alto=0
        for x in range(1,11):
            for t in trabajadores:
                for s in sueldos:
                    s1=s[x-1]
                    s2=s[x]
                    prom=(s1+s2)/2
            
def reporte_sueldo():
    if not sueldos:
        print('Los trabajadores no tienen sueldo...')
    else:
        print('reporte de sueldo. ')
        for x in range(1,11):
            for t in trabajadores[x-1]:
                for s in sueldos[x-1]:
                    desc_salud=s *0.07
                    desc_afp=s*0.12
                    sueldo_liq=s-desc_salud-desc_afp
                    with open('sueldo.txt','w')as archivo:
                        pass


def salir():
    print('Finalizando programa...')
    print('Desarrollado por: Benjamín Araya')
    print('Rut: 21.997.376-4')
    exit()

    