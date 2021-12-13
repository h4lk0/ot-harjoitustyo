from tkinter import Button, StringVar, Toplevel, ttk

class ListView:

    def __init__(self, root):
        self._root = root
        self._top = Toplevel(self._root)
        self._top.title("List management")

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._top, padding=5, borderwidth=2)
        exit_btn = ttk.Button(master=self._frame, text="Exit", command=self.destroy)
        self._create_new_list()
        self._select_from_dropdown_menu()

        exit_btn.grid(row=5, column=5, sticky="se")
        self._frame.pack()

    def _create_new_list(self):
        label1 = ttk.Label(master=self._frame, text="Create new list:")
        label2 = ttk.Label(master=self._frame, text="List name:")
        btn_new = ttk.Button(master=self._frame, text="Add")
        entry = ttk.Entry(master=self._frame)
        list_name = entry.get()

        label1.grid(row=0, column=0, columnspan=2)
        label2.grid(row=1, column=0)
        entry.grid(row=1, column=1)
        btn_new.grid(row=1, column=2)

    def _select_from_dropdown_menu(self):
        label = ttk.Label(master=self._frame, text="Select list:")
        
        list_of_tables = self._get_wordlists()
        self._listvar = StringVar()
        wordlist = ttk.Combobox(master=self._frame, textvariable=self._listvar)
        wordlist.bind("<<ComboboxSelected>>", self._show_edit_view)
        wordlist["values"] = list_of_tables

        label.grid(row=2, column=0)
        wordlist.grid(row=2, column=1)

    def _add_to_list(self):
        self._frame = ttk.Frame(master=self._top, padding=5, borderwidth=2)

    def _get_wordlists(self):
        pass

    def _handle_add_list(self, name):
        self._listvar.set(name)
        #lisää lista tietokantaan

    def destroy(self):
        self._top.destroy()
    
    def _show_edit_view(self):
        pass
