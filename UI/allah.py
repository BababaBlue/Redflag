from PySide2 import QtWidgets,QtCore ,QtGui
from UI import redflag
k=redflag.Ui_MainWindow
k1=k.tf()
print(k1)

if k==1:
	print("allocated")
	
else:
	print ("not allocated")
""" COmmneted for now
class MyApp(k.UI.re, Qk.tWidgets.QMainWindow):
    def __int__(self):
        super(MyApp, self).__int__()
       # self.setupUi(self)
        self.main_layout.addWidget(self.redflag)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qt_app = MyApp()
    qt_app.show()
    app.exec_()
"""
