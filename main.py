import tkinter as tk                

class app(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        """
        The container holds all of the frames, the frame
        is then raised above the others with show_frame()
        """
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        """
        fancy way of creating the classes
        """
        self.frames = {}
        for F in (main_menu, typeracer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            #placing the frames in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("main_menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class main_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="game", command=lambda: controller.show_frame("typeracer"))
        button1.pack()


class typeracer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        
        button = tk.Button(self, text="menu", command=lambda: controller.show_frame("main_menu"))
        button.pack()




if __name__ == "__main__":
    app = app()
    app.mainloop()