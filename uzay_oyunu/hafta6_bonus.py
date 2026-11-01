import math

temel_no = "453914880343646"
bulunan_hane = -1

for hane in range(10):
    denenen_no = temel_no + str(hane)
    toplam = 0
    uzunluk = len(denenen_no)
    
    i = uzunluk - 1
    while i >= 0:
        rakam = int(denenen_no[i])
        yer = uzunluk - i
        
        if yer % 2 == 0:
            rakam *= 2
            if rakam > 9:
                rakam -= 9
        
        toplam += rakam
        i -= 1
        
    if toplam % 10 == 0:
        bulunan_hane = hane
        break

print(f"Numara: {temel_no} | Kontrol hanesi: {bulunan_hane}")