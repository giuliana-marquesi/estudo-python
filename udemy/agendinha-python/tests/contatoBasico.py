import pytest
from models.telefone import Telefone
from models.contatoBasico import ContatoBasico

tipos = ['Telefone comercial', 'Telefone público', 'telefone celular', 'telefone particular', 

@pytest.fixture
def telefoneobj(telefone, tipo):
    return Telefone(telefone, tipo)

@pytest.fixture
def contato():
    return Contato()

def test_
