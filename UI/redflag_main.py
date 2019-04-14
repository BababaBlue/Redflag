import self as self
from PySide2 import QtCore, QtGui, QtWidgets
import sys

from UI import redflag

k = redflag.Ui_MainWindow
k1 = k.setupUi


class MyApp(k1, QtWidgets.QMainWindow):

    def __int__(self):
        super(MyApp, self).__int__()
        self.setupUi(self)
        self.main_layout.addWidget(self.redflag)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qt_app = MyApp()
    qt_app.show()
    app.exec_()
