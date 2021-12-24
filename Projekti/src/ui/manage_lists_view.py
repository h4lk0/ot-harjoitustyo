from services.database_methods import DatabaseMethods
from tkinter import filedialog, StringVar, Toplevel, ttk

class ListView:

    def __init__(self, root):
        self._root = root
        self._top = Toplevel(self._root)
        self._top.title("List management")
        self._list_name = None
        self._db = DatabaseMethods()

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._top, padding=5, borderwidth=2)
        back_btn = ttk.Button(master=self._frame, text="Back to menu", command=self.destroy)
        exit_btn = ttk.Button(master=self._frame, text="Quit", command=quit)
        self._create_new_list()
        self._select_from_dropdown_menu()

        exit_btn.grid(row=11, column=5, sticky="w")
        back_btn.grid(row=11, column=0, sticky="e")
        self._frame.pack()

    def _create_new_list(self):
        label2 = ttk.Label(master=self._frame, text="New list:")
        entry = ttk.Entry(master=self._frame)
        btn_new = ttk.Button(master=self._frame, text="Create", command=lambda: self._add_new_wordlist(entry.get()))
        self._lbl_added = ttk.Label(master=self._frame, text="")

        label2.grid(row=1, column=0, sticky="e", padx=1, pady=3)
        entry.grid(row=1, column=1, pady=3)
        btn_new.grid(row=1, column=2, sticky="w", padx=1, pady=3)
        self._lbl_added.grid(row=0, column=1, sticky="n")

    def _select_from_dropdown_menu(self):
        label = ttk.Label(master=self._frame, text="Select list:")
        
        list_of_tables = self._get_wordlists()
        self._listvar = StringVar()
        self._wordlist = ttk.Combobox(master=self._frame, textvariable=self._listvar)
        self._wordlist.bind("<<ComboboxSelected>>", self._show_edit_view)
        self._wordlist["values"] = list_of_tables

        label.grid(row=2, column=0, sticky="e", padx=1, pady=5)
        self._wordlist.grid(row=2, column=1, pady=2, sticky="e")

    def _add_new_wordlist(self, name):
        passed = self._db.create_new_table(name)
        if not passed:
            self._lbl_added["text"] = "List already exists!"
        if passed:
            self._lbl_added["text"] = "List created successfully!"
            self._update_combobox()

    def _update_combobox(self):
        list = self._get_wordlists()
        self._wordlist["values"] = list

    def _get_wordlists(self):
        table_names = self._db.get_table_names()
        return table_names

    def _add_from_file(self):
        file = filedialog.askopenfilename(filetypes=((".csv","*.csv"),))
        if file:
            passed = self._db.add_from_file(self._listvar.get(),file)
        else:
            return

        if not passed:
            self._lbl_result["text"] = "File contains invalid entries!"
        else:
            self._lbl_result["text"] = "Words added successfully!"

    def _add_wordlist_entry(self):
        eng = self._e.get()
        kor = self._k.get()
        table = self._listvar.get()
        passed = self._db.add_to_list(table, eng, kor)        

        if passed == 0:
            self._lbl_result["text"] = "INVALID ENTRY 'ENG'"
            return

        if passed == -1:
            self._lbl_result["text"] = "INVALID ENTRY 'KOR'"
            return

        else:
            self._lbl_result["text"] = "WORD ADDED TO LIST"
            self._e.set("")
            self._k.set("")
            return

    def destroy(self):
        self._top.destroy()
    
    def _show_edit_view(self, event):
        lbl_eng = ttk.Label(master=self._frame, text="ENG")
        lbl_kor = ttk.Label(master=self._frame, text="KOR")
        lbl_wordlist = ttk.Label(master=self._frame, text="Wordlist")
        btn_add = ttk.Button(master=self._frame, text="Add to list", command=self._add_wordlist_entry)
        self._k = StringVar()
        self._e = StringVar()
        self._entry_eng = ttk.Entry(master=self._frame, textvariable=self._e)
        self._entry_kor = ttk.Entry(master=self._frame, textvariable=self._k)
        self._entry_list_name = ttk.Entry(master=self._frame)
        btn_from_file = ttk.Button(master=self._frame, text="Add from .csv", command=self._add_from_file)
        lbl_or = ttk.Label(master=self._frame, text="or")
        self._lbl_result = ttk.Label(master=self._frame, text="")

        self._entry_list_name.insert(0, self._listvar.get())
        self._entry_list_name.config(state="readonly")

        btn_add.grid(row=4, column=0)
        lbl_eng.grid(row=3, column=1, pady=1)
        lbl_kor.grid(row=3, column=2)
        lbl_wordlist.grid(row=3, column=3)

        self._entry_eng.grid(row=4, column=1)
        self._entry_kor.grid(row=4, column=2)
        self._entry_list_name.grid(row=4, column=3, padx=7)
        lbl_or.grid(row=5, column=0, columnspan=5)

        btn_from_file.grid(row=6, column=0, columnspan=5, sticky="n")
        self._lbl_result.grid(row=7, column=0, columnspan=5, pady=10)
