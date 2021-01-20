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
        self.frame = tk.Frame(self.root)
        self.frame.pack()
    
        debug_print_button = tk.Button(self.frame, text="print", command= lambda: print(self.controller.getArray()))
        debug_print_button.pack(side=tk.LEFT)
        generate_button = tk.Button(self.frame, text="Generate", command=lambda: self.controller.generateNewArray(elem_num.get(), min_value_entry.get(), self.max_value_entry.get()))
        generate_button.pack(side=tk.LEFT)
        draw_button = tk.Button(self.frame, text="Draw", command=lambda: self.draw_array(self.controller.getArray()))
        draw_button.pack(side=tk.LEFT)
        algo = tk.StringVar(self.root)
        algo.set(algo_options[0])
        sort_button = tk.Button(self.frame, text="Sort",command=lambda: self.controller.sort(algo.get()))
        sort_button.pack(side=tk.LEFT)
        algo_menu = tk.OptionMenu(self.frame, algo, *algo_options)
        algo_menu.pack(side=tk.RIGHT)
        elem_num = tk.Scale(self.root, from_=10, to=1000)
        elem_num.pack()
        min_value_entry = tk.Entry(self.root)
        min_value_entry.pack()
        self.max_value_entry = tk.Entry(self.root)
        self.max_value_entry.pack()
        min_value_entry.insert(tk.END, 10)
        self.max_value_entry.insert(tk.END, 100)
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def show(self):
        self.root.mainloop()

    def draw_array(self, array, colours=[]):
        #clear the canvas
        self.canvas.delete('all')
        #little offset in order to make some space at the beginning and the end of the rectangles
        offset = 20
        #start x cordinate
        start_x = offset / 2
        rect_width = int((self.canvas_width - offset / 2) / len(array))
        if len(colours) == 0:
            colours = ['lightblue' for _ in range(len(array))]
        idx = 0
        for el in array:
            #max height is relative to the max value
            height = int(self.canvas_height * (el / int(self.max_value_entry.get())))
            self.canvas.create_rectangle(start_x, height, start_x + rect_width, self.canvas_height, fill=colours[idx])
            idx += 1
            start_x += rect_width
            self.frame.update_idletasks()