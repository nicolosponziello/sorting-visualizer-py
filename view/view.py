from tkinter.constants import HORIZONTAL, LEFT
from algorithms import Algorithms
import tkinter as tk

algo_options = [el.name for el in Algorithms]
class View():
    def __init__(self, width, height):
        self.controller = None
        self.width = width
        self.height = height
        self.canvas_width = width - 0.2 * width
        self.canvas_height = height - 0.3 * height

    def generateAndDraw(self, size, min, max):
        self.controller.generateNewArray(size, min, max)
        self.draw_array(self.controller.getArray())

    def init(self, controller):
        self.root = tk.Tk()
        self.root.title('Sorting Visualizer')
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        
        if controller == None:
            raise Exception('controller cannot be none')
        self.controller = controller
        self.frame = tk.Frame(self.root, relief=tk.RAISED)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(self.frame)
        self.input_frame.pack()
    
        #buttons 
        generate_button = tk.Button(self.input_frame, text="Generate", command=lambda: self.generateAndDraw(elem_num.get(), min_value_entry.get(), self.max_value_entry.get()))
        generate_button.pack(side=tk.LEFT)
        
        algo = tk.StringVar(self.root)
        algo.set(algo_options[0])
        
        sort_button = tk.Button(self.input_frame, text="Sort",command=lambda: self.controller.sort(algo.get(), speed_selector.get()))
        sort_button.pack(side=tk.LEFT)
        
        #menu
        algo_menu = tk.OptionMenu(self.input_frame, algo, *algo_options)
        algo_menu.pack(side=LEFT)
        
        #elem config
        elem_num = tk.Scale(self.input_frame, from_=10, to=150, orient=tk.HORIZONTAL, label="Elements:", length=200)
        elem_num.pack(side=LEFT)
       
        min_value_label = tk.Label(self.input_frame, text="Min Value:")
        min_value_label.pack(side=LEFT)
        min_value_entry = tk.Entry(self.input_frame)
        min_value_entry.pack(side=LEFT)
       
        max_value_label = tk.Label(self.input_frame, text="Max Value: ")
        max_value_label.pack(side=LEFT)
        self.max_value_entry = tk.Entry(self.input_frame)
        self.max_value_entry.pack(side=LEFT)

        #speed
        speed_selector = tk.Scale(self.input_frame, from_=0.1, to=1, orient=HORIZONTAL, label="Speed:", length=150, resolution=0.1)
        speed_selector.set(0.5)
        speed_selector.pack(side=LEFT)


        min_value_entry.insert(tk.END, 10)
        self.max_value_entry.insert(tk.END, 100)

        #canvas
        self.canvas = tk.Canvas(self.frame, width=self.canvas_width, height=self.canvas_height)
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