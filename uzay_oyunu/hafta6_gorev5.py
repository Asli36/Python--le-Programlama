import math

gizli = "KOŞUL"
tahminler = ""
hata = 0
max_hata = 6

while hata < max_hata:
    goruntu = ""
    tamamlandi = 1
    for h in gizli:
        bulundu = 0
        for t in tahminler:
            if h == t:
                bulundu = 1
        if bulundu == 1:
            goruntu += h + " "
        else:
            goruntu += "_ "
            tamamlandi = 0
            
    goruntu = goruntu.strip()
    
    if tamamlandi == 1:
        print(f"{goruntu}  (hata: {hata}/{max_hata})  Kazandınız!")
        break
        
    harf = input(f"{goruntu}  (hata: {hata}/{max_hata})\nHarf: ")
    
    if len(harf) != 1:
        continue
        
    if "a" <= harf <= "z":
        harf = chr(ord(harf) - 32)
    elif harf == "i":
        harf = "İ"
    elif harf == "ı":
        harf = "I"
        
    daha_once_denendi = 0
    for t in tahminler:
        if t == harf:
            daha_once_denendi = 1
            
    if daha_once_denendi == 1:
        print(f"Harf: {harf} ->    Bu harfi zaten denediniz.")
        continue
        
    tahminler += harf
    
    dogru_mu = 0
    for h in gizli:
        if h == harf:
            dogru_mu = 1
            
    if not (dogru_mu == 1):
        hata += 1
        
    kalan_hak = math.floor(max_hata - hata)
else:
    print(f"Kaybettiniz! Gizli kelime: {gizli}")