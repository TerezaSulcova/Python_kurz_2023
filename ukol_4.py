#zadání čísla
telefonni_cislo=input("Zadej telefonní číslo: ")
print(telefonni_cislo)

#zadání zprávy
poslana_zprava= input("Zadej zprávu, kterou chceš poslat: ")
print(poslana_zprava)

def overeni_cisla(telefonni_cislo):
    if len(telefonni_cislo)==9 or (len(telefonni_cislo)==13 and telefonni_cislo[0-4] == "+420"):
        return True
    else:
        return False

def cena_zpravy(poslana_zprava):
    if len(poslana_zprava)%180== 0:
        cena_zpravy = (len(poslana_zprava)// 180)* 3
    else:
        cena_zpravy = ((len(poslana_zprava)// 180) + 1) * 3
    return cena_zpravy
