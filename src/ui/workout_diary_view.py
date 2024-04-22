from tkinter import ttk, StringVar, constants
from services.app_service import app_service, InvalidDate, DuplicateWorkoutError
from datetime import datetime


class WorkoutView:

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._user = app_service.loggedin_user()
        self._create_workout = None
        self._create_workout_date = None
        self._workout_frame = None
        self._workout_view = None
        self._error_message = None
        self._error_label = None
        self._delete_frame = None
        self._delete_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        app_service.logout()
        if self._delete_view:
            self._delete_view.destroy()
        self.destroy()
        self._handle_logout()

    def _handle_create_workout(self):
        workout = self._create_workout.get()
        date = self._create_workout_date.get()
        username = self._user.username

        if workout.strip() and date:
            try:
                app_service.create_workout(workout, date, username)
                self._initialize_workouts()
                if self._delete_view:
                    self._delete_view.destroy()
                self._create_workout.delete(0, constants.END)
                self._create_workout_date.delete(0, constants.END)
                self._hide_error()
            except InvalidDate as error:
                self._error(str(error))
            except DuplicateWorkoutError as error:
                self._error(str(error))

    def _handle_delete_workout(self):
        if self._delete_view:
            self._delete_view.destroy()

        # generoitu koodi alkaa

        def handle_delete_return():
            self._initialize_workouts()
            self._delete_view.destroy()

        # generoitu koodi päättyy

        self._delete_view = WorkoutDeleteView(
            self._delete_frame,
            handle_delete_return # generoitu metodi
        )

        self._delete_view.pack()

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_workouts(self):
        if self._workout_view:
            self._workout_view.destroy()

        workouts = app_service.get_user_workouts()

        self._workout_view = WorkoutListView(
            self._workout_frame,
            workouts
        )

        self._workout_view.pack()

    def _initialize_create_workout_button(self):
        content_label = ttk.Label(master=self._frame, text="Treenin sisältö:")
        date_label = ttk.Label(
            master=self._frame, text="Päivämäärä (YYYY-MM-DD):")

        self._create_workout = ttk.Entry(master=self._frame)
        self._create_workout_date = ttk.Entry(master=self._frame)

        create_workout_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi treeni",
            command=self._handle_create_workout
        )

        content_label.grid(row=2, column=1, padx=2, pady=2, sticky=constants.E)
        date_label.grid(row=3, column=1, padx=2, pady=2, sticky=constants.E)

        self._create_workout.grid(
            row=2, column=2, padx=2, pady=2, sticky=constants.W)
        self._create_workout_date.grid(
            row=3, column=2, padx=2, pady=2, sticky=constants.W)

        create_workout_button.grid(
            row=4,
            column=2,
            padx=2,
            pady=2,
            sticky=constants.W
        )

    def _initialize_delete_workout_button(self):
        delete_workout_button = ttk.Button(
            master=self._frame,
            text= "Poista treeni",
            command = self._handle_delete_workout
        )
        delete_workout_button.grid(
            row=5,
            column=2,
            padx=2,
            pady=2,
            sticky=constants.W
        )

    def _initialize_logout_button(self):

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout_handler
        )

        logout_button.grid(
            row=0,
            column=2,
            padx=2,
            pady=2,
            sticky=constants.E
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._workout_frame = ttk.Frame(master=self._frame)

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="black",
            background="red"
        )

        self._error_label.grid(row=4, column=0, padx=3, pady=3)

        self._initialize_logout_button()

        user_name = ttk.Label(
            master=self._frame, text=f"Tervetuloa {self._user.username}!", foreground="blue")
        user_name.grid(row=0, column=0, padx=4, pady=4, sticky=constants.W)

        self._initialize_workouts()
        self._initialize_create_workout_button()
        self._initialize_delete_workout_button()

        self._workout_frame.grid(row=1, column=0, sticky=constants.W)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)

        self._hide_error()


class WorkoutListView:
    def __init__(self, root, workouts):

        self._root = root
        self._workouts = workouts
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_workout(self, workout):
        workout_frame = ttk.Frame(master=self._frame)
        workout_label = ttk.Label(
            master=workout_frame, text=f"{workout.date}: {workout.content}")

        workout_label.grid(row=0, column=0, padx=3, pady=3, sticky=constants.W)

        workout_frame.grid_columnconfigure(0, weight=1)
        workout_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for workout in self._workouts:
            self._initialize_workout(workout)

class WorkoutDeleteView:
    def __init__(self, root, delete_return):
        self._root = root
        self._frame = None
        self._delete_return = delete_return
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_delete_workout(self):
        workout = self._create_workout.get()
        date = self._create_workout_date.get()
        if workout and date:
            try:
                app_service.delete_one_workout(workout, date)
                self._delete_return()
            except InvalidDate as error:
                self._error(str(error))

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="black",
            background="red"
        )

        self._error_label.grid(row=4, column=0, padx=3, pady=3)

        content_label = ttk.Label(
            master=self._frame, text="Minkä treenin haluat poistaa?")
        content_label.grid(row=0, column=0, padx=4, pady=4, sticky=constants.W)

        workout_label = ttk.Label(master=self._frame, text="Treeni:")
        date_label = ttk.Label(
            master=self._frame, text="Päivämäärä (YYYY-MM-DD):")

        self._create_workout = ttk.Entry(master=self._frame)
        self._create_workout_date = ttk.Entry(master=self._frame)

        delete_workout_button = ttk.Button(
            master=self._frame,
            text="Poista treeni",
            command=self._handle_delete_workout
        )

        workout_label.grid(row=1, column=0, padx=4, pady=4, sticky=constants.W)
        date_label.grid(row=2, column=0, padx=4, pady=4, sticky=constants.W)
        self._create_workout.grid(row=1, column=1, padx=4, pady=4, sticky=constants.W)
        self._create_workout_date.grid(row=2, column=1, padx=4, pady=4, sticky=constants.W)
        delete_workout_button.grid(row=3, column=0, padx=4, pady=4, sticky=constants.W)

        self._hide_error()
