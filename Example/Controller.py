from Example import View, Model

class Controller(object):
    def __init__(self):
        self.view = View()
        self.view.setPriceChanger(self.changePrice)
        self.model = Model()
        self.model.price.addCallback(self.priceChanged)
        self.view.run()
    def changePrice(self):
        self.model.calcPrice(int(self.view.getPrice()))
    def priceChanged(self, price):
        self.view.setPrice(price)

app = Controller()