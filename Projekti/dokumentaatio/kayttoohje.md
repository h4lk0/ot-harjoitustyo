# Käyttöohje

Lataa uusin projektin viimeisin versio [täältä](https://github.com/h4lk0/ot-harjoitustyo/releases).

## Konfigurointi

Sovelluksen käyttämän tietokantatiedoston nimi on määritelty juuressa sijaitsevassa .env-[konfiguraatiotiedostossa](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/.env). Tiedoston on alussa seuraavanlainen:

```
DATABASE_FILENAME = wordlists.db
```
## Käynnistäminen

1. Asenna riippuvuudet suorittamalla komentorivillä komento:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Aloitusruutu

Ohjelman aloitusruutu, josta valitaan joko tehtäviin siirtyminen "Exercises"-painikkeella tai avataan listanäkymä uuteen ikkunaan "Manage lists"-painikkeella. "Exit"-painike sulkee ohjelman.

## Sanalistojen hallinta

Uuden sanalistan voi luoda kirjoittamalla ylimpään testikenttään uuden listan nimen ja painamalla "Add"-painiketta. "Quit"-painike sulkee listojenhallintaikkunan.
Tiputusvalikosta voi valita sanalistan, johon haluaa lisätä sanoja. Muokkausvalikko aukeaa, kun tiputusvalikosta valitaan jokin vaihtoehdoista.

[KUVA]

Listaan voi lisätä yksittäisen rivin kirjoittamalla englanninkielisen ja koreankielisen vastineen niille varattuihin syötekenttiin ja painamalla "Add to list"-nappulaa. Rivejä voi lisätä usean kerralla .csv-tiedostosta painikkeella "Add from .csv"

## Tehtävät

Tehtävänäkymässä valitaan tiputusvalikosta sanalista, jota halutaan käyttää tehtävissä. Oletusarvona on tietokannan ensimmäinen sanalista. Painikkeista valitaan tehtävätyyppi: monivalinta, aukkotehtävä tai opintokortti. "Back"-painike palauttaa ohjelman aloitusnäkymään.

### Monivalinta

Vastaus valitaan valintanapeilla ja tarkistetaan "Check"-painikkeella. "Next"-painike muuttuu klikattavaksi, kun vastaus tarkistetaan ja sillä päästään seuraavaan kysymykseen. "Back"-painikkeella palataan takaisin tehtävätyypinvalintaan.

### Aukkotehtävä

Vastaus kirjoitetaan syötekenttään ja tarkistetaan "Check"-painikkeella. "Next"-painike muuttuu klikattavaksi, kun vastaus tarkistetaan ja sillä päästään seuraavaan kysymykseen. "Back"-painikkeella palataan takaisin tehtävätyypinvalintaan.

### Opintokortti

Koreankielisen sanan ja englanninkielisen käännöksen välillä liikutaan "Flip"-painikkeella. "Next"-painike vaihtaa sanaa.
