# SW pro obchod, klíč slovníku je kód součástky, hodnota klíče je počet součástek na skladu, sw se zeptá na kód součástky a poté množství, obě informace ulož, následně naprogramuj tři varianty  

sklad = {
    "S11": 10,
    "V12": 100,
    "S13": 20,
    "V14": 300,
    "S15": 420,
    "V16": 15,
}

kod_soucastky = input("Zadej kód součástky: ")
print(kod_soucastky)
pocet_soucastek = input("Zadej počet součástek: ")
pocet_soucastek = int(pocet_soucastek)
print(pocet_soucastek)

# pokud kód není ve slovníku, vypiš "není skladem"
# pokud je skladem, ale je jí méně, vypiš, že lze prodat v omezeném množství a odeber ze skladu
# pokud je na skladě a v dostatečném množství, napiš, že lze uspokojit poptávku v plné výši a sniž počet součástek
if kod_soucastky not in sklad:
    print (f"Tato součástka {kod_soucastky} není skladem.")
else:
    if sklad[kod_soucastky] < pocet_soucastek:
        print (f"Součástku {kod_soucastky} lze prodat jen v omezeném množství {sklad[kod_soucastky]}.")
        sklad.pop(kod_soucastky)
    else:
        print(f"Poptávku lze uspokojit v plné výši.")
        sklad[kod_soucastky] -= pocet_soucastek















