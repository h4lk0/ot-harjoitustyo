from tkinter import IntVar, StringVar, ttk

from entities.exercise import Exercise
from services.table_getter import TableGetter


class ExerciseView:

    def __init__(self, root, back_to_start, show_mc, show_fillin, show_fc):
        self._root = root
        self._handle_back_to_start = back_to_start
        self._handle_show_mc = show_mc
        self._handle_show_fillin = show_fillin
        self._handle_show_fc = show_fc
        self._frame = None
        self._table = None
        self._getter = TableGetter()

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_dropdown()
        self._initialize_buttons()

        self.pack()

    def _initialize_buttons(self):
        btn_mc = ttk.Button(master=self._frame, text="Multiple choice", command=self._handle_show_mc)
        btn2 = ttk.Button(master=self._frame, text="Fill in", command=self._handle_show_fillin)
        btn_fc = ttk.Button(master=self._frame, text="Flashcard", command=self._handle_show_fc)
        btn_back = ttk.Button(master=self._frame, text="Back", command=self._handle_back_to_start)

        btn_back.grid(row=3, column=0)
        btn_mc.grid(row=1, column=1)
        btn2.grid(row=1, column=2)
        btn_fc.grid(row=1, column=3)
        
    def _initialize_dropdown(self):
        label = ttk.Label(master=self._frame, text="Select list:")

        list_of_tables = self._getter.get_tables()
        self._listvar = StringVar()
        self._wordlist = ttk.Combobox(master=self._frame, textvariable=self._listvar)
        self._wordlist["values"] = list_of_tables
        self._wordlist.bind("<<ComboboxSelected>>", self._update)
        self._listvar.set("Nouns")

        self._wordlist.grid(row=0, column=1, columnspan=4)
        label.grid(row=1, column=0)

    def _update(self, event):
        self._table = self.get_wordlist()

    def get_wordlist(self):
        return self._wordlist.get()

    def pack(self):
        self._frame.pack()
        self._frame.lift()

    def destroy(self):
        self._frame.destroy()

class MultipleChoiceView:

    def __init__(self, root, handle_return, wordlist):
        self._root = root
        self._frame = None
        self._exercise = Exercise(wordlist)
        self._answer = None
        self._options = None
        self._handle_return = handle_return
        self._radiobuttons = []

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._question = ttk.Label(master=self._frame, text="")
        self._question.grid(row=0, column=2, columnspan=5)

        self._initialize_radiobuttons()
        self._initialize_buttons()

        self._result = ttk.Label(master=self._frame, text="")
        self._result.grid(row=3, column=1)

        self._new_exercise()
        self.pack()

    def _new_exercise(self):
        self._exercise.new_values()
        self._answer = self._exercise.get_answer()
        self._options = self._exercise.get_options()
        self._btn_next.state(("disabled",))
        self._btn_check.state(("!disabled",))
        self._update_values()
        self._sel.set(None)
        self._result["text"] = ""

    def _update_values(self):
        self._question["text"] = self._answer["kor"]
        for radio, option in zip(self._radiobuttons, self._options):
            radio["text"] = option["eng"]

    def _initialize_buttons(self):
        btn_back = ttk.Button(master=self._frame, text="Back", command=self._handle_return)
        self._btn_check = ttk.Button(master=self._frame, text="Check", command=self._check_answer)
        self._btn_next = ttk.Button(master=self._frame, text="Next", command=self._new_exercise)
        self._btn_next.state(("disabled",))
        self._btn_check.state(("disabled",))

        btn_back.grid(row=2, column=0)
        self._btn_check.grid(row=2, column=2)
        self._btn_next.grid(row=2, column=1)

    def _initialize_radiobuttons(self):
        self._sel = IntVar()
        for i in range(0,5):
            radio = ttk.Radiobutton(master=self._frame, text="", variable=self._sel, value=i)
            radio.grid(row=1, column=i)
            self._radiobuttons.append(radio)

    def _check_answer(self):
        attempt = self._radiobuttons[self._sel.get()]["text"]
        correct = self._exercise.check(attempt)
        self._btn_next.state(("!disabled",))
        self._btn_check.state(("disabled",))
        if correct:
            self._result["text"] = "Correct!"
        else:
            ans = self._answer["eng"]
            self._result["text"] = f"Wrong! Answer: {ans}"
        self._sel.set(None)

    def pack(self):
        self._frame.pack()
        self._frame.lift()

    def destroy(self):
        self._frame.destroy()

