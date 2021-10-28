from os import name
import tkinter as tk
from tkinter import ttk
import tkinterDnD
from Texter import Texter
import pathlib


class App(tk.Frame):

    NAME = "IMG Texter"
    __title : str

    def __init__(self, master = tk.Tk(), title = "IMG Texter"):
        super().__init__(master)
        self.master = master
        self.setTitle(title = title)
        self.pack()

    def setTitle(self, title : str):
        self.__title = title
        self.master.title(self.__title)


def main():
    app = App()

    texter = Texter(str(pathlib.Path(__file__).parent.parent.resolve()) + "\\img-test\\text-test3.png")

    app.master.geometry("400x300")
    

    labelTexterView = tk.Label(app, text = texter.getText())

    boton = tk.Button(app, text = "Press Me", command = lambda: labelTexterView.pack())
    boton.pack()

    app.mainloop()


if __name__ == '__main__':
    main()
