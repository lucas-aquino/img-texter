import tkinter


class App(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()


app = App(master = tkinter.Tk())


app.master.title("IMG Texter")
app.master.geometry("400x300")

def hello(nombre):
    print("Hi " + nombre)

boton = tkinter.Button(app, text = "Press Me", command = lambda: hello("Lucas"))
boton.pack()

app.mainloop()

