# -*- coding: utf-8 -*- 

import unittest

from calculoArea import Calculos

class TesteClass(unittest.TestCase):

	def setUp(self):
		self.c =  Calculos(6.0,8.0,10.0,5.0)
		
	def test_obj(self):
		''' teste se objeto c '''
		self.assertTrue(self.c)
	
	def teste_areaQuadrado(self):
		''' teste area de area do quadrado'''
		self.assertEqual(self.c.areaQudrado(),48.0)
	

	def teste_areaTriangulo(self):
		''' teste area do triangulo '''
		self.assertEqual(self.c.areaTriangulo(),24.0)
	

	def teste_calculo_circulo(self):
		''' teste area circulo r =5 '''
		self.assertEqual(self.c.areaCirculo(),78.50)
    	    

    def teste_somaMaisLado(self):
        ''' teste de soma de mais lado'''
         self.assertEqual(self.c.somaMaisLado,24.0)
        


if __name__ == '__main__':
    unittest.main()
	
