"""Görev kaydı ve esnek parametre yönetim modülü."""


def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: str
) -> str:
    """Görev başlığını, adımlarını ve ek bilgileri biçimlendirerek döndürür."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for idx, adim in enumerate(adimlar, start=1):
        satirlar.append(f"  {idx}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1. Doğrudan çağrı örneği
    cikti1 = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe"
    )
    print("--- Doğrudan Çağrı ---")
    print(cikti1)
    print()

    # 2. Liste (*) ve Sözlük (**) açarak (unpacking) çağrı örneği
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    cikti2 = gorev_kaydi(
        "Kara deliğe atla",
        *adim_listesi,
        oncelik="yüksek",
        **ek_bilgiler
    )
    print("--- Unpacking (*) ve (**) Çağrısı ---")
    print(cikti2)