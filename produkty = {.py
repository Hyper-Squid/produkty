produkty = ["jablko", "banan", "mrkva", "zemiak", "mlieko"]
ceny = [0.50, 0.45, 0.30, 0.25, 1.20]
druhy = ["ovocie", "ovocie", "zelenina", "zelenina", "mliečne"]
sklad = [5, 3, 4, 6, 2]
kupon = [5]
kosik = []
celkova_cena = 0

while True:
    print("===OBCHOD===")

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

kupon = input("Mas kupon? (ano/nie): ").lower()
if kupon == "ano":
    celkova_cena = celkova_cena * 0.8  # Aplikuj 20% zľavu
    print("Kupon bol uplatnený!")
print("Celková cena po uplatnení kupónu:", celkova_cena, "€")

print("Mas este jeden kupon? (ano/nie):")
if input().lower() == "ano":
    print("Mozes uplatnit iba jeden kupon na nakup.")

print("Celková cena:", round(celkova_cena, 2), "€")

