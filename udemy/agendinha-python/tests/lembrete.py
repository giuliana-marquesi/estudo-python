from models.lembrete import Lembrete
import datetime
import pytest

@pytest.fixture
def lembrete():
    date_event = datetime.date(2018,3,14)
    lembrete = Lembrete(date_event, 'niver da gigik')
    return lembrete

def test_get_date(lembrete):
    assert lembrete.date == datetime.date(2018,3,14)

def test_get_description(lembrete):
    assert lembrete.descr == 'niver da gigik'

def test_set_date(lembrete):
    other_date = datetime.date(1991,3,14)
    lembrete.date = other_date
    assert lembrete.date == datetime.date(1991,3,14)

def test_set_description(lembrete):
    other_description = 'oieee'
    lembrete.descr = other_description
    assert lembrete.descr == 'oieee'

def test_read_lembrete(lembrete):
    assert lembrete.read_lembrete() == 'Data: 14/03/18 Descrição: niver da gigik'

def test_update_lembrete(lembrete):
    other_date = datetime.date(1991,3,14)
    other_description = 'nascimento da gigik'
    lembrete.update_lembrete(other_date, other_description)
    assert lembrete.date == datetime.date(1991,3,14)
    assert lembrete.descr == 'nascimento da gigik'
    assert lembrete.read_lembrete() == 'Data: 14/03/91 Descrição: nascimento da gigik'
