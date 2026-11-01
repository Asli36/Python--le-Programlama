tc = input("T.C. kimlik no: ")

hatali = 0
if len(tc) != 11:
    hatali = 1
else:
    for x in tc:
        if not ("0" <= x <= "9"):
            hatali = 1

if hatali == 1 or tc[0] == "0":
    print("GEÇERSİZ")
else:
    t_toplam = 0
    c_toplam = 0
    sayac = 1
    
    for x in tc:
        if sayac <= 9:
            rakam = int(x)
            if sayac == 1 or sayac == 3 or sayac == 5 or sayac == 7 or sayac == 9:
                t_toplam += rakam
            else:
                c_toplam += rakam
        sayac += 1
    
    h10 = (7 * t_toplam - c_toplam) % 10
    h11 = (t_toplam + c_toplam + h10) % 10
    
    gercek_h10 = int(tc[9])
    gercek_h11 = int(tc[10])
    
    if h10 == gercek_h10 and h11 == gercek_h11:
        print(f"Tek: {t_toplam} Çift: {c_toplam} 10. hane: {h10} 11. hane: {h11} -> GEÇERLİ")
    else:
        print("GEÇERSİZ")