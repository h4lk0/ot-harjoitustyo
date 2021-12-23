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
        exit_btn = ttk.Button(master=self._frame, text="Exit", command=self.destroy)
        self._create_new_list()
        self._select_from_dropdown_menu()

        exit_btn.grid(row=11, column=5, sticky="se")
        self._frame.pack()

    def _create_new_list(self):
        label1 = ttk.Label(master=self._frame, text="Create new list:")
        label2 = ttk.Label(master=self._frame, text="List name:")
        entry = ttk.Entry(master=self._frame)
        btn_new = ttk.Button(master=self._frame, text="Add", command=lambda: self._add_new_wordlist(entry.get()))
        self._lbl_added = ttk.Label(master=self._frame, text="")

        label1.grid(row=0, column=0, columnspan=2)
        label2.grid(row=1, column=0)
        entry.grid(row=1, column=1)
        btn_new.grid(row=1, column=2)
        self._lbl_added.grid(row=1, column=3)

    def _select_from_dropdown_menu(self):
        label = ttk.Label(master=self._frame, text="Select list:")
        
        list_of_tables = self._get_wordlists()
        self._listvar = StringVar()
        self._wordlist = ttk.Combobox(master=self._frame, textvariable=self._listvar)
        self._wordlist.bind("<<ComboboxSelected>>", self._show_edit_view)
        self._wordlist["values"] = list_of_tables

        label.grid(row=2, column=0)
        self._wordlist.grid(row=2, column=1)

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
        passed = self._db.add_from_file(self._listvar.get(),file)

        if passed == False:
            self._lbl_added["text"] = "File contains invalid entries"
        else:
            self._lbl_added["text"] = "Words added successfully"

    def _add_wordlist_entry(self):
        eng = self._e.get()
        kor = self._k.get()
        table = self._listvar.get()
        passed = self._db.add_to_list(table, eng, kor)        

        if passed == 0:
            self._lbl_result["text"] = "Invalid entry 'Eng'"
            return

        if passed == -1:
            self._lbl_result["text"] = "Invalid entry 'Kor'"
            return

        else:
            self._lbl_result["text"] = "Successfully added to list"
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
        lbl_or = ttk.Label(master=self._frame, text="OR")
        self._lbl_result = ttk.Label(master=self._frame, text="")

        self._entry_list_name.insert(0, self._listvar.get())
        self._entry_list_name.config(state="readonly")

        btn_add.grid(row=4, column=0)
        lbl_eng.grid(row=3, column=1)
        lbl_kor.grid(row=3, column=2)
        lbl_wordlist.grid(row=3, column=3)

        self._entry_eng.grid(row=4, column=1)
        self._entry_kor.grid(row=4, column=2)
        self._entry_list_name.grid(row=4, column=3, padx=7)
        lbl_or.grid(row=5, column=0, columnspan=5)

        btn_from_file.grid(row=6, column=0, columnspan=5, sticky="n")
        self._lbl_result.grid(row=7, column=0, columnspan=5)
