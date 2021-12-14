from tkinter import ttk, Tk
from ui.ui import Ui

def main():
    window = Tk()
    window.title("Language practice")
    window.geometry("500x200")
    theme = ttk.Style()
    theme.theme_use("alt")

    Ui(window)

    window.mainloop()


if __name__ == '__main__':
    main()
