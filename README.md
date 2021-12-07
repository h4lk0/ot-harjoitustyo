# Ohjelmistotekniikan harjoitustyö
Käyttäjä voi sovelluksen avulla tehdä vieraan kielen sanastoon liittyviä kertaustehtäviä.
## Python-versio
Sovelluksen toiminta on testattu Pythonin versiolla `3.8`, sovellus ei välttämättä ole yhteensopiva vanhempien Python-versioiden kanssa.
## Dokumentaatio
- [Alustava määrittelydokumentti](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/tuntikirjanpito.md)
- [Arkitehtuurikuvaus](https://github.com/h4lk0/ot-harjoitustyo/blob/master/Projekti/dokumentaatio/arkitehtuuri.md)
- [Release](https://github.com/h4lk0/ot-harjoitustyo/releases/tag/viikko5)

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

Koodin muotoilun voi tarkistaa komennolla:

```bash
poetry run invoke lint
```
