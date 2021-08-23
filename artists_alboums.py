# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'artists_alboums.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Alboums(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-3, 0, 451, 641))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f05053,stop:0.5 #ffd452, stop:1 #f05053);\n"
"\n"
"border-radius:12px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_mard_tanha = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_mard_tanha.setGeometry(QtCore.QRect(109, 130, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mard_tanha.setFont(font)
        self.pushButton_mard_tanha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_mard_tanha.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_mard_tanha.setObjectName("pushButton_mard_tanha")
        self.label_alboums = QtWidgets.QLabel(self.frame_2)
        self.label_alboums.setGeometry(QtCore.QRect(160, 10, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Dosis ExtraBold")
        font.setPointSize(30)
        self.label_alboums.setFont(font)
        self.label_alboums.setStyleSheet("background-color:none;\n"
"color:#f05053;")
        self.label_alboums.setObjectName("label_alboums")
        self.pushButton_avar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_avar.setGeometry(QtCore.QRect(109, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_avar.setFont(font)
        self.pushButton_avar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_avar.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_avar.setObjectName("pushButton_avar")
        self.pushButton_kavir = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_kavir.setGeometry(QtCore.QRect(109, 370, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kavir.setFont(font)
        self.pushButton_kavir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_kavir.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_kavir.setObjectName("pushButton_kavir")
        self.pushButton_negar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_negar.setGeometry(QtCore.QRect(109, 290, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_negar.setFont(font)
        self.pushButton_negar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_negar.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_negar.setObjectName("pushButton_negar")
        self.pushButton_gavazn = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_gavazn.setGeometry(QtCore.QRect(109, 450, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gavazn.setFont(font)
        self.pushButton_gavazn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_gavazn.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_gavazn.setObjectName("pushButton_gavazn")
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_exit.setGeometry(QtCore.QRect(394, 36, 18, 18))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
" background-color :#f05053;\n"
"  color:#ffd452;\n"
"} \n"
"")
        self.pushButton_exit.setText("")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_min = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_min.setGeometry(QtCore.QRect(395, 66, 18, 18))
        self.pushButton_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_min.setStyleSheet("QPushButton{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
" background-color :#f05053;\n"
"  color:#ffd452;\n"
"} \n"
"")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_back.setGeometry(QtCore.QRect(395, 96, 18, 18))
        self.pushButton_back.setStyleSheet("QPushButton{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
" background-color :#f05053;\n"
"  color:#ffd452;\n"
"} \n"
"")
        self.pushButton_back.setText("")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_single = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_single.setGeometry(QtCore.QRect(109, 530, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dosis")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_single.setFont(font)
        self.pushButton_single.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_single.setStyleSheet("QPushButton{\n"
"  background-color :#f05053;\n"
"  color:#ffd452;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color :#ffd452;\n"
"  color:#f05053;\n"
"}")
        self.pushButton_single.setObjectName("pushButton_single")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_exit.clicked.connect(MainWindow.close)
        self.pushButton_min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_mard_tanha.setText(_translate("MainWindow", "Marde-Tanha"))
        self.label_alboums.setText(_translate("MainWindow", "Alboums"))
        self.pushButton_avar.setText(_translate("MainWindow", "Aavar"))
        self.pushButton_kavir.setText(_translate("MainWindow", "Kavir"))
        self.pushButton_negar.setText(_translate("MainWindow", "Nagar"))
        self.pushButton_gavazn.setText(_translate("MainWindow", "Gavazn"))
        self.pushButton_single.setText(_translate("MainWindow", "Single-tracks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Alboums()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
