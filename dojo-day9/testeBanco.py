import unittest

from banco  import Banco

class TestClass(unittest.TestCase):
    
    def setUp(self):
        self.p = Banco(300)
        self.p1 = Banco(350)

    def test_obj(self):
        self.assertTrue(self.p)
        self.assertTrue(self.p1)

    def teste_saque_trezentos(self):
        self.assertEqual(self.p.saque(),[3,0,0,0,0])

    def teste_saque_quebradi(self):
        self.assertEqual(self.p1.saque(),[3,1,0,0,0])

if __name__ == '__main__':
    unittest.main()

