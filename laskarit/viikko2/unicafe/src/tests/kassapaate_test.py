import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_edullisesti_kateisella_vahentaa_oikein(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vaihto, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_vahenna_vaarin(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_vahentaa_oikein(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihto, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_ei_vahenna_vaarin(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_vahentaa_oikein(self):
        kortti = Maksukortti(1000)
        vaihto = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(vaihto, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    
    def test_syo_maukkaasti_kortilla_vahentaa_oikein(self):
        kortti = Maksukortti(1000)
        vaihto = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(vaihto, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kortilla_ei_vahenna_vaarin(self):
        kortti = Maksukortti(100)
        vaihto = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(vaihto, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    
    def test_syo_maukkaasti_kortilla_ei_vahenna_vaarin(self):
        kortti = Maksukortti(100)
        vaihto = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(vaihto, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(10000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+100)
        self.assertEqual(kortti.saldo, 10000+100)
    
    def test_lataa_rahaa_kortille_ei_negatiivinen(self):
        kortti = Maksukortti(10000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 10000)


