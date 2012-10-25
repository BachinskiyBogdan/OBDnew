# coding: utf-8
import Tkinter as Tk
class View(Tk.Toplevel):
    def __init__(self):
        self.root = Tk.Tk()
        self.root.withdraw()
        Tk.Toplevel.__init__(self, self.root)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.priceValue = Tk.Label(self, text='Вартість: 0')
        self.priceValue.pack(side='top')
        self.priceEntry = Tk.Entry(self, text='0', width=10)
        self.priceEntry.pack(side='top')
        self.changeButton = Tk.Button(self, text='Change',width=8)
        self.changeButton.pack(side='top')
    def run(self):
        self.root.mainloop()
    def setPriceChanger(self, changer):
        self.changeButton.config(command=changer)
    def getPrice(self):
        return self.priceEntry.get()
    def setPrice(self, value):
        self.priceValue.config(text='Вартість: %f' % value)
