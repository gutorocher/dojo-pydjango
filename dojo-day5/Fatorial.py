# _*_coding = utf-8 _*_
__author__ = 'gusrocha'
import math


def calculaFatorial(valor):

    """
    calcula o resultado do fatorial, pelo numero
    passado por paramentro
    """
    resultado = math.factorial(valor)
    print resultado

    
def fatorial(valor):

    fat = valor;

    '''
    neste local e feito analise que sera
    percorrido quando estiver o valor maior que 1.
    '''
    while (valor >1):

        fat = fat*(valor-1)
        #efetuado decremento do valor como no calculo do fatorial
        valor=valor-1
        #imprime o valor do fatorial em cada interacao
        print "%s! = %s" % (valor, fat)

#metodo main do python para chamar a funcao
if __name__ == '__main__':

    print " =========================="
    print " o valor do fatorial e: "
    print " =========================="
    #chamada da funcao
    fatorial(4)
    print " =========================="
    print " o valor do fatorial c/ biblioteca math: "
    print " =========================="

    '''chamada da funcao calculaFatorial
    passando por parametro o valor do fatorial
    a ser calculado'''

    calculaFatorial(4)


