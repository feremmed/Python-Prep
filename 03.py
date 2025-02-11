
# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

a = 10
if (a < 0):
    print('La variable es menor a cero')
elif (a > 0):
    print('La varaible es mayor a cero')
else:
    print('La variable es igual a cero')




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

a = 2
b = 'hola'
if (type(a) == type(b)):
    print('Las variables son del mismo tipo de dato')
else:
    print('Las variables son de tipos de dato diferentes')




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

a = 8
if(a % 2 == 0):
    print(a, 'es un número par')
else:
    print(a, 'es un número impar')



for i in range(1, 21):
    if i % 2 == 0:
        print('El número ', str(i), ' es par')
    else:
        print('El número ', str(i), ' es impar')

# del(a) borra el espacio de memoria en 'a'




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0, 6):
    print('Valor:', str(i), ' Elevado a la 3ra potencia:', str(i**3))
'''
Valor 0 Elevado a la 3ra potencia: 0
Valor 1 Elevado a la 3ra potencia: 1
Valor 2 Elevado a la 3ra potencia: 8
Valor 3 Elevado a la 3ra potencia: 27
Valor 4 Elevado a la 3ra potencia: 64
Valor 5 Elevado a la 3ra potencia: 125
'''




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

n = 12
for i in range(0, n):
    pass
print(i)


n = 12
for i in range(0, n):
    print(i + 1)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

factorial = 1
if (type(a) == int):
    if (a > 0):
        while(a > 1):
            factorial = factorial * a
            a-=1
    else:
        print('La variable debe ser mayor a cero')
else:
    print('La variable debe ser un número entero')



factorial = 1
if (type(a) == int):
    if (a > 0):
        a_original = a
        while(a > 1):
            factorial = factorial * a
            a-=1
        print('El factorial de ', a_original, 'es', factorial)
    else:
        print('La variable debe ser mayor a cero')
else:
    print('La variable debe ser un número entero')




a = 'hola'
if ((type(a) > == int) and (a > 0)):
    pass
else:
    print('La variable debe ser un número entero y mayor a cero')



n = 5
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n > 2):
            n = n - 1
            factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')
# Resuelto
# El factorial es 120

a = 8
if (a > 0):
    pass
else:
    print('La variable debe ser mayor a cero')
# nada porque True y pass

a = -2
if (a > 0):
    pass
else:
    print('La variable debe ser mayor a cero')
# La variable debe ser mayor a cero


a = '-2'
if (a > 0):
    pass
else:
    print('La variable debe ser mayor a cero')
# TypeError porque str


a = -2
if (type(a) == int):
    if (a > 0):
        pass
    else:
       print('La variable debe ser mayor a cero')
else:
    print('La variable debe ser un número entero')
# No falla porque ahora valida int vs str
#'La variable debe ser mayor a cero'



a = '-2'
if (a > 0):
    print(1)
else:
    print(2)
# Error porque str

# agregando {and} deberán cumplirse ambas condiciones

if ((a > 0) and (type(a) == int)):
    pass
else:
    print('La variable debe ser un número entero y mayor a cero')
# Error porque pregunta mayor que antes que el tipo de dato


if ((type(a) == int) and (a > 0)):
    pass
else:
    print('La variable debe ser un número entero y mayor a cero')
# No error porque pregunta tipo antes que mayor que

### Osea que; dependiendo del orden de consulta, fallará o no.




# 7) Crear un ciclo for dentro de un ciclo while

n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))




# 8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
    print('Ciclo while nro ' + str(n))
    print('Ciclo for nro ' + str(i))




# 9) Imprimir los números primos existentes entre 0 y 30

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))



ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

tope_rango=100
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))



ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')




# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1




# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1

