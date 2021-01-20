from model import model
from controller import controller
from view import view

WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1920

class MainApplication():
    def __init__(self):
        self.model = model.Model()
        self.view = view.View(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.controller = controller.Controller(self.view, self.model)
        self.view.init(self.controller)

    def launch(self):
        self.view.show()

if __name__ == '__main__':
    app = MainApplication()
    app.launch()
