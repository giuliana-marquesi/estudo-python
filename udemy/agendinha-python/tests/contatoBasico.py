import pytest
from models.telefone import Telefone
from models.contatoBasico import ContatoBasico

contatinhos = {'11909878979': 'Telefone celular', '23456718': 'Telefone residencial', '1234-5678': 'Telefone residencial', 
            '119089-0989': 'Telefone comercial'}

@pytest.fixture
def telefoneobj(telefone, tipo):
    return Telefone(telefone, tipo)

@pytest.fixture
def contato():
    return ContatoBasico()

def test_nenhumTelefone(contato):
    contato.nome('Clodoaldo')
 
    assert contato.nome() == 'Clodoaldo'
    assert contato.getDados() == 'Clodoaldo'

