class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    
    def getArray(self):
        return self.model.get_array()

    def generateNewArray(self, size):
        self.model.generateRandomArray(size)

    def sort(self, method):
        self.model.sort(method)