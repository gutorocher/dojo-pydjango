#!/usr/bin/python
# -*- coding: utf-8 -*-


# aqui serão implemntada

# a conversão numerica
# de decimal para romano
# de romano para decimal
# verificação de valores romanos inválidos

#implementar interface grafica para projeto futuro...

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
            return lista[0]
        elif valor == 'V':
            return lista[1]
        elif valor == 'X':
            return lista[2]
        else:
            print "valor invalido"

        valor = ['I','V','X']
        resultante = [1,5,10]


if __name__ == '__main__':
    conversorRomanoDecimal('V')


    