class FillInView:

    def __init__(self, root, handle_return, wordlist):
        self._root = root
        self._frame = None
        self._exercise = Exercise(wordlist)
        self._answer = None
        self._handle_return = handle_return

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._sv = StringVar()
        self._entry = ttk.Entry(master=self._frame, textvariable=self._sv)
        self._sv.trace_add("write", callback=self._able_check)

        self._label = ttk.Label(master=self._frame, text="")
        self._result = ttk.Label(master=self._frame, text="")
        txt = ttk.Label(master=self._frame, text="Answer:")
        self._initialize_buttons()

        self._label.grid(row=0, column=0)
        self._result.grid(row=2, column=0)
        txt.grid(row=1, column=0, sticky="e")
        self._entry.grid(row=1, column=1)

        self._new_exercise()

        self.pack()

    def _initialize_buttons(self):
        self._btn_check = ttk.Button(master=self._frame, text="Check", command=self._check_answer)
        self._btn_check.state(("disabled",))
        self._btn_next = ttk.Button(master=self._frame, text="Next", command=self._next)
        self._btn_next.state(("disabled",))
        btn_back = ttk.Button(master=self._frame, text="Back", command=self._handle_return)

        btn_back.grid(row=3, column=0)
        self._btn_next.grid(row=3, column=1)
        self._btn_check.grid(row=3, column=2)

    def _new_exercise(self):
        self._exercise.new_values()
        self._answer = self._exercise.get_answer()
        self._update_values()

    def _update_values(self):
        self._label["text"] = self._answer["kor"]

    def _check_answer(self):
        attempt = self._entry.get()
        correct = self._exercise.check(attempt)
        self._btn_next.state(("!disabled",))
        self._btn_check.state(("disabled",))
        if correct:
            self._result["text"] = "Correct!"
        else:
            ans = self._answer["eng"]
            self._result["text"] = f"Wrong! Answer: {ans}"
    
    def _able_check(self, var, index, mode):
        if len(self._sv.get()) > 0:
            self._btn_check.state(("!disabled",))
        else:
            self._btn_check.state(("disabled",))

    def _next(self):
        self._result["text"] = ""
        self._btn_check.state(("disabled",))
        self._btn_next.state(("disabled",))
        self._sv.set("")
        self._new_exercise()

    def pack(self):
        self._frame.pack()
        self._frame.lift()

    def destroy(self):
        self._frame.destroy()

class Flashcard:

    def __init__(self, root, handle_return, wordlist):
        self._root = root
        self._frame = None
        self._exercise = Exercise(wordlist)
        self._kor = None
        self._eng = None
        self._handle_return = handle_return
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._sv = StringVar()
        self._label = ttk.Label(master=self._frame, textvariable=self._sv)
        self._label.grid(row=0, column=0, columnspan=3)
        
        self._initialize_buttons()
        self._new_word()
        self.pack()

    def _initialize_buttons(self):
        btn_flip = ttk.Button(master=self._frame, text="Flip", command=self._flip)
        btn_flip.grid(row=1, column=1, columnspan=3)

        btn_back = ttk.Button(master=self._frame, text="Back", command=self._handle_return)
        btn_back.grid(row=3, column=1)

        btn_next = ttk.Button(master=self._frame, text="Next", command=self._new_word)
        btn_next.grid(row=2, column=1)

    def _new_word(self):
        self._exercise.new_values()
        word = self._exercise.get_answer()
        self._eng = word["eng"]
        self._kor = word["kor"]
        self._sv.set(self._kor)

    def _flip(self):
        if self._sv.get() == self._kor:
            self._sv.set(self._eng)
        else:
            self._sv.set(self._kor)

    def pack(self):
        self._frame.pack()
        self._frame.lift()

    def destroy(self):
        self._frame.destroy()


