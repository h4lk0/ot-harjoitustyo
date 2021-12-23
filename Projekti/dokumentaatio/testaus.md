# Testausdokumentti

Ohjelmaa on testattu järjestelmätason manuaalisilla testeillä, sekä automatisoiduilla testeillä unittestin avulla.

## Automatisoidut testit

Jokaisella sovelluslogiikan luokalla on sitä vastaava testitiedosto. Kaikki testitiedostot löytyvät [tests](../src/tests)-pakkauksesta.

### Tietokantametodien testaus

Testit käyttävät omaa, sovelluksen varsinaisesta tietokannasta erillistä, tietokantaa, jonka nimi on määritelty sovelluksen juuressa löytyvässä *.env.test*-tiedostossa.
Tietokantaan tietoa lisäävää tiedostoa käsittelevät metodit käyttävät omaa `tests`-pakkauksen mukana tulee *test-csvfile.csv*-nimistä [tiedostoa](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/src/tests/test-csvfile.csv).

### Testauskattavuus

Testeistä on jätetty pois kaikki käyttöliittymään liittyvä koodi. Seuraava kuva kertoo testauksen haaraumakattavuudesta.

[KUVA]

Testaamatta jäivät jne.

## Järjestelmätestaus

Järjestelmätestit on suoritettu manuaalisesti Linux-ympäristössä.

### Asennus ja konfigurointi

Sovelluksen asentaminen ja käyttö on testattu [käyttöohjeiden](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/kayttoohje.md) mukaan.

### Toiminnallisuus

[Määrittelydokumentissa](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeissa kuvaillut toiminnallisuudet on testattu manuaalisesti sekä oikeilla että virheellisillä arvoilla.

## Laatuongelmat

Testeissä käytettävän .csv-tiedoston nimi on kovakoodattu.
