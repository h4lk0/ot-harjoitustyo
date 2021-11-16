import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)

    def test_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)