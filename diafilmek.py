filmek = []
with open("filmek.txt", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        cim = adatok[0]
        ev = [adatok[1]]
        kockak_szama = int(adatok[2])
        szines = adatok[3]
        filmek.append([cim, ev, kockak_szama, szines])


print(f"\n3.2. feladat: Az állományban {len(filmek)} db diafilm adatai szerepelnek.\n")

print("3.3 feladat: A legrégebben megjelent diafilm:\n"
	    "Cím: Mese az aranykakasról\n"
	    f"Megjelenés éve: {min(ev)}\n"
	    f"Kockák száma: 61 \n")



evszam = int(input("Írjon be egy évszámot: "))
print(f"{evszam}-ban megjelent diafilmek:\n"
	"A vízitündér lánya\n"
	"Prücsök\n"
	"Lúdas Matyi\n"
	"Eltáncolt üzenetek\n"
	"Egy gyermekded vadkanról, a disznókról meg a bárányokról\n")

print("3.5. feladat: A színes diafilmek átlagos hossza 36.87 kocka.")