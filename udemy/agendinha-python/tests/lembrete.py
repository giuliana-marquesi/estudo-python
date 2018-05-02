from models.lembrete import Lembrete
import datetime
import pytest

@pytest.fixture
def lembrete():
    date_event = datetime.date(2018,3,14)
    lembrete = Lembrete(date_event, 'niver da gigik')
    return lembrete

def test_getDate(lembrete):
    assert lembrete.date == datetime.date(2018,3,14)

def test_getDescription(lembrete):
    assert lembrete.descr == 'niver da gigik'

def test_setDate(lembrete):
    other_date = datetime.date(1991,3,14)
    lembrete.date = other_date
    assert lembrete.date == datetime.date(1991,3,14)

def test_setDescription(lembrete):
    other_description = 'oieee'
    lembrete.descr = other_description
    assert lembrete.descr == 'oieee'
