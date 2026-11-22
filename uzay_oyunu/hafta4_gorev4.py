def obeb(a, b):
    """İki sayının en büyük ortak bölenini döndürür."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a or 1


class Kesir:
    """Sade kesir ve özel karşılaştırma/aritmetik metotlarını tanımlar."""

    def __init__(self, pay, payda=1):
        """Kesri sadeleştirir ve işaretini payda yerine payda/pay düzenine sokar."""
        if payda == 0:
            raise ZeroDivisionError("Payda 0 olamaz.")
        if payda < 0:
            pay, payda = -pay, -payda
        ortak = obeb(pay, payda)
        self.pay = pay // ortak
        self.payda = payda // ortak

    def __str__(self):
        """Kesri metin olarak döndürür."""
        return f"{self.pay}" if self.payda == 1 else f"{self.pay}/{self.payda}"

    def __add__(self, diger):
        """Yeni Kesir nesnesi olarak toplama yapar."""
        return Kesir(self.pay * diger.payda + diger.pay * self.payda, self.payda * diger.payda)

    def __sub__(self, diger):
        """Yeni Kesir nesnesi olarak çıkarma yapar."""
        return Kesir(self.pay * diger.payda - diger.pay * self.payda, self.payda * diger.payda)

    def __mul__(self, diger):
        """Yeni Kesir nesnesi olarak çarpma yapar."""
        return Kesir(self.pay * diger.pay, self.payda * diger.payda)

    def __truediv__(self, diger):
        """Yeni Kesir nesnesi olarak bölme yapar."""
        if diger.pay == 0:
            raise ZeroDivisionError("Sıfıra bölünemez.")
        return Kesir(self.pay * diger.payda, self.payda * diger.pay)

    def __eq__(self, diger):
        """Çapraz çarpımla eşitliği kontrol eder."""
        return self.pay * diger.payda == diger.pay * self.payda

    def __lt__(self, diger):
        """Çapraz çarpımla küçüklüğü (<) kontrol eder."""
        return self.pay * diger.payda < diger.pay * self.payda

    def __le__(self, diger):
        """Çapraz çarpımla küçük veya eşitliği (<=) kontrol eder."""
        return self.pay * diger.payda <= diger.pay * self.payda

    def __float__(self):
        """Kesri float değere çevirir."""
        return self.pay / self.payda


# (a) n=2..10 çarpımı

carpim = Kesir(1, 1)
for n in range(2, 11):
    carpim = carpim * (Kesir(1, 1) - Kesir(1, n))

# (b) Sadece '<' ile en büyük kesri bulma

k1, k2, k3, k4, k5 = Kesir(3, 7), Kesir(5, 12), Kesir(2, 5), Kesir(4, 9), Kesir(3, 8)
en_buyuk = k1
if en_buyuk < k2:
    en_buyuk = k2
if en_buyuk < k3:
    en_buyuk = k3
if en_buyuk < k4:
    en_buyuk = k4
if en_buyuk < k5:
    en_buyuk = k5

print(f"Çarpım: {carpim}        En büyük: {en_buyuk}")
print(f"Kesir(6, 8) == Kesir(3, 4) -> {Kesir(6, 8) == Kesir(3, 4)}        Kesir(3, 4) / Kesir(3, 8) -> {Kesir(3, 4) / Kesir(3, 8)}")
