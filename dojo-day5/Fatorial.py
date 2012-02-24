# _*_coding = utf-8 _*_
__author__ = 'gusrocha'
import math

class CalculaFatorial(object):

    def __init__ (self,valor):
        self.valor = valor


    def calculaFatorial(self,valor):

        """
        calcula o resultado do fatorial, pelo numero
        passado por paramentro
        """
        fatorial = math.factorial(valor)
        print fatorial

    
    def fatorial(self):

        fatorial = self.valor

        '''
        neste local e feito analise que sera
        percorrido quando estiver o valor maior que 1.
        '''

        while (self.valor >1):

            fatorial = fatorial*(self.valor-1)
            #efetuado decremento do valor como no calculo do fatorial
            self.valor=self.valor-1
            #imprime o valor do fatorial em cada interacao
            print "%s! = %s" % (self.valor, fatorial)

#metodo main do python para chamar a funcao
if __name__ == '__main__':

    f =  CalculaFatorial(3)

    print " =========================="
    print " o valor do fatorial e: "
    print " =========================="
    #chamada da funcao
    f.fatorial()
    print " =========================="
    print " o valor do fatorial c/ biblioteca math: "
    print " =========================="

    '''chamada da funcao calculaFatorial
    passando por parametro o valor do fatorial
    a ser calculado'''

    f.calculaFatorial(3)


