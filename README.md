# Workout App
Sovelluksen tarkoitus on, että käyttäjä voi pitää kirjaa omista treeneistä ja hallinnoida niitä.

## Python-versio

Sovelluksen toimintaa on testattu Python-versiolla 

```bash
3.10.12
```
.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Riippuvuudet asennetaan komennolla

```bash
poetry install
```

2. Vaadittavat alustustoimipiteet suoritetaan komennolla

Kesken

3. Sovellus käynnistetään komennolla

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
