from tkinter import ttk, StringVar, constants
from services.app_service import app_service, InvalidLoginError


class LoginView:
    def __init__(self, root, handle_login, handle_show_sign_up_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_sign_up_view = handle_show_sign_up_view
        self._frame = None
        self._username = None
        self._password = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login(self):
        username = self._username.get()
        password = self._password.get()

        try:
            app_service.login(username, password)
            self._handle_login()
        except InvalidLoginError:
            self._error("Väärä käyttäjätunnus tai salasana")

    def _error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username = ttk.Entry(master=self._frame)

        username_label.grid(padx=3, pady=3)
        self._username.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=3, pady=3)

    def _password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password = ttk.Entry(master=self._frame)

        password_label.grid(padx=3, pady=3)
        self._password.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=3, pady=3)

    def _initialize_buttons(self):

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._login
        )

        signup_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_show_sign_up_view
        )

        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=2, pady=2)

        signup_label = ttk.Label(
            master=self._frame, text="Eikö sinulla ole käyttäjätunnusta?")

        signup_label.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=3, pady=3)

        signup_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=2, pady=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="black",
            background = "red"
        )

        self._error_label.grid(padx=3, pady=3)

        heading_label = ttk.Label(
            master=self._frame, text="Sisäänkirjautuminen")
        heading_label.grid(columnspan=2, sticky=constants.W,
                           padx=3, pady=3)

        self._username_field()
        self._password_field()

        self._initialize_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()
