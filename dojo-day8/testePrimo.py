# -*- coding: utf-8 -*- 
#=======================================================
#Autor: Gustavo, Elber, Edgar, Vinicius, Jonas Cruz

#script de teste usando o unnit teste do python
#implementar teste da funcionalidade objeto
# implementar teste objeto fatores primo 10
# implementar teste objeto fatores primo 4
# implementar teste objeto fatores primo 5
# implementar teste objeto fatores primo 100
# implementar teste objeto fatores primo 198
# implementar teste objeto fatores primo 276
# qualquer nova implentação desenvolva o teste primeiro, 
#jamais esqueca disso
#=========================================================

''' carega a biblioteca unit de test'''
import unittest

''' carrega arquivo Primo e chama a classe numeroPrimo'''
from Primo import numeroPrimo

class TestClass(unittest.TestCase):

    def setUp(self):
    	''' configura a instancia '''
        self.p = numeroPrimo(10)
        self.p0 = numeroPrimo(4)
    	self.p1 = numeroPrimo(5)
    	self.p2 = numeroPrimo(100)
    	self.p3 = numeroPrimo(198)
    	self.p4 = numeroPrimo(276)

    def teste_obj(self):
    	''' testa se existem os objetos abaixo '''
        self.assertTrue(self.p)
        self.assertTrue(self.p0)
        self.assertTrue(self.p1)
        self.assertTrue(self.p2)
        self.assertTrue(self.p3)
        self.assertTrue(self.p4)


    def teste_divisao_dez(self):
    	''' testa os valores do primo 10 '''
        self.assertEqual(self.p.divisao_sucessiva(), [2,5])
    

    def teste_numero_quatro(self):
    	 ''' testa os valores do primo 04 '''
    	 self.assertEqual(self.p0.divisao_sucessiva(), [2,2])
    
    def teste_numero_cinco(self):
    	 ''' testa os valores do primo 05 '''
    	 self.assertEqual(self.p1.divisao_sucessiva(), [5])

    def teste_numero_cem(self):
        ''' testa os valores do primo 100 '''
        self.assertEqual(self.p2.divisao_sucessiva(), [2,2,5,5])

    def teste_numero_centro_noventa_oito(self):
        ''' testa os valores do primo 198 '''
    	self.assertEqual(self.p3.divisao_sucessiva(), [2,3,3,11])
    
    def teste_numero_duzendo_setenta_seis(self):
        ''' testa os valores do primo 276 '''
    	self.assertEqual(self.p4.divisao_sucessiva(), [2,2,3,23])


''' main para executar os testes desta classe'''
if __name__ == '__main__':
    unittest.main()