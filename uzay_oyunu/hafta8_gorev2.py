# Ad Soyad: Aslı Nur Genç
# Numara: 20253005018
# Tarih: 21.11.2026
# Açıklama: Hafta 8 - Görev 2: Taban Dönüştürücü

RAKAM = "0123456789ABCDEF"


def onluktan(n, taban):
    """Onluk tabandaki tam sayıyı 2-16 arası istenen tabana çevirip metin döndürür."""
    # Sayı 0 ise doğrudan "0" döndürülür
    if n == 0:
        return "0"

    sonuc = ""
    kalan_sayi = n
    # Kalanları tabana bölerek baştan ekleyip taban karşılığı metni oluşturur
    while kalan_sayi > 0:
        kalan = kalan_sayi % taban
        sonuc = RAKAM[kalan] + sonuc
        kalan_sayi //= taban

    return sonuc


def onluga(metin, taban):
    """Verilen tabandaki metni Horner yöntemiyle onluk sayıya çevirir."""
    # Küçük harf ve baştaki/sondaki boşlukları standartlaştırır
    temiz_metin = metin.strip().upper()
    deger = 0

    # Her basamağın değerini önceki toplamı tabanla çarparak ekler
    for ch in temiz_metin:
        basamak = RAKAM.find(ch)
        deger = deger * taban + basamak

    return deger


# Örnek çıktılar
sayi = 2026
ikilik = onluktan(sayi, 2)
sekizlik = onluktan(sayi, 8)
onaltilik = onluktan(sayi, 16)

print(f"{sayi} -> ikilik {ikilik} · sekizlik {sekizlik} · onaltılık {onaltilik}")
print(
    f'onluga("7ea", 16) = onluga("11111101010", 2) = onluga("3752", 8) = '
    f'{onluga("7ea", 16)}'
)