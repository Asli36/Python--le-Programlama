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

def say(fonk: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        sarmalayici.cagri += 1
        return fonk(*args, **kwargs)
    sarmalayici.cagri = 0
    return sarmalayici

def log_cagri(fonk: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        tum_arg = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"-> {fonk.__name__}({tum_arg})")
        sonuc = fonk(*args, **kwargs)
        print(f"<- {fonk.__name__} = {repr(sonuc)}")
        return sonuc
    return sarmalayici