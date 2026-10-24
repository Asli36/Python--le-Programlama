def satirlari_oku(yol):
    """Boş ve # ile başlayan satırları atlayarak satırları üretir."""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz

def ayristir(satirlar):
    """Her satırdan (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        parcalar = satir.split()
        if len(parcalar) >= 4 and parcalar[1] == "->":
            kaynak = parcalar[0]
            hedef = parcalar[2]
            yakit = int(parcalar[3])
            yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar, esik):
    """Yakıtı verilen eşikten büyük olan yolculukları süzer."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit