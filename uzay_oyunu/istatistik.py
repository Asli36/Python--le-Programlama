from functools import reduce, partial

def buyuk_harf_map(gezegenler):
    return list(map(lambda g: g.upper(), gezegenler))

def en_az_iki_baglanti_filter(galaksi_baglantilari):
    return list(filter(lambda g: len(galaksi_baglantilari.get(g, [])) >= 2, galaksi_baglantilari))

def toplam_baglanti_reduce(galaksi_baglantilari):
    return reduce(lambda toplam, komsu_listesi: toplam + len(komsu_listesi), galaksi_baglantilari.values(), 0)

def buyuk_harf_liste_ureteci(gezegenler):
    return [g.upper() for g in gezegenler]

def en_az_iki_baglanti_liste_ureteci(galaksi_baglantilari):
    return [g for g, komsu_listesi in galaksi_baglantilari.items() if len(komsu_listesi) >= 2]

def toplam_baglanti_sum(galaksi_baglantilari):
    return sum(len(komsu_listesi) for komsu_listesi in galaksi_baglantilari.values())

def yolculuk(hiz, mesafe):
    return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)