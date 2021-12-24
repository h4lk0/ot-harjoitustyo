from tkinter import Button, Tk, ttk
from ui.start_view import StartView
from ui.excercise_view import ExerciseView, MultipleChoiceView, FillInView, Flashcard

class Ui:

    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._main_frame = ttk.Frame(master=self._root)
        self._exit_frame = ttk.Frame(master=self._root)

        self._main_frame.pack(anchor="center")
        self._exit_btn()
        self._exit_frame.pack(anchor="n")
        self._exit_frame.lower()

        self._start()

    def _start(self):
        self._show_start_view()

    def _exit_btn(self):
        exit_button = ttk.Button(master=self._exit_frame, text="Quit", command=quit)
        exit_button.pack(fill="x")

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
            
        self._current_view = None

    def _show_exercise_view(self):
        self._hide_current_view()
        self._current_view = ExerciseView(self._main_frame, self._show_start_view, self._show_multiple_choice, self._show_fillin, self._show_flashcard)
        self._current_view.pack()

    def _show_start_view(self):
        self._hide_current_view()
        self._current_view = StartView(self._main_frame, self._show_exercise_view)
        self._current_view.pack()

    def _show_multiple_choice(self):
        wordlist = self._current_view.get_wordlist()
        self._hide_current_view()
        self._current_view = MultipleChoiceView(self._main_frame, self._show_exercise_view, wordlist)
        self._current_view.pack()

    def _show_fillin(self):
        wordlist = self._current_view.get_wordlist()
        self._hide_current_view()
        self._current_view = FillInView(self._main_frame, self._show_exercise_view, wordlist)
        self._current_view.pack()

    def _show_flashcard(self):
        wordlist = self._current_view.get_wordlist()
        self._hide_current_view()
        self._current_view = Flashcard(self._main_frame, self._show_exercise_view, wordlist)