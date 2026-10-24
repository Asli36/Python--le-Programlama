from itertools import islice
from uzay_oyunu.akis import fibonacci

def test_fibonacci_ilk_degerler():
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1

def test_fibonacci_islice():
    sonuc = list(islice(fibonacci(), 12))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    ilk_deneme = list(islice(g, 5))
    ikinci_deneme = list(islice(g, 5))
    assert ilk_deneme != ikinci_deneme