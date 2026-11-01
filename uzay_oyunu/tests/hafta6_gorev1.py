import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a <= 0 or b <= 0 or c <= 0 or not (abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b):
    print("Hata: Geçersiz üçgen kenarları.")
else:
    if a == b == c:
        tur1 = "Eşkenar"
    elif a == b or b == c or a == c:
        tur1 = "İkizkenar"
    else:
        tur1 = "Çeşitkenar"

    if a >= b and a >= c:
        en_uzun, k1, k2 = a, b, c
    elif b >= a and b >= c:
        en_uzun, k1, k2 = b, a, c
    else:
        en_uzun, k1, k2 = c, a, b

    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    cos_aci = max(-1.0, min(1.0, (k1**2 + k2**2 - en_uzun**2) / (2 * k1 * k2)))
    aci = math.degrees(math.acos(cos_aci))

    if math.isclose(aci, 90, abs_tol=1e-5):
        tur2 = "Dik açılı"
    elif aci < 90:
        tur2 = "Dar açılı"
    else:
        tur2 = "Geniş açılı"

    print(f"Tür: {tur1}, {tur2}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {aci:.2f}°")