from tkinter import ttk, Tk
from ui.ui import Ui

def main():
    window = Tk()
    window.title("Language practice")
    window.geometry("700x400")
    theme = ttk.Style()
    theme.theme_use("alt")

    Ui(window)
    theme.configure("main_frame", background="red")

    window.mainloop()

if __name__ == '__main__':
    main()
