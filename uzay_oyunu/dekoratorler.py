import time
from functools import wraps
from typing import Callable, Any

def sure_olc(fonk: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonk(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{fonk.__name__}: {bitis - baslangic:.4f} sn")
        return sonuc
    return sarmalayici