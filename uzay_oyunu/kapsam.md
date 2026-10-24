# Kapsam (Scope) ve UnboundLocalError Açıklamaları

## 1. Kapsam Örnekleri ve Sonuçları
- **Örnek 1:** Fonksiyon dışındaki global değişkene erişim (okuma) hatasız çalışır.
- **Örnek 2:** Fonksiyon içinde aynı isimle yerel değişken tanımlandığında yerel kapsam geçerli olur.
- **Örnek 3:** `UnboundLocalError`, bir fonksiyon içinde yerel değişkene atama yapılmadan önce o değişkenden okunmaya çalışıldığında Python'ın değişkeni yerel algılayıp henüz değer atanmadığı için hata vermesi durumudur.

Hiçbir görevde `global` anahtar kelimesi kullanılmamıştır.