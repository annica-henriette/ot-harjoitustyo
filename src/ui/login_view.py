from tkinter import ttk, StringVar, constants
from services.app_service import app_service

class LoginView:
    def __init__(self, root, handle_login, handle_show_sign_up_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_sign_up_view = handle_show_sign_up_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Sisäänkirjautuminen")

        signup_label = ttk.Label(master=self._frame, text="Eikö sinulla ole käyttäjätunnusta?")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._handle_login
        )

        signup_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_show_sign_up_view
        )

        Pos_X=2
        Pos_Y=2

        heading_label.grid(columnspan=2, sticky=constants.W, padx=Pos_X, pady=Pos_Y)

        username_label.grid(padx=Pos_X, pady=Pos_Y)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=Pos_X, pady=Pos_Y)
        password_label.grid(padx=Pos_X, pady=Pos_Y)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=Pos_X, pady=Pos_Y)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=Pos_X, pady=Pos_Y)

        signup_label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=Pos_X, pady=Pos_Y)
        signup_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=Pos_X, pady=Pos_Y)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
