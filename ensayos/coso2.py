# COSO 2
# ............................................


tipo_num=int(input("Introduce num: "))

if tipo_num<0:
    print("menor")

elif tipo_num>0:
    print("mayor")

else:
    print("igual")


v2 = 'coso'

if (type(v1) == type(v2)):
    print('son del mismo tipo')
else:
    print('no son del mismo tipo')



j = 4

if (j % 2 == 0):
    print(es par)
else:
    print(impar)




j = 5

if (j % 2 == 0):
    print('es par')
else:
    print('impar')




for var in range(1, 21):
    if var % 2 == 0:
        print('El número', str(var), 'es par')
    else:
        print('El número', str(var), 'es impar')




for i in range(0, 6):
    print(i ** 3)


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



x = '-9'
fact = 1
if(type(x) == int):
    if(x > 0):
        orig = x
        while(x > 1):
            fact = fact * x
            x-= 1
        print('El factorial de ', orig, 'es', fact)
    else:
        print('Debe ser mayor a cero')
else:
    print('Debe ser entero')




n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))







# ............................................
# COSO ALMACEN







































