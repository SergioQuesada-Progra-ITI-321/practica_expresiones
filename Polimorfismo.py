# --------------------------------------------------
# Creates main class
# --------------------------------------------------
import math


class Geometria:
    def __init__(self, valores):
        self.valores = valores

    def area(self):
        pass

    def formula(self):
        pass

    def datos(self):
        pass


# --------------------------------------------------
# Creates derived classes with abstract methods
# --------------------------------------------------
class cuadrado(Geometria):
    def area(self):
        return self.valores[0] ** 2

    def formula(self):
        return 'Base * Base'

    def datos(self):
        return self.valores[0]


class rectangulo(Geometria):
    def area(self):
        return self.valores[0] * self.valores[1]

    def formula(self):
        return 'Base * Altura'

    def datos(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1])

class triangulo(Geometria):
    def __init__(self, lados):
        self.valores = lados

    def datos(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1]) + ', ' + str(self.valores[2])

    def area(self):
        a,b,c = self.valores
        semiperimetro = (a + b + c) / 2

        area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

        return area


    def tipoTriangulo(self):
        x = ''
        if self.valores[0] == self.valores[1] and self.valores[1] == self.valores[2] and self.valores[0] == self.valores[2]:
            print('El triángulo es Equilátero')
        if self.valores[0] == self.valores[1] and self.valores[1] != self.valores[2]:
                print('El triángulo es Isósceles')
        else:
            print('El triángulo es Escaleno')

# --------------------------------------------------
# Using classes
# --------------------------------------------------
fig1 = cuadrado([3])
print(f'La formula del cuadrado es {fig1.formula()}.')
print(f'Y con la siguiente lista de valores [{fig1.datos()}] obtenemos un área de {fig1.area()}')

fig2 = rectangulo([3, 5])
print(f'La formula del rectángulo es {fig2.formula()}.')
print(f'Y con la siguiente lista de valores [{fig2.datos()}] obtenemos un área de {fig2.area()}')

fig3 = triangulo([3, 5, 5])
print(f'Con la siguiente lista de valores [{fig3.datos()}] obtenemos un area de {fig3.area()}'.format(fig3.datos(), fig3.area()))
