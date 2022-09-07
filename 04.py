
# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

lis = ['Buenos Aires','Brasilia','Asunción','Montevideo','Santiago','Lima','Caracas','Bogotá']
print(lis[1:4])
print(lis)




# 2) Imprimir por pantalla el segundo elemento de la lista

print(lis[1])

lis[1]
# Brasilia

lis[3]
# Montevideo




# 3) Imprimir por pantalla del segundo al cuarto elemento

print(lis[1:4])

lis[3:6]
Montevideo, Santiago, Lima

type(lis[3:6])
list




# 4) Visualizar el tipo de dato de la lista

print(type(lis))
<class 'list'>




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(lis[2:]) # desde el tecero al último
Asunción, Montevideo, Santiago, Lima, Caracas, Bogotá




# 6) Visualizar los primeros 4 elementos de la lista

print(lis[:4]) # desde el primero hasta el quinto
# 'Buenos Aires','Brasilia','Asunción','Montevideo','Santiago'




# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

lis.append('Ciudad de Méjico')
# elemento nuevo

lis.append('Montevideo')
# elemento repetido
'''python no audita los elementos de una lista, etsos pueden estar repetidos,
ser de distintas clases, incluir listas dentro de listas, tuplas dentro de listas, diccionarios dentro de listas,
listas dentro de tuplas, listas dentro de diccionarios, etc.
'''

lis.append('Montevideo')

print(lis)




# 8) Agregar otra ciudad, pero en la cuarta posición

lis.insert(3, 'Quito')

print(lis)




# 9) Concatenar otra lista a la ya creada

lis1 = ['manzana', 'pera', 'naranja']
lis2 = ['melon', 'kiwi', 'sandía']

lis1.extend(lis2)
# ['manzana', 'pera', 'naranja', 'melon', 'kiwi', 'sandía']

#¡Ojo! no confundir "concatenar" con "Adjuntar" (append) pues esta última propiedad agrega
#
# la segunda lista como un elemento mas.

lis1.append(lis2)
# ['manzana', 'pera', 'naranja', ['melon', 'kiwi', 'sandía']]

lis1[3]
# ['melon', 'kiwi', 'sandía']]

lis1[3][1]
# 'kiwi'

lis1.sort()
print(lis1)
# ['kiwi', 'manzana', 'melon', 'naranja', 'pera', 'sandía']

lis1 = ['1',9,7,'3']

lis1[0] = int (lis1[0])

lis1[3] = int (lis1[3])

lis1
#[1,3,7,9]


lis2 = ['Madrid','Roma','Bruselas']
lis.extend(lis2)
print(lis)

lis.extend(['Madrid','Roma','Bruselas'])
print(lis)
# ['Buenos Aires', 'Brasilia', 'Asunción', 'Quito', 'Montevideo', 'Santiago', 'Lima', 'Caracas', 'Bogotá', 'Ciudad de Méjico', 'Montevideo', 'Madrid', 'Roma', 'Bruselas']



lis1 = ['1', 9, 7, '3']

lis1[0] =int(lis1[3])

lis1.sort()




# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(lis.index('Montevideo'))




# 11) ¿Qué pasa si se busca un elemento que no existe?

'París' in lis
# False
# Consulta de existencia


# con if no falla
if ('París' in lis):
    print(lis.index('París'))


print(lis.index('París'))




# 12) Eliminar un elemento de la lista

lis.remove('Buenos Aires')

lis.remove('París') # falla porque no existe


print(lis)




# 13) ¿Qué pasa si el elemento a eliminar no existe?

lis.sort(reverse=True)
# Ordena alfabéticamente de reversa
lis # da la lista de z-a

# "remove" quita cualquier elemento de la lista especificado y no retiene el valor
lis.remove('Buenos Aires')

# 14) Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo

# "pop" quita el último elemento de la lista, retiene el valor y puede ser utilizado
ultimo = lis.pop()
print(ultimo)
# imprimirá el elemento recién eliminado




# 15) Mostrar la lista multiplicada por 4

