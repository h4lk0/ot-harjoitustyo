from tkinter import Button, Tk, ttk
from start_view import StartView

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = StartView(self._root)
        self._exit()

    def _exit(self):
        exit_button = ttk.Button(master=self._root, text="Exit", command=quit)
        exit_button.pack(anchor="se")

window = Tk()
window.title("Language practice")
window.geometry("500x200")

ui = UI(window)

window.mainloop()
