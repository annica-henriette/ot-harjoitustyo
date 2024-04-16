from tkinter import ttk, StringVar, constants
from services.app_service import app_service


class WorkoutView:

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._user = app_service.loggedin_user()
        self._create_workout = None
        self._workout_frame = None
        self._workout_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        app_service.logout()
        self.destroy()
        self._handle_logout()

    def _handle_create_workout(self):
        workout = self._create_workout.get()
        username = self._user.username

        if workout:
            app_service.create_workout(workout, username)
            self._initialize_workouts()
            self._create_workout.delete(0, constants.END)

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
            column=0,
            padx=2,
            pady=2,
            sticky = constants.W
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._workout_frame = ttk.Frame(master=self._frame)

        self._initialize_logout_button()
        self._initialize_workouts()
        self._initialize_create_workout_button()

        self._workout_frame.grid(row=1, column=0, columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)

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
        workout_label = ttk.Label(master=workout_frame, text=workout.content)

        workout_label.grid(row=0, column=0, padx=3, pady=3)

        workout_frame.grid_columnconfigure(0, weight=1)
        workout_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for workout in self._workouts:
            self._initialize_workout(workout)
