'''Los graduandos de la facultad de ingeniería, desean elaborar un programa que determine el estatus de
cada uno de ellos, para cada estudiante se registro en un archivo de nombre graduandos.txt
la siguiente información:
Nombre del estudiante, Edad y su Promedio Académico
Procese la información anterior y determine e imprima por consola para N graduandos:
Para cada estudiante:
1. Su estatus.
Para todos los estudiantes:
2. Promedio académico de los estudiantes de estatus Excelente.
3. Porcentaje de alumnos cuyo promedio académico está entre 17 y 19 puntos.
4. Nombre del primer y del último estudiante con estatus diferente a Bueno.
Consideraciones: Para el estatus usaremos la siguiente tabla:
Promedio entre - Estatus
09.50 y 13.40 Regular
13.50 y 16.60 Bueno
16.50 y 18.40 Muy Bueno
18.50 y 20.00 Excelente

Variables de entrada
nombre as string
edad as integer
prom as single

Variables de proceso
acum1 as single
cont1 as integer
cont2 as integer
band as integer


Variables de salida
porcentaje as single
prom_exc as single
primer_n as string
ultimo_n as string
'''

arch = open('graduandos.txt','r')

#Inicializacion
acum1 = 0
cont1 = 0
cont2 = 0
band = 0

n = int(arch.readline())

for registro in arch:
    lista = registro.split(',')
    
    nombre = lista[0]
    edad = int(lista[1])
    prom = float(lista[2])
    
    if 9.5 <= prom <= 13.4:
        print('%s, estatus: Regular' %(nombre))
    elif 13.5 <= prom <= 16.6:
        print('%s, estatus: Bueno' %(nombre))            
    elif 16.5 <= prom <= 18.4:
        print('%s, estatus: Muy bueno' %(nombre))
    elif 18.5 <= prom <= 20:
        print('%s, estatus: Excelente' %(nombre))
        acum1 += prom
        cont1 += 1 
    else:
        print('')
        
        
    if 17 <= prom <= 19:
        cont2 += 1
    
    if not(13.5 <= prom <= 16.6) and band == 0:
        primer_n = nombre
        band = 1
    elif not(13.5 <= prom <= 16.6):
        ultimo_n = nombre
        
    
if cont1 != 0:
    prom_exc = acum1 / cont1
    print('El promedio académico de los estudiantes de estatus Excelente es de %.2f' %prom_exc)
else:
    print('Ningun estudiante posee el estatus excelente')

if cont2 != 0:
    porcentaje = cont2 / n *100
    print('El porcentaje de alumnos cuyo promedio académico está entre 17 y 19 puntos es de %.2f' %porcentaje, '%')
else:
    print('Ningun estudiante posee un promedio entre 17 y 19 puntos')

if band != 0:
    print('El primer y el último estudiante con estatus diferente a Bueno, fueron: %s y %s ' %(primer_n,ultimo_n))
else:
    print('Todos los estudiantes se encuestran en el estatus de promedio: Bueno')
    
arch.close()
