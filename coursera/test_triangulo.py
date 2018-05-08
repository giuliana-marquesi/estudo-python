import pytest
import Triangulo


@pytest.mark.parametrize("a,b,c, esperado", [
    (7,23,3, 'escaleno'),
    (2,2,5, 'isósceles'),
    (2,5,2, 'isósceles'),
    (5,2,2, 'isósceles'),
    (1,2,3, 'escaleno'),
    (45,45,45, 'equilátero')
    ])

def testa_tipo_lado(a,b,c,esperado):
    t = Triangulo.Triangulo(a,b,c)
    assert t.tipo_lado() == esperado

