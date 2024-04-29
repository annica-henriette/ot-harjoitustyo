class User:
    """Luokka, joka vastaa yksittäisestä käyttäjästä.

    Attributes:
        username: Merkkijono, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijono, joka kuvaa käyttäjän salasanaa.
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.
        """
        self.username = username
        self.password = password
