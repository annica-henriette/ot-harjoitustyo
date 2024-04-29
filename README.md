# Treenipäiväkirja
Sovelluksen tarkoitus on, että käyttäjä voi kirjautua sisään ja pitää kirjaa omista treeneistä ja hallinnoida niitä.

## Python-versio

Sovelluksen toimintaa on testattu Python-versiolla 3.10.12.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Työaikakirjanpito](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Ensimmäinen release](https://github.com/annica-henriette/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Riippuvuudet asennetaan komennolla

```bash
poetry install
```

2. Vaadittavat alustustoimipiteet suoritetaan komennolla

```bash
poetry run invoke build
```

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

### Pylint

Tiedoston [.pylintrc](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
