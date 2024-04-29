from tkinter import ttk, StringVar, constants
from services.app_service import app_service, InvalidDate, DuplicateWorkoutError, NoSuchWorkoutError
from datetime import datetime


class WorkoutView:
    """Treenien listauksesta, lisäämisestä, muokkaamisesta ja poistamisesta vastaava näkymä.
    """

    def __init__(self, root, handle_show_logout_view):
        """Luokan konstruktori, joka luo uuden treeninäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout: Arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
        """

        self._root = root
        self._handle_show_logout_view = handle_show_logout_view
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
        self._modify_frame = None
        self._modify_view = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _logout_handler(self):
        app_service.logout()
        if self._delete_view:
            self._delete_view.destroy()
        if self._modify_view:
            self._modify_view.destroy()
        self.destroy()
        self._handle_show_logout_view()

    def _handle_create_workout(self):
        workout = self._create_workout.get().lstrip()
        date = self._create_workout_date.get()
        username = self._user.username

        if len(workout) > 100:
            self._error("Treenin sisältö liian pitkä")
            return

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
        if self._modify_view:
            self._modify_view.destroy()

        # generoitu koodi alkaa

        def handle_delete_return():
            self._initialize_workouts()
            self._delete_view.destroy()

        # generoitu koodi päättyy

        self._delete_view = WorkoutDeleteView(
            self._delete_frame,
            handle_delete_return  # generoitu metodi
        )

        self._delete_view.pack()

    def _handle_modify_workout(self):
        if self._modify_view:
            self._modify_view.destroy()
        if self._delete_view:
            self._delete_view.destroy()

        # generoitu koodi alkaa

        def handle_modify_return():
            self._initialize_workouts()
            self._modify_view.destroy()

        # generoitu koodi päättyy

        self._modify_view = WorkoutModifyView(
            self._modify_frame,
            handle_modify_return  # generoitu metodi
        )

        self._modify_view.pack()

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_workouts(self):
        if self._workout_view:
            self._workout_view.destroy()

        workouts = app_service.get_user_workouts()
        sorted_workouts = sorted(workouts, key=lambda workout: workout.date)

        self._workout_view = WorkoutListView(
            self._workout_frame,
            sorted_workouts
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

        content_label.grid(row=3, column=0, padx=2,
                           pady=2, sticky=constants.EW)
        date_label.grid(row=4, column=0, padx=2, pady=2, sticky=constants.EW)

        self._create_workout.grid(
            row=3, column=1, padx=2, pady=2, sticky=constants.EW)
        self._create_workout_date.grid(
            row=4, column=1, padx=2, pady=2, sticky=constants.EW)

        create_workout_button.grid(
            row=5,
            column=1,
            padx=2,
            pady=2,
            sticky=constants.EW
        )

    def _initialize_other_buttons(self):
        modify_workout_button = ttk.Button(
            master=self._frame,
            text="Muokkaa treeniä",
            command=self._handle_modify_workout
        )

        modify_workout_button.grid(
            row=7,
            column=0,
            padx=2,
            pady=2,
            sticky=constants.W
        )

        delete_workout_button = ttk.Button(
            master=self._frame,
            text="Poista treeni",
            command=self._handle_delete_workout
        )
        delete_workout_button.grid(
            row=8,
            column=0,
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
            column=3,
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

        self._error_label.grid(row=5, column=2, padx=3, pady=3)

        self._initialize_logout_button()

        user_name = ttk.Label(
            master=self._frame, text=f"Tervetuloa {self._user.username}!",
            background="blue",
            foreground="white",
            font=("Helvetica", 12, "bold"))
        user_name.grid(row=0, column=0, columnspan=3, padx=4,
                       pady=(10, 4), sticky=constants.W)

        self._initialize_workouts()

        create_label = ttk.Label(
            master=self._frame, text="Haluatko lisätä treenin?", font=("Helvetica", 10, "bold"))
        create_label.grid(row=2, column=0, columnspan=3,
                          padx=4, pady=(10, 4), sticky=constants.W)

        self._initialize_create_workout_button()

        functions_label = ttk.Label(
            master=self._frame, text="Haluatko muokata tai poistaa treenin?",
            font=("Helvetica", 10, "bold"))
        functions_label.grid(row=6, column=0, columnspan=3,
                             padx=4, pady=(10, 4), sticky=constants.W)

        self._initialize_other_buttons()

        self._workout_frame.grid(row=1, column=0, sticky=constants.W)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        self._frame.grid_columnconfigure(1, weight=0)

        self._hide_error()


class WorkoutListView:
    """Näkymä, joka vastaa treenien listauksesta.
    """

    def __init__(self, root, workouts):
        """Luokan konstruktori, joka luo uuden treenien listausnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            workouts: Lista Workout-olioita, jotka näytetään näkymässä.
        """
        self._root = root
        self._workouts = workouts
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
    """Treenien poistamisesta vastaava näkymä."""

    def __init__(self, root, delete_return):
        """Luokan konstruktori, joka luo treenien poistamisnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            delete_return: Arvo, jota kutsutaan, kun treeni on poistettu onnistuneesti ja palataan listausnäkymään.
        """

        self._root = root
        self._frame = None
        self._delete_return = delete_return
        self._error_message = None
        self._error_label = None
        self._selected_workout = StringVar()

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_delete_workout(self):
        workout_str = self._selected_workout.get()
        if workout_str:
            try:
                # generoitu koodi alkaa
                content, date = workout_str.split(" - ")
                content = content.strip()
                date = date.strip()
                # generoitu koodi päättyy
                app_service.delete_one_workout(content, date)
                self._delete_return()
            except InvalidDate as error:
                self._error(str(error))
            except NoSuchWorkoutError as error:
                self._error(str(error))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

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

        workouts = app_service.get_user_workouts()
        workout_options = [
            f"{workout.content} - {workout.date}" for workout in workouts]

        self._selected_workout.set(workout_options[0])
        workout_dropdown = ttk.Combobox(
            master=self._frame,
            textvariable=self._selected_workout,
            values=workout_options
        )

        workout_dropdown.grid(row=1, column=0, padx=4,
                              pady=4, sticky=constants.W)

        delete_workout_button = ttk.Button(
            master=self._frame,
            text="Poista treeni",
            command=self._handle_delete_workout
        )

        workout_label.grid(row=1, column=0, padx=4, pady=4, sticky=constants.W)
        delete_workout_button.grid(
            row=3, column=0, padx=4, pady=4, sticky=constants.W)

        self._hide_error()


class WorkoutModifyView:
    """Treenien muokkaamisesta vastaava näkymä."""

    def __init__(self, root, modify_return):
        """Luokan konstruktori, joka luo treenien muokkaamisnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            modify_return: Arvo, jota kutsutaan, kun treeniä on muokattu onnistuneesti ja palataan listausnäkymään.
        """

        self._root = root
        self._frame = None
        self._modify_return = modify_return
        self._error_message = None
        self._error_label = None
        self._selected_workout = StringVar()
        self._new_content = StringVar()

        self._initialize()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_modify_workout(self):
        workout_str = self._selected_workout.get()
        new_content = self._new_content.get().lstrip()
        if len(new_content) > 100:
            self._error("Treenin sisältö liian pitkä")
            return
        if len(new_content.strip()) == 0:
            self._error("Treenin sisältö ei voi olla tyhjä")
            return
        if workout_str and new_content.strip():
            try:
                # generoitu koodi alkaa
                old_content, date = workout_str.split(" - ")
                old_content = old_content.strip()
                date = date.strip()
                # generoitu koodi päättyy
                app_service.modify_workout(old_content, new_content, date)
                self._modify_return()
            except InvalidDate as error:
                self._error(str(error))
            except NoSuchWorkoutError as error:
                self._error(str(error))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="black",
            background="red"
        )

        self._error_label.grid(row=4, column=0, padx=3, pady=3)

        heading_label = ttk.Label(
            master=self._frame, text="Mitä treeniä haluat muokata?")
        heading_label.grid(row=0, column=0, padx=4, pady=4, sticky=constants.W)

        workout_label = ttk.Label(
            master=self._frame, text="Muokattava treeni:")

        workouts = app_service.get_user_workouts()

        workout_options = [
            f"{workout.content} - {workout.date}" for workout in workouts]

        self._selected_workout.set(workout_options[0])
        workout_dropdown = ttk.Combobox(
            master=self._frame,
            textvariable=self._selected_workout,
            values=workout_options
        )

        content_label = ttk.Label(
            master=self._frame, text="Treenin uusi sisältö:")
        self._new_content = ttk.Entry(master=self._frame)

        modify_workout_button = ttk.Button(
            master=self._frame,
            text="Muokkaa treeniä",
            command=self._handle_modify_workout
        )

        workout_label.grid(row=1, column=0, padx=4, pady=4, sticky=constants.W)
        workout_dropdown.grid(row=1, column=1, padx=4,
                              pady=4, sticky=constants.W)
        content_label.grid(row=2, column=0, padx=4, pady=4, sticky=constants.W)
        self._new_content.grid(row=2, column=1, padx=4,
                               pady=4, sticky=constants.W)
        modify_workout_button.grid(
            row=3, column=0, padx=4, pady=4, sticky=constants.W)

        self._hide_error()
