class Banco(object):

    def __init__(self, valor):
        self.valor = valor

    def saque(self):

        acumulativa = []

        #usuario pode sacar ate 1.200 reais
        if ((self.valor < 10)  or (self.valor > 1200)):
            print " quantidade nao  permitada pra saque"
        else:
            print "valor do saque : R$ " +str(self.valor)
            notas_100 = self.valor/100
            notas100 = notas_100
            acumulativa.append(notas100)
            print  "notas de 100 : "+str(notas_100) + " ---> R$"+str(notas_100*100)

            notas_50 = (self.valor-(notas_100*100))/50
            acumulativa.append(notas_50)
            print "notas de 50 :"+ str( notas_50)+ " ---> R$"+str(notas_50*50)
            
            notas_10 = (self.valor-(notas_100*100+notas_50*50))/10
            acumulativa.append(notas_10)
            print  "notas de 10 : "+ str(notas_10) + " ---> R$"+str(notas_10*10)
            
            notas_5 =  (self.valor-(notas_100*100+notas_50*50+notas_10*10))/5
            acumulativa.append(notas_5)
            print  "notas de 5 : " + str(notas_5)+" ---> R$"+str(notas_5*5)
            
            notas_1 = (self.valor-(notas_100*100+notas_50*50+notas_10*10+notas_5*5))
            acumulativa.append(notas_1)
            print  "notas de 1 : "+str(notas_1) + " ---> R$" +str(notas_1*1)
            #exibe o valor total sacado
            print "TOTAL : R$"+str( notas_100*100 + notas_50*50 + notas_10*10 + notas_5*5 +notas_1*1)
        
        return acumulativa
            
if __name__=='__main__':
    p = Banco(300)
    p1 = Banco(350)
    print "===================================="
    print " DEMONSTRATIVO DE ESTRATO BANCO S/A"
    print "===================================="
    print " "+ str(p.saque())
    print " "+ str(p1.saque())

