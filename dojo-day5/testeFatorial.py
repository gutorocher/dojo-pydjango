
import unittest
from Fatorial  import CalculaFatorial

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.v1 = CalculaFatorial(3)

    def test_obj(self):
        ''' testa se existe o objeto v1 '''
        self.assertTrue(self.v1)

    def teste_fat_v1(self):
        ''' teste se o objeto r calcula fatorial'''
        self.assertEqual(self.v1.fatorial(), 6)

if __name__ == '__main__':
    unittest.main()
