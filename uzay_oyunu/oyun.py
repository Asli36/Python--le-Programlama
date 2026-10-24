def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    parcalar = []
    if credits:
        parcalar.append("bol kredi")
    if engines:
        parcalar.append("guclu motor")
    if copilot:
        parcalar.append("yetenekli bir pilot")
    
    if not parcalar:
        return ""
    return "Sende: " + ", ".join(parcalar)

def hedef_menuosu(hedefler: list[str]) -> str:
    sonuc = "Nereye gitmek istersin?\n"
    for i, hedef in enumerate(hedefler, start=1):
        sonuc += f"[{i}] {hedef}\n"
    return sonuc.strip()