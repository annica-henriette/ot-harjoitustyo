# Vaatimusmäärittely


## Sovelluksen kuvaus

Sovelluksen avulla käyttäjän on mahdollista pitää kirjaa treeneistä. Sovellusta on mahdollista käyttää useamman 
käyttäjän, jotka kaikki ovat luoneet tunnuksen ja pitävät kirjaa omista treeneistä.

## Käyttäjät

Sovellukseen suunnitellaan toteutettavan sekä normaalit käyttäjät, että myöhemmin pääkäyttäjät. 

## Käyttöliittymä

Sovellus koostu neljästä näkymästä. Sovellus aukeaa kirjautumisnäkymään, josta voi siirtyä uuden käyttäjän luomisnäkymään ja treenipäiväkirjaan. Treenipäiväkirjasta voi siirtyä uloskirjautumisnäkymään.

## Toiminnallisuudet

- Käyttäjä voi luoda käyttäjätunnuksen 
	- Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan 1-20 merkkiä
- Käyttäjä voi kirjautua järjestelmään
	- Kirjautuminen onnistuu, kun syötetään olemassaoleva käyttäjätunnus ja salasana
	- Jos käyttäjä ei ole olemassa tai salasana ei täsmää, syntyy virheilmoitus
- Käyttäjä voi hallinnoida omia treenejä 
	- Käyttäjä voi lisätä uuden treenin
		- Käyttäjä lisää treenille päivämäärän
		- Treeni näkyy ainoastaan kirjautuneelle käyttäjälle, joka on sen luonut
		- Jos käyttäjä yrittää luoda treenin sisällöllä ja päivämäärällä, joka on jo olemassa, syntyy virheilmoitus
	- Käyttäjä voi poistaa treenin
	- Käyttäjä voi muokata treenin sisältöä
		- Jos käyttäjä yrittää lumuokata treeniä sisällöllä ja päivämäärällä, joka on jo olemassa, syntyy virheilmoitus
- Käyttäjä voi kirjautua ulos

## Jatkokehitysideoita
- Treenit näkyväksi scrollattavaan listaan
- Kalenterinäkymä

