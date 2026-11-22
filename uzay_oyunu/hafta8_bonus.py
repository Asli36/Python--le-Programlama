def roma_rakamina(sayi):
    """Pozitif onluk tam sayıyı (1-3999) Roma rakamına çevirir."""
  
    # Değer ve karşılık gelen sembol çiftleri büyükten küçüğe sıralı tutulur
  
    deger_sira = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    sembol_sira = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

    kalan = sayi
    roma = ""
    i = 0

    # Uygun en büyük Roma karşılığı eklendikçe sayı azaltılır
  
    while kalan > 0 and i < len(deger_sira):
        deger = deger_sira[i]
        while kalan >= deger:
            roma += sembol_sira[i]
            kalan -= deger
        i += 1

    return roma


def roma_degeri(krk):
    """Tek bir Roma harfinin onluk karşılığını döndürür."""
    if krk == "I":
        return 1
    elif krk == "V":
        return 5
    elif krk == "X":
        return 10
    elif krk == "L":
        return 50
    elif krk == "C":
        return 100
    elif krk == "D":
        return 500
    elif krk == "M":
        return 1000
    return 0


def onluga_roma(roma_metin):
    """Roma rakamı metnini onluk tabandaki tam sayıya çevirir."""
    temiz = roma_metin.strip().upper()
    toplam = 0
    uzunluk = len(temiz)
    i = 0

    # Sağdaki sembolün değeri büyükse çıkarma kuralı (IV=4, IX=9 vb.) uygulanır
  
    while i < uzunluk:
        suanki = roma_degeri(temiz[i])
        if i + 1 < uzunluk:
            sonraki = roma_degeri(temiz[i + 1])
            if suanki < sonraki:
                toplam += sonraki - suanki
                i += 2
                continue
        toplam += suanki
        i += 1

    return toplam


# Örnek çıktılar

print(f"2026 -> {roma_rakamina(2026)}, 1994 -> {roma_rakamina(1994)}")
print(f'XLII -> {onluga_roma("XLII")}')
