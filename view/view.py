import tkinter as tk

class View():
    def __init__(self):
        self.controller = None

    def init(self, controller):
        self.root = tk.Tk()
        self.root.title('Sorting Visualizer')
        self.root.geometry('800x600')
        if controller == None:
            raise Exception('controller cannot be none')
        self.controller = controller
    
        b = tk.Button(self.root, text="current array", command= lambda: print(self.controller.getArray()))
        b.pack()
        b2 = tk.Button(self.root, text="new", command=lambda: self.controller.generateNewArray(10))
        b2.pack()

    def show(self):
        self.root.mainloop()