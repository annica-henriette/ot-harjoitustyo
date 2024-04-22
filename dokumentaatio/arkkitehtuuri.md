# Ohjelman arkkitehtuuri

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

### Sisäänkirjautuminen
