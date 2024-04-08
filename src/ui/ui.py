from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Sisäänkirjautuminen")
        username_label = ttk.Label(master=self._root, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root)

        button = ttk.Button(
            master=self._root,
            text="Kirjaudu",
        )

        x=2
        y=2

        heading_label.grid(columnspan=2, sticky=constants.W, padx=x, pady=y)
        username_label.grid(padx=x, pady=y)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        password_label.grid(padx=x, pady=y)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=x, pady=y)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

