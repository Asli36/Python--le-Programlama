# Ad Soyad: Aslı Nur Genç
# Numara: 20253005018
# Tarih:  21.11.2026
# Açıklama: Hafta 8 - Görev 3: Vigenère Şifresi


def vigenere(metin, anahtar, yon=1):
    """Metni anahtar kelimeyle Vigenère şifresine göre şifreler (yon=1) veya çözer (yon=-1)."""
    # Anahtardaki harfleri büyük harfe çevirerek 0-25 arası kaydırma değeri üretir
    temiz_anahtar = anahtar.strip().upper()
    anahtar_uzunlugu = len(temiz_anahtar)

    sonuc = ""
    anahtar_sayaci = 0

    for krk in metin:
        if krk.isalpha():
            # Büyük veya küçük harf başlangıç ASCII kodunu belirler
            if krk.isupper():
                taban_kod = ord("A")
            else:
                taban_kod = ord("a")

            # Metindeki harf konumu (0-25) ve anahtar harfinin kaydırma miktarı (0-25)
            p_degeri = ord(krk) - taban_kod
            anahtar_krk = temiz_anahtar[anahtar_sayaci % anahtar_uzunlugu]
            k_degeri = ord(anahtar_krk) - ord("A")

            # yon=1 şifreleme, yon=-1 çözme işlemi yapar
            yeni_deger = (p_degeri + yon * k_degeri) % 26
            sonuc += chr(taban_kod + yeni_deger)

            # Anahtar yalnızca harf işlendiğinde ilerler
            anahtar_sayaci += 1
        else:
            # Boşluk, noktalama veya rakam gibi harf olmayan karakterler aynen kalır
            sonuc += krk

    return sonuc


# Örnek çıktılar
sifreli = vigenere("Attack at dawn", "LEMON")
cozulmus = vigenere("Lxfopv ef rnhr", "LEMON", -1)

print(f'vigenere("Attack at dawn", "LEMON") -> {sifreli}')
print(f'vigenere("Lxfopv ef rnhr", "LEMON", -1) -> {cozulmus}')