produkty = ["jablko", "banan", "mrkva", "zemiak", "mlieko"]
ceny = [0.50, 0.45, 0.30, 0.25, 1.20]
druhy = ["ovocie", "ovocie", "zelenina", "zelenina", "mliečne"]
sklad = [5, 3, 4, 6, 2]

kosik = []
celkova_cena = 0

while True:
    print("\n--- OBCHOD ---")

    for i in range(len(produkty)):
        if sklad[i] == 0:
            print(produkty[i], "-", druhy[i], "-", ceny[i], "€ - VYPREDANÉ")
        else:
            print(produkty[i], "-", druhy[i], "-", ceny[i], "€ - sklad:", sklad[i])

    vyber = input("\nNapíš názov produktu (alebo 'koniec'): ").lower()

    if vyber == "koniec":
        break

    if vyber not in produkty:
        print("Tento produkt neexistuje!")
        continue

    pozicia = produkty.index(vyber)

    if sklad[pozicia] == 0:
        print("Tento produkt je vypredaný!")
    else:
        kosik.append(produkty[pozicia])
        celkova_cena = celkova_cena + ceny[pozicia]
        sklad[pozicia] = sklad[pozicia] - 1

        print("Produkt bol pridaný do košíka!")

print("\n--- KOŠÍK ---")

for produkt in kosik:
    print("-", produkt)

print("Celková cena:", celkova_cena, "€")
