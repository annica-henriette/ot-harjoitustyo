from tkinter import ttk, StringVar, constants
from services.app_service import app_service, UsernameTakenError


class SignUpView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä.
    """
    
    def __init__(self, root, handle_signup, handle_show_login_view):
        """Luokan konstruktori, joka luo uuden rekisteröitymisnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_signup: Arvo, jota kutsutaan, kun käyttäjä luodaan.
            handle_show_login_view: Arvo, jota kutsutaan, kun käyttäjä siirtyy kirjautumisnäkymään.
        """

        self._root = root
        self._handle_signup = handle_signup
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username = None
        self._password = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _signup_handler(self):
        username = self._username.get()
        password = self._password.get()

        if len(username) == 0 or len(password) == 0:
            self._error("Käyttäjätunnus tai salasana ei voi olla tyhjä")
            return

        if len(password) < 3 or len(password) > 30:
            self._error("Salasanan tulee olla 3-30 merkkiä")
            return

        if len(username) > 20:
            self._error("Käyttäjätunnus ei voi olla yli 20 merkkiä")
            return

        try:
            app_service.create_user(username, password)
            self._handle_signup()
        except UsernameTakenError:
            self._error(f"Käyttäjätunnus {username} on jo käytössä")

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username = ttk.Entry(master=self._frame)

        username_label.grid(padx=2, pady=2, sticky=constants.W)
        self._username.grid(padx=2, pady=2, sticky=constants.EW)

    def _password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")

        self._password = ttk.Entry(master=self._frame)

        password_label.grid(padx=2, pady=2, sticky=constants.W)
        self._password.grid(padx=2, pady=2, sticky=constants.EW)

    def _initialize_buttons(self):

        signup_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._signup_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_show_login_view
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_show_login_view
        )

        signup_button.grid(padx=4, pady=4, sticky=constants.EW)
        login_button.grid(padx=4, pady=4, sticky=constants.EW)
        back_button.grid(padx=4, pady=4, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="black",
            background="red"
        )

        heading_label = ttk.Label(
            master=self._frame, text="Luo käyttäjä")
        heading_label.grid(columnspan=2, padx=3, pady=3)

        self._username_field()
        self._password_field()

        self._initialize_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        self._hide_error()
