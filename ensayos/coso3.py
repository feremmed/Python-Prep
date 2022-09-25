# C O S O   3
# ---------------------

lis = ['ba', 'br', 'as', 'mo', 'sa', 'li']


lis.append('cm')

lis.append('mo')

lis.insert(3, 'Qo')

lis.extend(['ma', 'ro', 'be'])


print(lis)



lis1 = ['a', 'b', 'c']
lis2 = ['d', 'e', 'f']

lis1.extend(['d', 'e', 'f'])

print(lis1)



print(lis.index('mo'))

print(lis.index('ba'))

print('co' in lis)


print(lis.pop())
lis.remove('ma')
print(lis)


frase = 'Buen día '
print(frase * 4)

print(lis * 4)

lis_repe = lis * 4

lis_repe.sort()


print(lis_repe)

# armar contador de repes

tup = (1, 2, 3, 4, 5, 6, 7, 8)

for i in range(1,21):
    print(i)

# tup = tuple(range(1,21))

list(range(1,21))

print(tup[1:6])


a = '101'
b = 101

b = 'hola'


print(b)


print(2 in tup)
print(9 in tup)



print(tup[3])

print('qu' in lis)

elem = 'qu'
if (elem in lis):
    print('elem', elem, 'exist')
else:
    lis.append(elem)
    print('insert elem ', elem)

print(lis)

print(not(False))

print(lis.count('mo'))


lis2=list(tup)
print(lis2)


v1, v2, v3 = tup[:3]


print(v1, v2, v3)


tup2 = (v1, v2, v3)

print(tup2)

print('coso')



lis2 = 'br', 'pa', 'ec', 'ur', 'ch', 'pe', 've', 'co', 'me', 'ur', 'fr'
lis3 = 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'eu'



dicc = { 'ciud' : lis,
         'pais' : lis2,
         'cont' : lis3,
         'ejem' : [1,2,3,4]}


print(dicc)


print(dicc.keys())


print('lalala')


print(dicc['pais'])
type(dicc['pais'])


dicc['cont'].append('eu')
























































