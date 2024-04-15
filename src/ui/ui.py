from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.sign_up_view import SignUpView
from ui.workout_diary_view import WorkoutView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _destroy_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._destroy_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_workout_view,
            self._show_handle_sign_up_view
        )

        self._current_view.pack()

    def _show_handle_sign_up_view(self):
        self._destroy_current_view()

        self._current_view = SignUpView(
            self._root,
            self._show_workout_view,
            self._show_login_view
        )

    def _show_workout_view(self):
        self._destroy_current_view()

        self._current_view = WorkoutView(self._root, self._show_login_view)

        self._current_view.pack()


