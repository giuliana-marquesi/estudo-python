from models.telefone import Telefone

def test_comddd_residencial():
    tel = Telefone('118987877', 'Telefone Residencial')

    assert tel.getTelefone() == '118987877 Telefone Residencial'

def test_separadocomhifem_celular():
    tel = Telefone('9876-6768', 'Telefone Celular')

    assert tel.getTelefone() == '9876-6768 Telefone Celular'

def test_comminusculas():
    tel = Telefone('11234567890', 'telefone comercial')

    assert tel.getTelefone() == '11234567890 telefone comercial'


