import tkinter as tk

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
CANVAS_WIDTH = WINDOW_WIDTH - 200
CANVAS_HEIGHT = WINDOW_HEIGHT - 100

class View():
    def __init__(self):
        self.controller = None

    def init(self, controller):
        self.root = tk.Tk()
        self.root.title('Sorting Visualizer')
        self.root.geometry(str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT))
        if controller == None:
            raise Exception('controller cannot be none')
        self.controller = controller
    
        b = tk.Button(self.root, text="current array", command= lambda: print(self.controller.getArray()))
        b.pack()
        b2 = tk.Button(self.root, text="new", command=lambda: self.controller.generateNewArray(20))
        b2.pack()
        b3 = tk.Button(self.root, text="draw", command=lambda: self.draw_array(self.controller.getArray()))
        b3.pack()
        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
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
        rect_width = int((CANVAS_WIDTH - offset / 2) / len(array))
        for el in array:
            #max height is relative to the canvas size
            height = int(CANVAS_HEIGHT*el/1000)
            self.canvas.create_rectangle(start_x, height, start_x + rect_width, CANVAS_HEIGHT)
            start_x += rect_width

