# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\project\redflag\UI\redflag.ui',
# licensing of 'D:\project\redflag\UI\redflag.ui' applies.
#
# Created: Sat Apr 13 12:30:39 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Arun/Downloads/LogoMakr_4Ox8H5.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_whole = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_whole.setGeometry(QtCore.QRect(0, 0, 801, 251))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tab_whole.setFont(font)
        self.tab_whole.setAcceptDrops(False)
        self.tab_whole.setAutoFillBackground(False)
        self.tab_whole.setObjectName("tab_whole")
        self.tab_sql = QtWidgets.QWidget()
        self.tab_sql.setObjectName("tab_sql")
        self.label_url_sql = QtWidgets.QLabel(self.tab_sql)
        self.label_url_sql.setGeometry(QtCore.QRect(50, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_url_sql.setFont(font)
        self.label_url_sql.setObjectName("label_url_sql")
        self.input_url_sql = QtWidgets.QLineEdit(self.tab_sql)
        self.input_url_sql.setGeometry(QtCore.QRect(90, 50, 251, 22))
        self.input_url_sql.setObjectName("input_url_sql")
        self.button_ok = QtWidgets.QPushButton(self.tab_sql)
        self.button_ok.setGeometry(QtCore.QRect(90, 120, 93, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(self.tab_sql)
        self.button_cancel.setGeometry(QtCore.QRect(250, 120, 93, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_cancel.setFont(font)
        self.button_cancel.setObjectName("button_cancel")
        self.textEdit_sql = QtWidgets.QTextEdit(self.tab_sql)
        self.textEdit_sql.setGeometry(QtCore.QRect(390, 0, 381, 221))
        self.textEdit_sql.setObjectName("textEdit_sql")
        self.tab_whole.addTab(self.tab_sql, "")
        self.tab_ddos = QtWidgets.QWidget()
        self.tab_ddos.setObjectName("tab_ddos")
        self.input_url_ddos = QtWidgets.QLineEdit(self.tab_ddos)
        self.input_url_ddos.setGeometry(QtCore.QRect(110, 40, 211, 22))
        self.input_url_ddos.setObjectName("input_url_ddos")
        self.label_url_ddos = QtWidgets.QLabel(self.tab_ddos)
        self.label_url_ddos.setGeometry(QtCore.QRect(60, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_url_ddos.setFont(font)
        self.label_url_ddos.setObjectName("label_url_ddos")
        self.button_ok_2 = QtWidgets.QPushButton(self.tab_ddos)
        self.button_ok_2.setGeometry(QtCore.QRect(110, 140, 71, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_ok_2.setFont(font)
        self.button_ok_2.setObjectName("button_ok_2")
        self.button_cancel_2 = QtWidgets.QPushButton(self.tab_ddos)
        self.button_cancel_2.setGeometry(QtCore.QRect(240, 140, 81, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_cancel_2.setFont(font)
        self.button_cancel_2.setObjectName("button_cancel_2")
        self.label_request_ddos = QtWidgets.QLabel(self.tab_ddos)
        self.label_request_ddos.setGeometry(QtCore.QRect(60, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_request_ddos.setFont(font)
        self.label_request_ddos.setObjectName("label_request_ddos")
        self.input_req_no = QtWidgets.QLineEdit(self.tab_ddos)
        self.input_req_no.setGeometry(QtCore.QRect(160, 90, 161, 22))
        self.input_req_no.setObjectName("input_req_no")
        self.textEdit_ddos = QtWidgets.QTextEdit(self.tab_ddos)
        self.textEdit_ddos.setGeometry(QtCore.QRect(390, 0, 381, 221))
        self.textEdit_ddos.setObjectName("textEdit_ddos")
        self.tab_whole.addTab(self.tab_ddos, "")
        self.tab_port = QtWidgets.QWidget()
        self.tab_port.setObjectName("tab_port")
        self.label_url_port = QtWidgets.QLabel(self.tab_port)
        self.label_url_port.setGeometry(QtCore.QRect(50, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_url_port.setFont(font)
        self.label_url_port.setObjectName("label_url_port")
        self.input_url_port = QtWidgets.QLineEdit(self.tab_port)
        self.input_url_port.setGeometry(QtCore.QRect(90, 50, 241, 22))
        self.input_url_port.setText("")
        self.input_url_port.setObjectName("input_url_port")
        self.button_ok_3 = QtWidgets.QPushButton(self.tab_port)
        self.button_ok_3.setGeometry(QtCore.QRect(90, 120, 93, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_ok_3.setFont(font)
        self.button_ok_3.setObjectName("button_ok_3")
        self.button_cancel_3 = QtWidgets.QPushButton(self.tab_port)
        self.button_cancel_3.setGeometry(QtCore.QRect(240, 120, 91, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_cancel_3.setFont(font)
        self.button_cancel_3.setObjectName("button_cancel_3")
        self.textEdit_port = QtWidgets.QTextEdit(self.tab_port)
        self.textEdit_port.setGeometry(QtCore.QRect(390, 0, 381, 221))
        self.textEdit_port.setObjectName("textEdit_port")
        self.tab_whole.addTab(self.tab_port, "")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(50, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.output_screen = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_screen.setGeometry(QtCore.QRect(50, 300, 711, 271))
        self.output_screen.setObjectName("output_screen")
        self.button_graph = QtWidgets.QPushButton(self.centralwidget)
        self.button_graph.setGeometry(QtCore.QRect(660, 260, 93, 28))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.button_graph.setFont(font)
        self.button_graph.setObjectName("button_graph")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_whole.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "RedFlag", None, -1))
        self.label_url_sql.setText(QtWidgets.QApplication.translate("MainWindow", "Url :", None, -1))
        self.button_ok.setText(QtWidgets.QApplication.translate("MainWindow", "Execute", None, -1))
        self.button_cancel.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.textEdit_sql.setHtml(QtWidgets.QApplication.translate("MainWindow",
                                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
                                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help?</p></body></html>",
                                                                   None, -1))
        self.tab_whole.setTabText(self.tab_whole.indexOf(self.tab_sql),
                                  QtWidgets.QApplication.translate("MainWindow", "SQL Injection", None, -1))
        self.label_url_ddos.setText(QtWidgets.QApplication.translate("MainWindow", "Url :", None, -1))
        self.button_ok_2.setText(QtWidgets.QApplication.translate("MainWindow", "Execute", None, -1))
        self.button_cancel_2.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.label_request_ddos.setText(QtWidgets.QApplication.translate("MainWindow", "Requests :", None, -1))
        self.textEdit_ddos.setHtml(QtWidgets.QApplication.translate("MainWindow",
                                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help?</p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                    None, -1))
        self.tab_whole.setTabText(self.tab_whole.indexOf(self.tab_ddos),
                                  QtWidgets.QApplication.translate("MainWindow", "DDOS", None, -1))
        self.label_url_port.setText(QtWidgets.QApplication.translate("MainWindow", "Url :", None, -1))
        self.button_ok_3.setText(QtWidgets.QApplication.translate("MainWindow", "Execute", None, -1))
        self.button_cancel_3.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.textEdit_port.setHtml(QtWidgets.QApplication.translate("MainWindow",
                                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help?</p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                    None, -1))
        self.tab_whole.setTabText(self.tab_whole.indexOf(self.tab_port),
                                  QtWidgets.QApplication.translate("MainWindow", "Port Scanner", None, -1))
        self.label_output.setText(QtWidgets.QApplication.translate("MainWindow", "Output :", None, -1))
        self.button_graph.setText(QtWidgets.QApplication.translate("MainWindow", "Graph", None, -1))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
