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
    
        b = tk.Button(self.root, text="test", command= lambda: print(self.controller.getRandomArray(10)))
        b.pack()

    def show(self):
        self.root.mainloop()