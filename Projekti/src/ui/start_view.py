from ui.manage_lists_view import ListView
from tkinter import Text, ttk

class StartView:

    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, padding=5, borderwidth=2)
        self._welcome_text()
        self._text_box()

        button1 = ttk.Button(master=self._frame, text="Exercises")
        button2 = ttk.Button(master=self._frame, text="Manage lists", command= lambda: ListView(self._root))

        button1.grid(row=2, column=0, padx=15, pady=5)
        button2.grid(row=2, column=2, padx=15, pady=5)
        self.pack()

    def _welcome_text(self):
        label = ttk.Label(master=self._frame, text="WELCOME!")
        label.grid(row=0, sticky="n", columnspan=3)

    def _text_box(self):
        message = "Click 'Exercises' to choose exercise or manage wordlists with 'Manage lists'"
        text_box = Text(self._frame, height=3, width=40, borderwidth=3)
        text_box.insert('end', message)
        text_box.config(state="disabled")
        text_box.grid(row=1, column=0, columnspan=3, sticky="n")

    def pack(self):
        self._frame.pack(anchor="c")

    def destroy(self):
        self._frame.destroy()
