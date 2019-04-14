import self as self
from PySide2 import QtWidgets

from UI import redflag

import redflag

k = redflag.Ui_MainWindow.setupUi(self,Mainwindow)


class MyApp(k, QtWidgets.QMainWindow):

    def __int__(self):
        super(MyApp, self).__int__()
        self.setupUi(self)
        self.main_layout.addWidget(self.redflag)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qt_app = MyApp()
    qt_app.show()
    app.exec_()
