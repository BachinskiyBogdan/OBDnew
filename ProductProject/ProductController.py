from ProductProject import DeleteView, MainView, InsertView, LoginView

class ProductController(object):
    def __init__(self):
        self.main_view = MainView.Ui_MainWindow()
        self.insert_view = InsertView.Ui_MainWindow()
        self.delete_view = DeleteView.Ui_MainWindow()
        self.login_view = LoginView.Ui_MainWindow()
        self.login_view.run()

a = ProductController()