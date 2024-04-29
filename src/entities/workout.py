class Workout:
    """Luokka, joka kuvaa yksittäistä treeniä.

        Attributes:
            content: Merkkijono, joka kuvaa treenin sisältöä.
            date: Merrkijono, joka kuvaa treenin päivämäärää.
            user: User-olio, joka kuvaa treenin omistajaa.
    """
    def __init__(self, content, date, user=None):
        """Luokan konstruktori, joka luo uuden treenin.

        Args:
            content: Merkkijono, joka kuvaa treenin sisältöä.
            date: Merrkijono, joka kuvaa treenin päivämäärää.
            user: User-olio, joka kuvaa treenin omistajaa. Vapaaehtoinen, oletusarvo None.
        """
        self.content = content
        self.date = date
        self.user = user
