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
            tamanho = len(valor)    
            if tamanho == 1:
                if valor == 'I':
                    return self.resultante[0]
                elif valor == 'V':
                    return self.resultante[1]
                elif valor == 'X':
                    return self.resultante [2]
                else:
                    print "valor invalido para valor de 1 caracter"
            
            if tamanho == 2 :
                lista = []
                lista = list(valor)
                print " =============================="
                print " LISTA"
                print " =============================="
                print " resposta é: " + str(lista)
                print " =============================="
                
                elemento1 = lista[0]
                elemento2 = lista[1]

                if elemento1 > elemento2:                
                    
                    if lista[0] == 'I':
                        temp1 = self.resultante[0];return temp1
                    elif lista[0]== 'V':
                        temp1= self.resultante[1];return temp1
                        print "teste" +str(temp1)
                    elif lista[0]== 'X':
                        temp1 =  self.resultante[2];return temp1
                   
                    elif lista[1]== 'I':
                        temp2= self.resultante[0];return temp2
                    elif lista[1] == 'V':
                        temp2 =self.resultante[1]; return temp2
                    elif lista[1]=='X':
                        temp2 = self.resultante[2];return temp2
                   
                    print temp1 + temp2
                    
                else:
                    return elemento2 - elemento1
                    
       

if __name__ == "__main__":
    
#    print " valor decimal de V"
#    print Conversor().conversorRomanoDecimal('V')
#    
#    print "valor decimal de X"
#    print Conversor().conversorRomanoDecimal('X')
#    
#    print "valor decimal de I"
#    print Conversor().conversorRomanoDecimal('I')
    
    print Conversor().conversorRomanoDecimal('I')
#    print "valor decimal de IV"
#    print Conversor().conversorRomanoDecimal('IV')
#    print "valor decimal de VI"
#    print Conversor().conversorRomanoDecimal('VI')
    

