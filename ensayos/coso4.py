# C O S O   4
# ---------------------


lista = []

for elemento in range(-15,0):

    lista.append(elemento)
print(lista)



print(lista[0] % 2)


i = 0
while(i < len(lista)):
    if (lista[i] % 2 == 0):
        print('el numero ', lista[i], 'es par')
    i += 1





for i, e in enumerate(lista):
    print(i, e)


for elemento in lista[:3]:
    print(elemento)


n = 0
while(n < len(lista)):
    if (lista[n] % 2 == 0):
        print(lista[n])
        lista[n] = str(lista[n])
    n += 1


print(lista)

# 6


lis = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]


aux = 1
while (aux <= 20):
    if (not(aux in lis)):
        #list.append(aux)
        # con la de arriba (append) quedan los faltantes al final de la lista
        # con la de abajo queda toda la lista ordenada
        lis.insert((aux - 1), aux)
    aux += 1



print(lis)

# another way


lisa = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]
for aux in range(1,21):
    if(not(aux in lisa)):
        lisa.insert((aux - 1), aux)

print(lisa)


# 7


fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n+= 1
print(fibo)



# print(sum(fibo))


n = 2
while(n < len(fibo)):
    print(fibo[n]/fibo[n-1])
    n += 1



dic = {'ciud' : ['buai', 'cara', 'bogo', 'lisb', 'roma'],
       'pais' : ['arge', 'vene', 'colo', 'port', 'ital'],
       'cont' : ['amer', 'amer', 'amer', 'euro', 'euro']}


print(dic)

print(dic.keys())

dic['ciud'].append('coso')


print(dic)

dic['pobl'] = [5,5,5,5,5,5]


print(dic)

del dic['pobl']

print(dic)



cad = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python. '
print(type(cad))

cad = list(cad)
print(type(cad))

print(cad)


rec = iter(cad)
lar = len(cad)
for i in range(0, lar):
    print(next(rec))

print('---------------- coso ----------------')

reco = iter(cad)

print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))
print(next(reco))

print(len(cad))


lis1 = ['run', 'fly', 'sleep']
lis2 = ['correr', 'volar', 'dormir']

lisz = zip(lis1, lis2)
print(type(lisz))
print(list(lisz))

lisz = list(lisz)

print(type([0]))


lis = [18, 21, 29, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
lis2 = [i for i in lis if i % 7 == 0]
print(lis2)



liso = [[1,2,3,4], 'rojo', 'verde', [True, False, False], ['uno', 'dos', 'tres']]

print(liso)



























