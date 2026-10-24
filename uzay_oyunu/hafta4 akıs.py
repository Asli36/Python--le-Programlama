from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayı üreteci (generator)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her çağrıldığında yakıtı tüketim kadar azaltan ve kalan yakıtı üreten üreteç."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit