import unittest

from ugen import spocitaj_vyskyt_osoby


class spocitaj_vyskyt(unittest.TestCase):

    def test__spocitaj_vyskyt_osoby__prazdny_zoznam(self):
        self.assertEqual(spocitaj_vyskyt_osoby(['1234', 'Jozef', 'Miloslav', 'Hurban', 'Legal'], []), 0)

    def test__spocitaj_vyskyt_osoby__zoznam_s_prvkom_hladam_neexistujuci_prvok(self):
        self.assertEqual(spocitaj_vyskyt_osoby(['2345', 'Milan', 'Jano', 'Sladkovic', 'Ilegal'], ['4567', 'mrstefan', 'Milan', 'Rastislav', 'Stefanik', 'Defence']), 0)

    def test__spocitaj_vyskyt_osoby__zoznam_s_troma_prvkami_hladam_existujuci_prvok(self):
        self.assertEqual(spocitaj_vyskyt_osoby(['4563', 'Pista', '', 'Hufnagel', 'Sales'], [['1111', 'phufnage', 'Pista', '', 'Hufnagel', 'Sales'], ['4563', 'phufnage', 'Pista', '', 'Hufnagel', 'Sales'], ['7321', 'phufnage', 'Pista', '', 'Hufnagel', 'Sales']]), 3)


if __name__ == '__main__':
    unittest.main()