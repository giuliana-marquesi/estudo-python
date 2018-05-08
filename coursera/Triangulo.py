class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
        
    def tipo_lado(self):
        if self.a == self.b:
            if self.b == self.c:
                return 'equilátero'
            else:
                return 'isósceles'
        elif self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'
    
    def retangulo(self):
        
        ordenado = sorted([self.a, self.b, self.c])
            
        if ordenado[0] ** 2 + ordenado[1] ** 2 == ordenado[2] ** 2:
            return True
        return False
        
    def semelhantes(self, triangulo):
    
        triangulo_self = sorted([self.a, self.b, self.c])
        triangulo_visitante = sorted([triangulo.a, triangulo.b, triangulo.c])
        
        if triangulo_self[0] / triangulo_visitante[0] == triangulo_self[1] / triangulo_visitante[1] and triangulo_self[0] / triangulo_visitante[0] == triangulo_self[2]/ triangulo_visitante[2]:
            return True
        return False
        
        
