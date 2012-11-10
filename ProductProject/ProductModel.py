import ProductObservable as Observable
import ProductRepository as Repository

count_on_page = 10

class ProductModel(object):
    def __init__(self):
        self.products = []
        self.repository = Repository.ProductRepository()
        products = self.repository.read(0, count_on_page)
        i = 0
        for product in products:
            self.products[i] = Observable.ProductObservable()
            self.products[i].set(product)
            i += 1

    def insert(self, new_product):
        pass

    def update(self, new_product):
        pass

    def delete(self, product):
        pass