from model import model
from controller import controller
from view import view

def main():
    m = model.Model()
    v = view.View()

    c = controller.Controller(v, m)
    v.init(c)

    v.show()

if __name__ == '__main__':
    main()
