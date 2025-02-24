filmek = []
with open("filmek.txt", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        cim = adatok[0]
        ev = int(adatok[1])
        kockak_szama = int(adatok[2])
        szines = adatok[3]
        filmek.append([cim, ev, kockak_szama, szines])

print(f"{filmek=}")