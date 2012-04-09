import math

class Calculos(object):
i
    def __init__(self, n1, n2, n3,r):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.r =r
    
	
    def areaQudrado(self):
        area = self.n1 * self.n2
        return area
    
    def areaTriangulo(self):
    	area = self.n1 * self.n2 / 2
    	return area

    def areaCirculo(self):
    	area =  math.pi * (self.r*self.r)
        return area
    

    def somaMaisLado(self):
        resultado = self.n1 + self.n2 + self.n3
        return resultado

if __name__ == '__main__':
    print " ============================"
    print " CALCULOS AREA "
    print " ============================"

    c = Calculos(6.0,8.0,20.0,5.0)

    print " Calculo Area Quadrado   : %s" %c.areaQudrado()
    print " Calculo Area tringulo   : %s" %c.areaTriangulo()
    print " Calculo Area tringulo   : %s" %c.areaTriangulo()
    print " Calculo Area circulo    : %s" %c.areaCirculo()
    print " Calculo soma mais lado  : %s" %c.somaMaisLado()

