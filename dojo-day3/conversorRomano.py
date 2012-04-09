#!/usr/bin/python
# -*- coding: utf-8 -*-

# aqui serão implementado
# os seguintes itens.::
# a conversão numerica
# de romano para decimal
# verificação de valores romanos inválidos

class Conversor(object):

    ''' definir os metodos para a classe para implementar
as funcionalidade do Conversão de Romano para decimal '''

    resultante = [1,5,10]

    def conversorRomanoDecimal(self,valor):
        if valor is not None:
            # a funcao len verifica o tamanho da string
            tamanho = len(valor)
            print "valor do tamanho pelo len", tamanho
            if tamanho == 1:
                if valor == 'I':
                    return self.resultante[0]
                elif valor == 'V':
                    return self.resultante[1]
                elif valor == 'X':
                    return self.resultante [2]
                else:
                    print "valor invalido para valor de 1 caracter"
            
            if tamanho == 2:
                lista = []
                lista = list(valor)

                print " =============================="
                print " a lista é: " + str(lista)
                print " =============================="
                #print lista[0]
                #print lista[1]

                elemento1 = lista[0]
                elemento2 = lista[1]

                if elemento1 == 'I':
                    el1 = int(self.resultante[0])
                elif elemento1 == 'V':
                    el1= int(self.resultante[1])
                elif elemento1 == 'X':
                    el1 = int(self.resultante[2])

                if elemento2 == 'I':
                    el2= int(self.resultante[0])
                elif elemento2 == 'V':
                    el2 = int(self.resultante[1])
                elif elemento2 =='X':
                    el2 = int(self.resultante[2])

                #print el1, el2

                if int(el1) > int(el2):
                    print el1 + el2
                else:
                    if int(el1) < int(el2):
                        print  el2 - el1




if __name__ == "__main__":
    print "valor decimal de V"
    print Conversor().conversorRomanoDecimal('V')
    print "valor decimal de X"
    print Conversor().conversorRomanoDecimal('X')
    print "valor decimal de I"
    print Conversor().conversorRomanoDecimal('I')
    print "valor decimal de IV", Conversor().conversorRomanoDecimal('IV')
    print "valor decimal de VI", Conversor().conversorRomanoDecimal('VI')
