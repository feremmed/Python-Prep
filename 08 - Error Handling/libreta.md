
import unittest

def suma(num_1, num_2):
    return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):

        def test_suma_dos_positivos(self):
            num_1 = 10
            num_2 = 5

            resultado = suma(num_1, num_2)

            self.assertEqual(resultado, 15)

        def test_suma_dos_negativos(self):
            num_1 = -10
            num_2 = -7

            resultado = suma(num_1, num_2)

            self.assertEqual(resultado, 3)


import os

os.listdir("./")

import os

lineas_archivo = ['Esto es un archivo de ejemplo','Segunda linea','Tercera linea']
archivo = open('datos.txt', 'w')
for linea in lineas_archivo:
    archivo.write(linea+'\n')
archivo.close()