print(lis * 4) # concatena la misma lista por cuatro, todo dentro de una misma lista




# 16) Crear una tupla que contenga los números enteros del 1 al 20

tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(type(tup))
print(tup)
# <calss 'tuple'>
# (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for i in range(1,21):
    print(i)
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''

list(range(1,21)) # crear una lista de números enteros del 1 al 20

tup = tuple(range(1,21)) # crear una tupla de números enteros del 1 al 20




# 17) Imprimir desde el índice 10 al 15 de la tupla

a = '101'

b = 'hola'

# python siempre sobreescribe la variable pase lo que pase salvo que se tuple
b = ['algo', 'algo', 'algo']

 # para acceder a la consulta de indices de una tupla debe hacerse siempre con corchetes ya que este es el método de consulta de índices.
tupla[18:]
# (19, 20)


print(tup[10:16]) # minimo incluye, máximo excluye (10 al 15)
# (11, 12, 13, 14, 15, 16)




# 18) Evaluar si los números 20 y 30 están dentro de la tupla

print(20 in tup)
print(30 in tup)
# True
# False




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

not('Quito' in lis)


elemento = 'París'
if (not(elemento in lis)):
    lis.append(elemento)
    print('Se insertó el elemento', elemento)
else:
    print('El elemento', elemento, 'ya existía')
# El elemento París ya existía




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

lis.count('Montevideo')
# 2


print(tup.count(10))
print(lis.count('Montevideo'))




# 21) Convertir la tupla en una lista

lis2=list(tup)
print(lis2)




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

v1, v2, v3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = tup
print(v1)
print(v2)
print(v3)

v1
# 1

v2
# 2

v3
# 3
# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

dicc = {  'Ciudad': lis,
'País': ['Brasil','Paraguay','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España','Italia','Francia'],
'Continente' : ['América','América','América','América','América','América','América','América','América','América','Europa','Europa','Europa']}

print(dicc)




# 24) Imprimir las claves del diccionario

print(dicc.keys())




# 25) Imprimir las ciudades a través de su clave

print(dicc['Ciudad'])








# Iteradores e iterables

# Si tenemos un alista con varios valores, y queremos reccorrerla, podríamos resolverlo de la siguiente manera:

lista = [5, 3, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
'''
5
4
9
2
'''


Sin embargo, contamos con una forma sencilla de resolverlo:

lista = [5, 3, 9, 2]
for elemento in lista:
    print(elemento)
'''
5
4
9
2
'''


cadena = "Hola"
for c in cadena:
    print(c)
'''
H
o
l
a
'''

Algunas funcionalidades que podemos usar sobre elemento iterables:


* sum()
* join()
* list()

print(list("Hola"))
# ['H', 'o', 'l', 'a']

print(sum([1, 2, 3]))
# 6

print("-".join("Hola"))
# H-o-l-a


# Iteración sobre un diccionario:

mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)
'''
a
b
c
'''

# Un libro tiene diferentes páginas a las queUn libro tiene diferentes páginas a las que podemos acceder. Este libro podría ser una lista, y cada página un elemento de la lista. Por otro lado, el iterador sería un marcapáginas, es decir, una referencia que nos indica en qué posición estamos del libro, y que puede ser usado para "navergar" por él.

# Se trata de un objeto que podemos usar para navegar a travéz del libro. Usando la función next() sobre el iterador, podemos ir accediendo secuencialmente a cada elemento de nuestra lista(las páginas del libro).

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
print(next(marcapaginas))
# página1

# Dadas dos listas, digamos lista1 y lista2, al pasarlas a zip como entrada, el elemento 1 de lista1 se asocia con el elemento 1 de lista2, el elemento 2 de lista1 se asocia con el elemento 2 de lista2, el elemento 3 de lista1 se asocia con el elemento 3 de lista2, y así sucesivamente. Es decir que el resultado será una tupla donde cada elemento tendrá todos y cada uno de los elementos i-ésimos de las listas pasadas como entrada.

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)
type(c)
zip
list(c)
[(1, 'Uno'), (2, 'Dos')]


































