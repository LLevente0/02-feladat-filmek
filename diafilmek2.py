filmek = []
with open("filmek.txt", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        cim, ev, kockak_szama, szines = sor.strip().split(';')
        filmek.append([cim, int(ev), int(kockak_szama), szines])

print(f"{filmek=}")