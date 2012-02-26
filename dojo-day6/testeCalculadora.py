#script de teste usando o unnit teste do python
#implementar teste da funcionalidade objeto
# implementar teste objeto calculadora
# implementar teste de calculos basicos
# implementar teste 
# qualquer nova implentacao desenvolva o teste primeiro...

import unittest
from calculadora import Calculos

class TesteClass(unittest.TestCase):
    
    def setUp(self):
        self.c = Calculos(2.0,3.0)
       
    def test_obj(self):
        ''' testa se existe o objeto c '''
        self.assertTrue(self.c)


    def teste_soma(self):
        ''' teste se o objeto c calcula a soma'''
        self.assertEqual(self.c.soma(), 5)
        
    def teste_subtracao(self):
        ''' teste se o objeto c calcula a subtracao'''
        self.assertEqual(self.c.subtracao(),-1)

    def teste_multiplicacao(self):
        ''' teste se o objeto c calcula a multiplicacao'''
        self.assertEqual(self.c.multiplicacao(),6)

    def teste_divisao(self):
        ''' teste se o objeto c calcula a divisao'''
        self.assertEqual(self.c.divisao(),0.66666666666666666666666666666667)

    def teste_raiz(self):
        ''' teste se o objeto c calcula a raiz Quadrada'''
        self.assertEqual(self.c.raizQuadrada(),1.4142135623730950488016887242097)


if __name__ == '__main__':
    unittest.main()
