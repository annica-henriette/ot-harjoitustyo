import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortti_tulostaa_oikein(self):
        kortti = Maksukortti(200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    # Kortin saldo alussa oikein
    def testin_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    # Rahan lataaminen kasvattaa saldoa oikein
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
        
    # Rahan ottaminen toimii:
        
    # Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
    
    # Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(500)

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    # Metodi palauttaa True, jos rahat riittivät ja muuten False
    
    def test_ota_rahaa_palauttaa_True(self):
        saldo = self.maksukortti.ota_rahaa(500)
        self.assertEqual(saldo, True)
    
    def test_ota_rahaa_palauttaa_False(self):
        saldo = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(saldo, False)

    def test_saldo_euroissa(self):
        saldo = self.maksukortti.saldo_euroina()

        self.assertEqual(saldo, 10.0)


    
  
