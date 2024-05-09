# Testausdokumentti

Ohjelmaa on testattu automatisoitujen yksikkö- ja integraatiotestien avulla unittestilla sekä manuaalisilla järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

_AppService_-luokkaa testataan [TestAppService](https://github.com/annica-henriette/ot-harjoitustyo/blob/78014366b699958cdbf52b57fd478261b23f5ed7/src/tests/services/app_service_test.py#L63)-luokalla. Testissä on käytössä _UserRepositoryForTesting_ ja _WorkoutRepositoryForTesting_, jotka tallentavat tietoa.

### Repository-luokat

Luokkia testataan ainoastaan testeissä käytössä olevilla tiedostoilla. _WorkoutRepository_-luokkaa testataan [TestWorkoutRepository](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/tests/repositories/workout_repository_test.py)-luokalla ja _UserRepository_-luokkaa testataan [TestUserRepository](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/tests/repositories/user_repository_test.py)-luokalla.

### Testikattavuus

Sovelluksen testauksen haarautumakattavuus on 97%. 
Testaamatta on jättetty _build.py_, _config.py_ ja _initialize\_database.py_-tiedostot.

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellusta on testattu [käyttöohjeen](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) kuvaamalla tavalla Linux-ympäristössä.

Sovellusta on testattu tilanteissa, jossa tiedostot, jotka tallettavat käyttäjät ja treenit ovat olleet olemassa ja tilanteissa, jossa ohjelma on luonut ne itse.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen toiminnallisuudet on käyty läpi myös virheellisillä arvoilla. 

## Sovelluksen laatuongelmat

Sovellus ei anna virheilmoitusta, kun SQLite tietokantaa ei ole alustettu.