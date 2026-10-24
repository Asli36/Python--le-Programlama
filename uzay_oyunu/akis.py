from typing import Callable, Any
import time

def sure_olc(fonk: Callable[..., Any]) -> Callable[..., Any]:
    """Verilen fonksiyonun çalışma süresini ölçen ve ekrana yazdıran sarmalayıcı (decorator) fonksiyon."""
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.time()
        sonuc = fonk(*args, **kwargs)
        bitis = time.time()
        print(f"{fonk.__name__} fonksiyonu {bitis - baslangic:.6f} saniyede çalıştı.")
        return sonuc
    return sarmalayici
   from functools import lru_cache

def rota_sayaci(baglantilar):
    """Verilen bağlantılara göre önbellekli (lru_cache) rota sayısı hesaplayan fonksiyon döndürür."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1
        if gezegen not in baglantilar:
            return 0
        return sum(rota_sayisi(komsu, adim - 1) for komsu in baglantilar[gezegen])
    return rota_sayisi 