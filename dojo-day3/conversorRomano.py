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
            print " valor do tamanho pelo len"
            print tamanho
            if tamanho == 1:
                if valor == 'I':
                   return self.resultante[0]
                elif valor == 'V':
                    return self.resultante[1]
                elif valor == 'X':
                    return self.resultante [2]
                else:
                    print "valor invalido para valor de 1 caracter"
        
    def conversaoDecimal(self):

        if lista[0] == 'I':
            elemento1= self.resultante[0]
            print elemento1
            return elemento1
        elif lista[0]== 'V':
            elemento1= self.resultante[1]
            return elemento1
            print elemento1
        elif lista[0]== 'X':
            elemento1 = self.resultante[2]
            print elemento1
            return elemento1
                   
        elif lista[1]== 'I':
            elemento2= self.resultante[0]
            print elemento2
            return elemento2
        elif lista[1] == 'V':
            lemento2 =self.resultante[1]
            print elemento2
            return elemento2
        elif lista[1]=='X':
            elemento2 = self.resultante[2]
            print elemento2
            return elemento2
            if tamanho == 2:
                lista = []
                lista = list(valor)

                print " =============================="
                print " LISTA ATUAL"
                print " =============================="
                print " a lista empresa é: " + str(lista)
                print " =============================="

                elemento1 = lista[0]
                elemento2 = lista[1]  

            if elemento1 > elemento2:                
                    
                conversaoDecimal()
                print int(elemento1) + int(elemento2)

                   
            else:
                if elemento1 < elemento2:

                    conversorDecimal()
                    print elemento2
                    print elemento1
                    print  (elemento2) - (elemento1)
            

if __name__ == "__main__":
    
    print "valor decimal de V"
    print Conversor().conversorRomanoDecimal('V')
    
    print "valor decimal de X"
    print Conversor().conversorRomanoDecimal('X')
    
    print "valor decimal de I"
    print Conversor().conversorRomanoDecimal('I')

    print "valor decimal de IV"
    print Conversor().conversorRomanoDecimal('IV')
#    print "valor decimal de VI"
#    print Conversor().conversorRomanoDecimal('VI')
    

    

