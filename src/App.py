from os import name
import tkinter
from Texter import Texter
import pathlib


class App(tkinter.Frame):

    NAME = "IMG Texter"
    __title : str

    def __init__(self, master = tkinter.Tk(), title = "IMG Texter"):
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


    labelTexterView = tkinter.Label(app, text = texter.getText())

    boton = tkinter.Button(app, text = "Press Me", command = lambda: labelTexterView.pack())
    boton.pack()

    app.mainloop()


if __name__ == '__main__':
    main()
