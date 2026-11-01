girdi_n = nput("n: ")
girdi_sinir = input("Üst sınır: ")

if len(girdi_n) == 0 or len(girdi_sinir) == 0:
    print("Hata: Boş değer girdiniz.")
else:
    n = int(girdi_n)
    sinir = int(girdi_sinir)
    
    gecici = n
    adim = 0
    maks_deger = n

    while gecici > 1:
        if gecici > maks_deger:
            maks_deger = gecici
        if gecici % 2 == 0:
            gecici = gecici // 2
        else:
            gecici = 3 * gecici + 1
        adim += 1

    en_uzun_zincir = 0
    en_iyi_sayi = 1
    i = 1

    while i < sinir:
        sayi = i
        sayac = 0
        while sayi > 1:
            sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1
            sayac += 1
        if sayac > en_uzun_zincir:
            en_uzun_zincir = sayac
            en_iyi_sayi = i
        i += 1

    print(f"{n} -> 1: {adim} adım, en yüksek değer {maks_deger}")
    print(f"1-{sinir} arasında en uzun zincir: {en_iyi_sayi} ({en_uzun_zincir} adım)")