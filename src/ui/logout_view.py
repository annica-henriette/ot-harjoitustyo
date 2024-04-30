from tkinter import ttk, StringVar, constants
from services.app_service import app_service


class LogoutView:
    """Käyttäjän uloskirjautumisesta vastaava näkymä.
    """

    def __init__(self, root, handle_show_login_view):
        """Luokan konstruktori, joka luo uuden uloskirjautumisnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_show_login_view: Arvo, jota kutsutaan, kun käyttäjä siirtyy kirjautumisnäkymään.
        """

        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Olet kirjautunut ulos")
        heading_label.grid(columnspan=2, padx=3, pady=3)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_show_login_view
        )

        login_button.grid(padx=4, pady=4, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
