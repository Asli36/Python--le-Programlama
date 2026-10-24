durum = {
    "konum": "dünya",
    "baglantilar": {"dünya": ["orion", "mars"], "orion": ["dünya"], "mars": ["dünya"]},
    "credits": True, "engines": False, "copilot": True
}
while True:
    hedefler = durum["baglantilar"][durum["konum"]]
    print("Nereye gitmek istersin?")
    for numara, hedef in enumerate(hedefler, 1):
        print(f"[{numara}] {hedef}")
    secim = input("Komut, gezegen numarası veya çıkış: ").strip()
    if secim == "çıkış":
        break
    if secim in KOMUTLAR:
        fonksiyon, aciklama = KOMUTLAR[secim]
        print(fonksiyon(durum))
        continue
    if secim.isdigit() and 1 <= int(secim) <= len(hedefler):
        durum["konum"] = hedefler[int(secim) - 1]
    else:
        print("Geçersiz seçim.")
