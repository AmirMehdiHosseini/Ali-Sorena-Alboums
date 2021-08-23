from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from login           import Ui_MainWindow
from name_panel      import Ui_Panel
from loading         import Ui_Main_loading
from sign_up         import Ui_Sign_up
from artists_alboums import Ui_Alboums
import mysql.connector 


my_db = mysql.connector.connect(user = 'root',
                                password = '43694369',
                                host = '127.0.0.1',
                                database = 'account')

my_cursor = my_db.cursor()





# boro bara panel class besaz bad ino vsl kon
'''
class Alboums(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Alboums()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


'''

class Artists_names(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Panel()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.pushButton_back.clicked.connect(self.login)

    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    
    def login(self):
        self.login = Main_Login()
        self.login.show()
        self.close()





















class Main_Sign_up(QMainWindow):
    def __init__(self):


        QMainWindow.__init__(self)
        self.ui = Ui_Sign_up()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.lineEdit_username_signup.setPlaceholderText  ('                      Username' )
        self.ui.lineEdit_password_signup.setPlaceholderText  ('                      Password' )
        self.ui.lineEdit_password_signup_2.setPlaceholderText('               Confirm password')
        self.ui.pushButton_back_signup.clicked.connect(self.login)
        self.ui.pushButton_login.clicked.connect(self.sign_up)

    
    def sign_up(self):
        password , con_pass, username = self.ui.lineEdit_password_signup_2.text() , self.ui.lineEdit_password_signup.text(), self.ui.lineEdit_username_signup.text()
        

    
        if password == con_pass:
            my_cursor.execute('INSERT INTO info (username, password) VALUES (\'%s\', \'%s\');' %(username, password))
        
        
        my_db.commit()     

        self.login()



    def login(self):
        self.login2 = Main_Login()
        self.login2.show()
        self.close()


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    




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
        self.timer.start(10)


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

            self.Panel = Main_Login()
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


class Main_Login(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.pushButton_login.clicked.connect(self.LoginPanel)

        self.ui.lineEdit_username.setPlaceholderText('                      Username')
        self.ui.lineEdit_password.setPlaceholderText('                      Password')

        self.ui.pushButton_Register.clicked.connect(self.register)


    def register(self):
        self.sign_up = Main_Sign_up()
        self.sign_up.show()
        self.close()


    
    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def LoginPanel(self):
        user = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()


        if user == 'aa' and password == '11':
            
            self.paneluser = Artists_names()
            self.paneluser.show()
            self.close()

        else :
# ye massagebox bezar bara in o sign up eshtebah
            print('error')
            


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = MainLoading()
    sys.exit(app.exec_())


    
my_db.close()
