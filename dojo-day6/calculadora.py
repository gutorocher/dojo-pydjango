# -*- coding: utf-8 -*- 

#Autor: Gustavo, Elber

#Caso:
# Implementar Classe objeto
#Implementar classe calculos
#todos os objetos informam seus valores

#PASSO 1 - implementar teste
#PASSO 2 - implementar funcionalidade
#PASSO 3 - Voltar o passo 1

import math
 
class Calculos(object):

    def __init__ (self,n1,n2):
        self.n1 = n1
        self.n2 = n2
       
    def soma (self):
        soma = self.n1 + self.n2 
        return soma

    def subtracao(self):
        subtracao = self.n1 - self.n2 
        return subtracao

    def multiplicacao(self):
        multiplicacao = self.n1 * self.n2 
        return multiplicacao

    def divisao(self):
        divisao = self.n1 / self.n2 
        return divisao

    def raizQuadrada(self):
        raiz = math.sqrt(self.n1)
        return raiz

    
if __name__ == '__main__':
    print " ============================"
    print "      CALCULOS BASICOS CALCULADORA "
    print " ============================"
    
    c = Calculos(5.0,6.0)

    print " Soma dos valores        : %s" %c.soma()
    print " Subtracao dos valores   : %s" %c.subtracao()
    print " Divisao dos valores     : %s" %c.divisao()
    print " Raiz Quadrada do valor  : %s" %c.raizQuadrada()
    print " ============================"