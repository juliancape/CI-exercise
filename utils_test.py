from test import sum

def test_sum_positivos():
    assert sum(2, 3) == 5

def test_sum_negativos():
    assert sum(-2, -3) == -5

def test_sum_positivo_negativo():
    assert sum(2, -3) == -1

def test_sum_cero():
    assert sum(0, 0) == 0