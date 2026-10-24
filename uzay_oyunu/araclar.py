from typing import Callable, List, Dict

def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında artan bir hamle sayacı döndüren closure fonksiyonu."""
    sayac = 0
    def say():
        nonlocal sayac
        sayac += 1
        return sayac
    return say

def en_bagli_gezegenler(galaksi: Dict[str, List[str]]) -> List[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sıraya göre sıralar."""
    # Bağlantı sayısına göre azalan (-sayi), alfabetik isme göre artan (isim) sıralama
    return sorted(galaksi.keys(), key=lambda gezegen: (-len(galaksi[gezegen]), gezegen))