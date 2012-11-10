class ProductObservable(object):
    def __init__(self, value=None):
        self.value = value
        self.callbacks = []

    def add_callback(self, func):
        self.callbacks.append(func)

    def set(self, value):
        self.value = value
        for func in self.callbacks:
            func(self.value)