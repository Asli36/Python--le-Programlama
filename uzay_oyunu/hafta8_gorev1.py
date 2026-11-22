# Ad Soyad: Aslı Nur Genç
# Numara: 20253005018
# Tarih: 21.11.2026
# Açıklama: Hafta 8 - Görev 1: E-posta Doğrulayıcı

def eposta_denetle(adres):
    """Verilen e-posta adresini kurallara göre kontrol edip durum mesajı döndürür."""
    # 1. Tam olarak bir '@' işareti bulunmalı
    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    # '@' konumunu bulup kullanıcı adı ve alan adını dilimle
    at_indeksi = adres.find("@")
    kullanici_adi = adres[:at_indeksi]
    alan_adi = adres[at_indeksi + 1:]

    # 2. Kullanıcı adı boş olmamalı; harf, rakam, '.', '_', '-' dışında karakter içermemeli
    if len(kullanici_adi) == 0:
        return "Geçersiz kullanıcı adı"

    for krk in kullanici_adi:
        if not (krk.isalnum() or krk == "." or krk == "_" or krk == "-"):
            return f"Geçersiz karakter: '{krk}'"

    # 3. Kullanıcı adı nokta ile başlayıp bitmemeli
    if kullanici_adi.startswith(".") or kullanici_adi.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    # 4. Alan adında en az bir nokta olmalı ve nokta ile başlayıp bitmemeli
    if alan_adi.count(".") < 1 or alan_adi.startswith(".") or alan_adi.endswith("."):
        return "Alan adı hatalı"

    # 5. Adreste art arda iki nokta ('..') bulunmamalı
    if adres.find("..") != -1:
        return "Ardışık nokta (..) içeremez"

    return "Geçerli"


# Örnek testler
ornek1 = "ece.yilmaz@nisantasi.edu.tr"
ornek2 = "ece@@mail.com"
ornek3 = "ece yilmaz@mail.com"
ornek4 = ".ece@mail.com"
ornek5 = "ece@mail"

print(f"{ornek1} -> {eposta_denetle(ornek1)}")
print(f"{ornek2} -> {eposta_denetle(ornek2)}")
print(f"{ornek3} -> {eposta_denetle(ornek3)}")
print(f"{ornek4} -> {eposta_denetle(ornek4)}")
print(f"{ornek5} -> {eposta_denetle(ornek5)}")