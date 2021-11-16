import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def assert_kassapaate(self, rahaa, edulliset, maukkaat):
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.edulliset, edulliset)
        self.assertEqual(self.kassapaate.maukkaat, maukkaat)

    def kassapaatteen_maarat_alussa_oikein(self):
        self.assert_kassapaate(100000, 0, 0)

    def test_kateisosto_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assert_kassapaate(100240, 1, 0)

    def test_kateisosto_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assert_kassapaate(100400, 0, 1)

    def test_kateisosto_edullinen_ei_onnistu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assert_kassapaate(100000, 0, 0)

    def test_kateisosto_maukas_ei_onnistu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assert_kassapaate(100000, 0, 0)

    def test_korttiosto_edullinen(self):
        kortti = Maksukortti(300)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tapahtuma, True)
        self.assertEqual(str(kortti), "saldo: 0.6")
        self.assert_kassapaate(100000, 1, 0)

    def test_korttiosto_maukas(self):
        kortti = Maksukortti(500)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tapahtuma, True)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assert_kassapaate(100000, 0, 1)

    def test_korttiosto_edullinen_ei_onnistu(self):
        kortti = Maksukortti(100)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tapahtuma, False)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assert_kassapaate(100000, 0, 0)

    def test_korttiosto_maukas_ei_onnistu(self):
        kortti = Maksukortti(100)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tapahtuma, False)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assert_kassapaate(100000, 0, 0)

    def test_kortin_lataus(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(str(kortti), "saldo: 3.0")
        self.assert_kassapaate(100200, 0, 0)

    def test_kortin_lataus_ei_onnistu(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assert_kassapaate(100000, 0, 0)

    def test_ladataan_nolla(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 0)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assert_kassapaate(100000, 0, 0)