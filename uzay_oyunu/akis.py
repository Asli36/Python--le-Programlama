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