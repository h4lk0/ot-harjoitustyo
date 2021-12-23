# Ohjelmistotekniikan harjoitustyö
Käyttäjä voi sovelluksen avulla tehdä korean kielen sanastoon liittyviä harjoituksia.
## Python-versio
Sovellus vaatii vähintään Pythonin version `3.8.x`
## Dokumentaatio
- [Arkitehtuurikuvaus](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/arkitehtuuri.md)
- [Käyttöohje](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/kayttoohje.md)
- [Määrittelydokumentti](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/vaatimusmaarittely.md)
- [Testausdokumentti](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet suorittamalla komentorivillä komento:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin voi luoda kommennolla:

```bash
poetry run invoke coverage-report
```

Koodin muotoilun voi tarkistaa komennolla. Tarkistukset on määritelty tiedostossa [.pylintrc](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/.pylintrc):

```bash
poetry run invoke lint
```
