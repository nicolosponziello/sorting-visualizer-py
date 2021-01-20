from algorithms import Algorithms
import tkinter as tk

algo_options = [el.name for el in Algorithms]
class View():
    def __init__(self, width, height):
        self.controller = None
        self.width = width
        self.height = height
        self.canvas_width = width - 200
        self.canvas_height = height - 220

    def init(self, controller):
        self.root = tk.Tk()
        self.root.title('Sorting Visualizer')
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        if controller == None:
            raise Exception('controller cannot be none')
        self.controller = controller
    
        b = tk.Button(self.root, text="current array", command= lambda: print(self.controller.getArray()))
        b.pack()
        b2 = tk.Button(self.root, text="new", command=lambda: self.controller.generateNewArray(elem_num.get(), min_value.get(), max_value.get()))
        b2.pack()
        b3 = tk.Button(self.root, text="draw", command=lambda: self.draw_array(self.controller.getArray()))
        b3.pack()
        b4 = tk.Button(self.root, text="sort", command=lambda: self.controller.sort(var.get()))
        b4.pack()
        var = tk.StringVar(self.root)
        algo_select = tk.OptionMenu(self.root, var, *algo_options)
        algo_select.pack()
        elem_num = tk.Scale(self.root, from_=10, to=1000)
        elem_num.pack()
        min_value = tk.Entry(self.root)
        min_value.pack()
        max_value = tk.Entry(self.root)
        max_value.pack()
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def show(self):
        self.root.mainloop()

    def draw_array(self, array):
        #clear the canvas
        self.canvas.delete('all')
        #little offset in order to make some space at the beginning and the end of the rectangles
        offset = 20
        #start x cordinate
        start_x = offset / 2
        rect_width = int((self.canvas_width - offset / 2) / len(array))
        for el in array:
            #max height is relative to the canvas size
            height = int(self.canvas_height*el/1000)
            self.canvas.create_rectangle(start_x, height, start_x + rect_width, self.canvas_height)
            start_x += rect_width