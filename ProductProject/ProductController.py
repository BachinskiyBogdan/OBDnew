import MainView
import InsertView
import DeleteView
import LoginView
import ErrorView
import ProductModel as Model

product_model = Model.ProductModel()

class ProductController(object):
    def __init__(self):
        self.insert_view = InsertView.Ui_MainWindow()
        self.delete_view = DeleteView.Ui_MainWindow()
        self.main_view = MainView.Ui_MainWindow(self.insert_view, self.delete_view)
        self.error_view = ErrorView.Ui_MainWindow()
        self.login_view = LoginView.Ui_MainWindow(self.main_view, self.error_view)
        #self.login_view.run()
        self.main_view.run()

a = ProductController()