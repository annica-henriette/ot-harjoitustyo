### Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi. Valitse _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävän tiedoston nimeä voi konfiguroida _.env_-tiedostossa.
Tiedosto luodaa _data_-hakemistoon.

```
DATABASE_FILENAME=database.sqlite
```

## Näin käynnistät ohjelman

# Ennen ohjelman käynnistämistä: 

Riippuvuudet asennetaan komennolla

```bash
poetry install
```

Vaadittavat alustustoimipiteet suoritetaan komennolla

```bash
poetry run invoke build
```
# Käynnistä sovellus

Sovellus käynnistetään komennolla

```bash
poetry run invoke start
```

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään.

Kirjoita voimassa oleva käyttäjätunnus ja salasana syötekenttiin ja paina "Kirjaudu"-painiketta.

## Käyttäjän luominen

Kirjautusmisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään painamalla "Luo käyttäjä"-painiketta.

Uusi käyttäjä luodaan syöttämällä käyttäjätunnus ja salasana syötekenttiin ja painamalla "Luo käyttäjä"-painiketta.

Jos käyttäjän luominen onnistuu, käyttäjä kirjataan sisään ja siirrytään käyttäjän treeninäkymään.

## Treeninäkymä

Kun käyttäjä on kirjautunut sisään onnistuneesi, näkee hän omat lisätyt treenit.

Treenejä on mahdollista lisätä "Lisää treeni"-painikkeen avulla ja poistaa "Poista treeni"-painikkeen avulla. 

Käyttäjä voi kirjautua ulos klikkaamalla "Kirjaudu ulos"-painiketta oikeassa ylänurkassa. 