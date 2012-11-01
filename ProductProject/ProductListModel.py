import Observables.OriginObservable

class OriginListModel(object):
    origins_on_page = 10

    def __init__(self):
        self.origins = OriginObservable()[origins_on_page]
        self.repository = OriginRepository()

    def insert(self, new_origin):
        pass

    def update(self, new_origin):
        pass

    def delete(self, origin):
        pass