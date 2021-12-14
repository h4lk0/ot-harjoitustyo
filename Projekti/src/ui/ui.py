from tkinter import Button, Tk, ttk
from ui.start_view import StartView

class Ui:

    def __init__(self, root):
        self._root = root
        self._current_view = StartView(self._root)
        self._message()
        self._exit()

    def _exit(self):
        exit_button = ttk.Button(master=self._root, text="Exit", command=quit)
        exit_button.pack(anchor="se")

    def _message(self):
        lbl = ttk.Label(master=self._root, text="HUOM! Refaktorointi käynnissä, 'Exercises' väliaikaisesti poissa käytöstä")
        lbl.pack()
