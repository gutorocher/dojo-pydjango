#!/usr/bin/python
# -*- coding: utf-8 -*-


# aqui serão implemntada

# a conversão numerica
# de romano para decimal
# verificação de valores romanos inválidos

class Conversor(object):

    ''' definir os metodos para a classe para implementar as funcionalidade do Conversão de Romano para decimal '''

    def conversorRomanoDecimal(valor):    
        if valor is not None:
            tamanho = len(valor)    
            if tamanho == 1 :
                identificaRomano(self,valor)
            elif tamanho == 2 :
                lista = []
                lista = list(valor)
                print lista
                primeiro = identificaRomano(self,lista[0])
                segundo = identificaRomano(self,lista[1])
                if primeiro > segundo:
                    return primeiro + segundo
                else:
                    return segundo - primeiro
                
            
    def identificaRomano(self,valor):
        if valor == 'I':
            return resultante[0]
        elif valor == 'V':
            return resultante[1]
        elif valor == 'X':
            return resultante[2]
        else:
            print "valor invalido"

        valor = ['I','V','X']
        resultante = [1,5,10]


if __name__ == '__main__':
    conversorRomanoDecimal('V')


    
