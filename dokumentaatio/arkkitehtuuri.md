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
