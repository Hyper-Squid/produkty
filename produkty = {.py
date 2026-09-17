produkty = {
    "jablko": (0.5, "ovocie"),
    "banan": (0.45, "ovocie"),
    "hruska": (0.7, "ovocie"),
    "marhula": (0.8, "ovocie"),
    "slivka": (0.6, "ovocie"),
    "mrkva": (0.4, "zelenina"),
    "petrzlen": (0.5, "zelenina"),
    "celer": (0.9, "zelenina"),
    "zemiak": (0.3, "zelenina"),
    "cokolada": (1.1, "sladkost"),
    "cukor": (0.75, "sladkost"),
    "mlieko": (1.0, "ina vec"),
    "chlieb": (0.8, "ina vec")
}

nakupny_kosik = [
    "jablko",
    "mlieko",
    "cukor",
    "cokolada",
    "chlieb",
    "banan"
]

pocet = int(input("Kolko veci chces pridat do kosika?\n"))

while pocet:
    print("Co chcete pridat?")
    nazov = input().strip().lower()

    if nazov in produkty:
        nakupny_kosik.append(nazov)
        pocet -= 1
    else:
        print("Tato polozka nie je v zozname.")

for polozka in nakupny_kosik:
    cena, kategoria = produkty[polozka]
    print(f"{polozka} - {cena} EUR - {kategoria}")