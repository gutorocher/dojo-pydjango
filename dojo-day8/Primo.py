# -*- coding: utf-8 -*- 

#Autor: Gustavo, Elber
#=============================================================
#Autor: Gustavo, Elber, Edgar, Vinicius, Jonas Cruz
#Caso:
# Implementar Classe numeroPrimo
#todos os objetos informam seus valores
# implementar todas as funcionalidade contida no testePrimo.py

#PASSO 1 - implementar teste
#PASSO 2 - implementar funcionalidade
#PASSO 3 - Voltar o passo 1

#=================================================================

class numeroPrimo(object):

    def __init__(self, num):
        self.num = num

    def divisao_sucessiva(self):
        fator = []
        acumulador = 2
        resultado = self.num
        while (resultado > 1):
            '''analiso se o numero e divisao exata
            caso afirmativo eu adiciono o numero a lista e faz a divisao 
            ate quando for possivel'''           
            if(resultado % acumulador == 0):
                resultado = resultado / acumulador
                fator.append(acumulador)
            ''' verificar se o numero nao faz divisao exato
            caso o mesmo nao faz incrementar o acumulador para o numero seguinte
            e feito novamente a estrutura ate que e o resutado seja igual a 1 '''
            if (resultado % acumulador != 0):
                acumulador = acumulador + 1
        ''' enviar o valor para o fator, caso nao colocar assim, gera o none'''
        return fator

''' metodo main da classe '''
if __name__ == '__main__':
    '''valores a ser testado '''
    p  = numeroPrimo(10)
    p0 = numeroPrimo(4)
    p1 = numeroPrimo(5)
    p2 = numeroPrimo(100)
    p3 = numeroPrimo(198)
    p4 = numeroPrimo(276)
    print "=============================="
    print "Resultado dos fator primos: "
    print "=============================="
    print  "  "+str(p0.num) +"= "+ str(p0.divisao_sucessiva())
    print  "  "+str(p1.num) +"= "+ str(p1.divisao_sucessiva())
    print  " "+str(p.num) +"= " +  str(p.divisao_sucessiva())
    print  str(p2.num) +"= "+ str(p2.divisao_sucessiva())
    print  str(p3.num) +"= "+ str(p3.divisao_sucessiva())
    print  str(p4.num) +"= "+ str(p4.divisao_sucessiva())
    print "==============================="
    
