class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    
    def getArray(self):
        return self.model.get_array()

    def generateNewArray(self, size, min, max):
        try:
            min = int(min)
        except:
            min = 10
        try:
            max = int(max)
        except:
            max = 100
        self.model.generateRandomArray(size, min, max)

    def update_view(self, array, colors):
        self.view.draw_array(array, colors)

    def sort(self, method):
        self.model.sort(method, self.update_view)