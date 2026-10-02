produkty = ["jablko", "banan", "mrkva", "zemiak", "mlieko"]
ceny = [0.50, 0.45, 0.30, 0.25, 1.20]
druhy = ["ovocie", "ovocie", "zelenina", "zelenina", "mliečne"]
sklad = [5, 3, 4, 6, 2]

kosik = []
celkova_cena = 0

while True:
    print("\n=== OBCHOD ===")

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

print("Cena pred zľavou:", round(celkova_cena, 2), "€")


# CLUBCARD
clubcard = input("\nChcete naskenovať Clubcard? (ano/nie): ").lower()

if clubcard == "ano":
    celkova_cena = celkova_cena * 0.9
    print("Clubcard bola naskenovaná! Uplatnená zľava 10 %.")
else:
    print("Clubcard nebola použitá.")

print("Vyberte sposob platby:")
vyber_platby = input("1. Hotovosť\n2. Karta\n3. Kupon\nZadajte číslo platby: ")
if vyber_platby == "1":
    print("Platba hotovosťou bola zvolená.")

if vyber_platby == "2":
    print("Platba kartou bola zvolená.")

    if vyber_platby == "3":
        print("Platba kupónom bola zvolená.")

if vyber_platby == "3":
    kupon = input("Chcete použiť kupón? (ano/nie): ").lower()
                         
def pouzit_kupon(celkova_cena):
    if kupon == "ano":
        celkova_cena = celkova_cena * 0.8
        print("Kupón bol použitý! Uplatnená zľava 20 %.")
    else:
        print("Kupón nebol použitý.")
    return celkova_cena

print("\nCelková cena:", round(celkova_cena, 2), "€")

print("\nĎakujeme za nákup!")
