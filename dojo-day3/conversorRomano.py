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
                print " a lista empresa é: " + str(lista)
                print " =============================="
                
                elemento1 = lista[0]
                elemento2 = lista[1]
                #resultado1 = 0
                #resultado2 = 0


                if elemento1 > elemento2:      
                    
                    
                    if lista[0] == 'I':
                        resultado1 = 1
                        #return resultado1
                    elif lista[0]== 'V':
                        resultado1 = 5
                        #return resultado1
                    elif lista[0]== 'X':
                        resultado1 = 10
                        #return resultado1
                   
                    elif lista[1]== 'I':
                        resultado2=1
                        #return resultado2
                    elif lista[1] == 'V':
                        resultado2 =5
                        #return resultado2
                    elif lista[1]=='X':
                        resultado2 = 10
                        #return resultado2
                   
                    return  (resultado1) + (resultado2)
                    
                else:
                    if elemento1 < elemento2:
                        return resultado2 - resultado1
                    
       

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
    

    

