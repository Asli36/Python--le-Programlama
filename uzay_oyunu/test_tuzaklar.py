from uzay_oyunu.oyun import yakit_ekle

def test_yakit_ekle():
    ilk_cagri = yakit_ekle(10)
    assert ilk_cagri == [10]
    
    ikinci_cagri = yakit_ekle(20)
    assert ikinci_cagri == [20]