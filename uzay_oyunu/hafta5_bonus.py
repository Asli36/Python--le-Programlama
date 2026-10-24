from functools import lru_cache
from uzay_oyunu.dekoratorler import hafiza


@hafiza(maxsize=2)
def kare(n):
    """Kareyi kendi önbelleğimizle hesaplar."""
    print("Hesaplandı:", n)
    return n * n


@lru_cache(maxsize=2)
def kare_lru(n):
    """Aynı sonucu standart önbellekle hesaplar."""
    return n * n


for n in [2, 3, 2, 4, 2]:
    print(n, kare(n), kare_lru(n))