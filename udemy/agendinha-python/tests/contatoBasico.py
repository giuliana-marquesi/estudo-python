import pytest
from models.telefone import Telefone
from models.contatoBasico import ContatoBasico

contatinhos = {'11909878979': 'Telefone celular', '23456718': 'Telefone residencial', '1234-5678': 'Telefone residencial', 
            '119089-0989': 'Telefone comercial'}

contato = ContatoBasico()

@pytest.fixture
def telefone():
    contatoDaLista = contatinhos.popitem()
    telefone = Telefone(contatoDaLista[0],contatoDaLista[1])
    return telefone
    
def test_nenhumTelefone():
    contato.nome = 'Clodoaldo'
 
    assert contato.nome == 'Clodoaldo'
    assert contato.getDados() == 'Clodoaldo\n'

def test_umTelefone(telefone):
    contato.addToTelefones(telefone)
    assert contato.getDados() == 'Clodoaldo\n119089-0989 Telefone comercial\n'

def test_doisTelefones(telefone):
    contato.addToTelefones(telefone)
    assert contato.getDados() == 'Clodoaldo\n119089-0989 Telefone comercial\n1234-5678 Telefone residencial\n'

def test_mudaNome():
    contato.nome = 'Marcela'

    assert contato.nome == 'Marcela'
    assert contato.getDados() == 'Marcela\n119089-0989 Telefone comercial\n1234-5678 Telefone residencial\n'

def test_insereNumDepoisMudancaNome(telefone):
    contato.addToTelefones(telefone)
    assert contato.getDados() == 'Marcela\n119089-0989 Telefone comercial\n1234-5678 Telefone residencial\n23456718 Telefone residencial\n'
    
