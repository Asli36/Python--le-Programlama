c = input("Cümle: ")
h = se = ssz = r = k = 0
b = 0
t = ""
p = ""
v = "aeıioöuüAEIİOÖUÜ"

for x in c:
    t = x + t
    if x != " ":
        if b == 0:
            k += 1
            b = 1
    else:
        b = 0
    
    if ("a" <= x <= "z") or ("A" <= x <= "Z") or (x in v):
        h += 1
        if x in v:
            se += 1
        else:
            ssz += 1
        
        if "A" <= x <= "Z":
            p += chr(ord(x) + 32)
        else:
            p += x
    elif "0" <= x <= "9":
        r += 1

pt = ""
for x in p:
    pt = x + pt

print(f"Harf: {h} Sesli: {se} Sessiz: {ssz} Rakam: {r} Kelime: {k}")
print(f"Ters: {t}")
print("Palindrom" if p == pt and len(p) > 0 else "Palindrom değil")