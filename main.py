from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from login           import Ui_MainWindow
from panel           import Ui_Panel
from loading         import Ui_Main_loading

 
Counter = 0


class MainLoading(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Main_loading()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(30)


        self.show()


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def progress(self):
        global Counter
        self.ui.progressBar.setValue(Counter)

        if Counter > 100:
            self.timer.stop()

            self.Panel = RootMain()
            self.Panel.show()

            self.close()

        Counter += 1
        

        if Counter >= 50 :
            self.ui.progressBar.setStyleSheet("QProgressBar::chunk{\n"
"  border-radius:15px;\n"
"  background-color: #ffd452;\n"
"}\n"
"QProgressBar{\n"
"  background-color:#f05053;\n"
"  color:#f05053;\n"
"  border-style: none;\n"
"  border-radius:15px;\n"
"  text-align: center;\n"
"  height :50px;\n"
"  \n"
"}")



class Panel(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Panel()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


class RootMain(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.pushButton_login.clicked.connect(self.LoginPanel)


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def LoginPanel(self):
        user = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()


        if user == 'admin' and password == '123456':
            
            self.paneluser = Panel()
            self.paneluser.show()
            self.close()

        else :

            print('error')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = MainLoading()
    sys.exit(app.exec_())