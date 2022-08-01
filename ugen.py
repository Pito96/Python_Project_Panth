# import kniznic
from argparse import ArgumentParser

#funkcia pre vytvorenie username
def vytvor_username(osoba):
    # priprava prvkov pre username
    priezvisko = osoba[3]
    meno = osoba[1]
    meno2 = osoba[2]

    # podmienka pre vytvorenie username osoby s jednym menom
    if meno2 == '':
        username = (meno[0] + priezvisko).lower()
    # podmienka pre vytvorenie username osoby s dvoma menami
    else:
        username = (meno[0] + meno2[0] + priezvisko).lower()
    # username moze mat max 8 znakov
    username = username[0:8]
    return username


#funkcia, ktora pocita, ci sa osoba s rovnakym menom/menami uz vyskytla v zozname a vracia pocet jej vyskytov
def spocitaj_vyskyt_osoby(osoba, zoznam_osob):
    pocet = 0
    for o in zoznam_osob:
        if o[2:] == osoba[1:]:
            pocet += 1
    return pocet

#funkcia, ktora prida cislo k username podla poctu vyskytu toho isteho username
def pridaj_cislo_username(username, osoba, zoznam_osob):
    # pouzitie metody pre pocitanie vyskytu urcitej osoby a pridelenie cisla za username
    vyskyt = spocitaj_vyskyt_osoby(osoba, zoznam_osob)
    if vyskyt > 0:
        username = username + str(vyskyt)
    return username


parser = ArgumentParser()
parser.add_argument(dest='vstupny_subor', metavar='INPUT_FILE', nargs='+',
                    help='read people from INPUT_FILE')
parser.add_argument('-o', '--output', dest='vystupny_subor', required=True,
                    help='write usernames to OUTPUT_FILE', metavar='OUTPUT_FILE')
args = parser.parse_args()

zoznam_osob = []

# cyklus pre jeden alebo viac vstupnych .txt suborov
for s in args.vstupny_subor:
    with open(s, 'r') as subory_zaznamov:
        # cyklus pre pracu s jednotlivymi zaznamami v .txt suboroch
        for riadok in subory_zaznamov:
            osoba = riadok.strip().split(':')
            username = vytvor_username(osoba)
            username = pridaj_cislo_username(username, osoba, zoznam_osob)
            # pridanie username k osobe za ID
            osoba.insert(1, username)
            # pridanie osoby do zoznamu osob
            zoznam_osob.append(osoba)

# naplnenie vystupneho .txt suboru osobami s usernames
with open(args.vystupny_subor, 'w') as subor_vystupov:
    for r in zoznam_osob:
        # priradenie : medzi prvky
        list_s_dvojb = ':'.join(r)
        # zapis osob do zoznamu, kazdu na novy riadok
        subor_vystupov.write(f'{list_s_dvojb}\n')


