import time

def zamanlayici(aralik):
    baslangic = time.time()
    hedef = baslangic + aralik
    while True:
        simdiki = time.time()
        if simdiki >= hedef:
            yield simdiki
            hedef += aralik

def calistir():
    baslangic_zamani = time.time()
    tik_uretici = zamanlayici(2)
    tak_uretici = zamanlayici(5)
    
    son_tik = next(tik_uretici)
    son_tak = next(tak_uretici)
    
    while time.time() - baslangic_zamani < 10:
        simdiki = time.time()
        if simdiki >= son_tik:
            print("tik")
            son_tik = next(tik_uretici)
        if simdiki >= son_tak:
            print("tak")
            son_tak = next(tak_uretici)