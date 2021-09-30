import tkinter


class App(tkinter.Frame):
    def __init__(self, master, title = "IMG Texter"):
        super().__init__(master)
        self.master = master
        self.setTitle(title = title)
        self.pack()

    def setTitle(self, title : str):
        self.master.title(title)


app = App(master = tkinter.Tk())


#app.setTitle(title = "IMG Texter")

#app.master.title("IMG Texter")
app.master.geometry("400x300")

def hello(nombre):
    print("Hi " + nombre)

boton = tkinter.Button(app, text = "Press Me", command = lambda: hello("Lucas"))
boton.pack()

app.mainloop()

