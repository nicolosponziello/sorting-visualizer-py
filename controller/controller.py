class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    
    def getRandomArray(self, size):
        return self.model.getRandomArray(size)