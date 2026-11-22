# Ad Soyad: Aslı Nur Genç
# Numara: 20253005018
# Tarih: 21.11.2026
# Açıklama: Hafta 8 - Görev 5: Türkçe Kelime Sınıfı

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


def turkce_kucult(metin):
    """Metni Türkçe kurallara göre (I -> ı, İ -> i) küçük harfe çevirir."""
    # Önce Türkçe I ve İ dönüşümleri yapılır, ardından standart küçültme uygulanır
    donusmus = metin.replace("İ", "i").replace("I", "ı")
    return donusmus.lower()


class TrKelime:
    """Türkçe alfabe sırasına göre karşılaştırma ve özel metotlar sunan kelime sınıfı."""

    def __init__(self, metin):
        """Kelimeyi Türkçe küçük harf biçiminde saklar."""
        self.metin = turkce_kucult(metin)

    def __str__(self):
        """Kelimeyi metin olarak döndürür."""
        return self.metin

    def __len__(self):
        """Kelimenin karakter sayısını döndürür."""
        return len(self.metin)

    def __getitem__(self, indeks):
        """İndeks veya dilim erişimi sağlar."""
        return self.metin[indeks]

    def __contains__(self, alt_metin):
        """Alt metnin kelime içinde geçip geçmediğini döndürür."""
        return str(alt_metin) in self.metin

    def __eq__(self, diger):
        """İki TrKelime nesnesinin Türkçe küçük harf karşılığının eşitliğini kontrol eder."""
        if isinstance(diger, TrKelime):
            return self.metin == diger.metin
        return self.metin == turkce_kucult(str(diger))

    def __lt__(self, diger):
        """İki kelimeyi ALFABE sırasına göre karşılaştırır; ön ekse kısa olan küçüktür."""
        diger_metin = diger.metin if isinstance(diger, TrKelime) else turkce_kucult(str(diger))
        min_uzunluk = min(len(self.metin), len(diger_metin))

        for i in range(min_uzunluk):
            krk1 = self.metin[i]
            krk2 = diger_metin[i]
            if krk1 != krk2:
                sira1 = ALFABE.find(krk1)
                sira2 = ALFABE.find(krk2)
                # Alfabede bulunmayan karakterler için ASCII fallback kullanılır
                if sira1 != -1 and sira2 != -1:
                    return sira1 < sira2
                return krk1 < krk2

        # Ortak kısım aynıysa kısa kelime diğerinin ön ekidir
        return len(self.metin) < len(diger_metin)

    def buyuk(self):
        """Kelimeyi Türkçe kurallara göre (ı -> I, i -> İ) büyük harfe çevirir."""
        # Önce ı ve i harfleri Türkçe büyük karşılıklarına çevrilir
        donusmus = self.metin.replace("ı", "I").replace("i", "İ")
        return donusmus.upper()


# Örnek çıktılar
print(f'çay < dağ        Türkçe: {TrKelime("çay") < TrKelime("dağ")}     Python str: {"çay" < "dağ"}')
print(f'ılık < iğne      Türkçe: {TrKelime("ılık") < TrKelime("iğne")}   Python str: {"ılık" < "iğne"}')
print(f'ördek < pasta    Türkçe: {TrKelime("ördek") < TrKelime("pasta")} Python str: {"ördek" < "pasta"}')
print(f'TrKelime("Işık") == TrKelime("ışık") -> {TrKelime("Işık") == TrKelime("ışık")}')

k = TrKelime("İSTANBUL")
print(f'k = TrKelime("İSTANBUL") -> {k}        len(k) -> {len(k)}')
print(f'"tan" in k -> {"tan" in k}                      k.buyuk() -> {k.buyuk()}')

#UML DİYAGRAMI:

+-------------------------------------------------------+
|                       TrKelime                        |
+-------------------------------------------------------+
| - metin : str                                         |
| + ALFABE : str = "abcçdefgğhıijklmnoöprsştuüvyz"       |
+-------------------------------------------------------+
| + __init__(metin : str)                               |
| + __str__() : str                                     |
| + __len__() : int                                     |
| + __getitem__(indeks : int | slice) : str             |
| + __contains__(alt_metin : str) : bool                |
| + __eq__(diger : TrKelime | Any) : bool               |
| + __lt__(diger : TrKelime | Any) : bool               |
| + buyuk() : str                                       |
+-------------------------------------------------------+