from tkinter import ttk, StringVar, constants
from services.app_service import app_service


class WorkoutView:

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._user = app_service.loggedin_user()
        self._create_workout = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        app_service.logout()
        self._handle_logout()

    def _handle_create_workout(self):
        workout = self._create_workout.get()
        username = self._user.username

        if workout:
            app_service.create_workout(workout, username)

    def _initialize_create_workout_button(self):
        self._create_workout = ttk.Entry(master=self._frame)

        create_workout_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi treeni",
            command=self._handle_create_workout
        )

        self._create_workout.grid(
            row=2, column=0, padx=3, pady=3, sticky=constants.EW)

        create_workout_button.grid(
            row=2,
            column=1,
            padx=3,
            pady=3,
            sticky=constants.EW
        )

    def _initialize_logout_button(self):

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout_handler
        )

        logout_button.grid(
            row=0,
            column=1,
            padx=2,
            pady=2,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_logout_button()
        self._initialize_create_workout_button()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
