# Ohjelman arkkitehtuuri

## Rakenne

Koodin pakkausrakenne on seuraava:

```mermaid
classDiagram
    ui..>services
    services..>repositories
    services..>entities
    repositories..>entities
```
Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin. Pakkaus _services_ sisältää sovelluslogiikasta ja _repositories_ tietojen tallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvastavat sovelluksessa käyettyjä olioita. 

## Käyttöliittymä

Käyttöliittymä sisältää seuraavat näkymät:
- Kirjautuminen (aloitussivu)
- Uuden käyttäjän rekisteröinti
- Treeninäkymä
- Uloskirjautuminen

Näkymien näyttämisestä vastaa _UI_ luokka. Näkymistä aina yksi kerrallaan on näkyvillä ja jokainen on toteutettu omana luokkana. Kun treenien tilanne muuttuu, eli niitä lisätään, muokataan tai poistetaan, kutsutaan sovelluksen metodia _initialize_workouts_, joka luo näkymän uudelleen.

## Sovelluslogiikka

Sovellus muodostuu luokista 

- [User](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/entities/user.py)
- [Workout](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/entities/workout.py)

```mermaid
 classDiagram
       Workout "*" --> "1" User
       class User{
           username
           password
       }
       class Workout{
           content
           date
           user
       }
```

Luokat kuvaavat käyttäjiä jä heidän treenejä. 

Toiminnallisuudesta vastaa luokka [AppService](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/services/app_service.py).

AppService pääsee käsiksi luokkiin User ja Workout luokkien [WorkoutRepository](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/repositories/workout_repository.py) ja [UserRepository](https://github.com/annica-henriette/ot-harjoitustyo/blob/master/src/repositories/user_repository.py) kautta.

```mermaid
 classDiagram
       Workout "*" -- "1" User
       AppService "0..1" -- "0..1" User
       AppService "0..1" -- "0..1" Workout
       AppService ..> UserRepository
       AppService ..> WorkoutRepository
       UserRepository ..> User
       WorkoutRepository ..> Workout
```
## Tietojen pysyväistallennus
Luokat _WorkoutRepository_ ja _UserRepository_ vastaavat tietojen tallentamisesta. Molemmat luokat tallentavat tietoa SQLite-tietokantaan. Molemmat noudattavat _Repository_-suunnittelumallia. 

### Tiedostot
Käyttäjät ja treenit tallennetaan SQLite-tietokannan tauluihin _Users_ ja _Workouts_. Näiden alustus tapahtuu _initialize_database.py_-tiedostossa.

## Sovelluksen päätoiminnallisuudet

Sovelluksen päätoiminnallisuudet voi kuvata seuraavien sekvenssikaavioiden avulla.

### Käyttäjän luominen

Käyttäjän luomiseen tarvitaan syötteenä käyttäjätunnus, joka ei ole jo käytössä, ja salasana. Tämä jälkeen klikataan "Luo käyttäjä"-painiketta.

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant AppService
    participant UserRepository
    participant teemu
    User->>UI: click "Luo käyttäjä" button
    UI->>AppService: create_user("teemu", "123")
    AppService->>UserRepository: find_one_user("teemu")
    UserRepository-->>AppService: None
    AppService->>teemu: User("teemu", "123")
    AppService->>UserRepository: create_user(teemu)
    UserRepository-->>AppService: user
    AppService-->>UI: user
    UI->>UI: show_workout_view()
```

Painikkeen painamisen jälkeen sovelluslogiikan `AppService` selvittää käyttäjätunnuksen ja `UserRepository`:n avulla onko käyttäjätunnus jo olemassa. Jos ei ole, sovelluslogiikka luo `User` -olion ja tallentaa sen `UserRepository`:n `create_user` metodin avulla. Käyttäjä on luotu ja näkymäksi vaihtuu kirjautuneen käyttäjän treenipäiväkirja. 

### Sisäänkirjautuminen

Käyttäjä voi kirjautua sovellukseen kirjoittamalla käyttäjätunnuksen ja salasanan syötekenttiin ja klikkaamalla painiketta "Kirjaudu".

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant AppService
    participant UserRepository
    User->>UI: click "Kirjaudu" button
    UI->>AppService: login("teemu", "123")
    AppService->>UserRepository: find_one_user("teemu")
    UserRepository-->>AppService: user
    AppService-->>UI: user
    UI->>UI: show_workout_view()
```

Painikkeen painamisen jälkeen sovelluslogiikan `AppService` metodi, käyttäjätunnuksen ja salasanan avulla, selvittää `UserRepository`:n avulla onko käyttäjätunnus jo olemassa. Jos käyttäjätunnus on olemassa ja salasanat täsmäävät, kirjautuminen onnistuu ja käyttöliittymä avaa sovelluksen varsinaisen päänäkymän, eli kirjautuneen käyttäjän treeninäkymän.

### Uuden treenin luominen

Sisäänkirjautunut käyttäjä voi lisätä uuden treenin klikkaamalla "Lisää uusi treeni"-painiketta.

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant AppService
    participant WorkoutRepository
    participant workout
    User->>UI: click "Lisää uusi treeni" button
    UI->>AppService: create_workout("running", "2024-04-30", teemu)
    AppService->>workout: Workout("running", "2024-04-30", teemu)
    AppService->>WorkoutRepository: create_workout(workout)
    WorkoutRepository-->>AppService: workout
    AppService-->>UI: workout
    UI->>UI: initialize_workouts()
```

Sama periaate toistuu sovelluksen muissa toiminnallisuuksissa, kuten treenin muokkaamisessa, poistamisessa
ja käyttäjän uloskirjautumisessa.

## Ohjelman heikkoudet

Ohjelmassa ei ole otettu kantaa ohjelman tietoturvaan. 