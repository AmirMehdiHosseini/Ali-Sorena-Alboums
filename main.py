from PyQt5.QtWidgets   import *
from PyQt5.QtCore      import *
from login             import Ui_MainWindow
from name_panel        import Ui_Panel
from loading           import Ui_Main_loading
from sign_up           import Ui_Sign_up
from artists_alboums   import Ui_Alboums
from marde_tanha       import *
from Aavar             import *
from Negar             import *
from Kavir             import *
from Gavazn            import *
from Gharibe_nisti     import Ui_GharibeNisti
from Beshnas           import Ui_Beshnas
from Taghsir           import Ui_Taghsir
from Masti             import Ui_Masti
from mysql.connector   import connect
from Zendegi           import Ui_Zendegi














my_db = connect(user = 'root',
                password = '43694369',
                host = '127.0.0.1',
                database = 'account')


my_cursor = my_db.cursor()




class Cut(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Cut()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()

























class Dashte(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Dashte()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()




























class Asayeshgah(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Asayeshgah()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()


























class sixteen(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_16()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()


























class NaMimiram(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_NaMimiram()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()


























class Pelikan(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Pelikan()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
























class Istgah(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Istgah()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
























class Gavazn_track(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Gavazn_track()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()



























class Laghzesh(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Laghzesh()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
























class Ghalb(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Ghalb()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()




























class Bad_pichid(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Bad_pichid()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()





















class Raghs(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Raghs()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()























class Birahe(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Birahe()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
























class Goriz(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Goriz()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
































class Dar(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Daar()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()























class Nakhoda(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Nakhoda()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()
























class Harkat(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Harkat()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Gavazn()
        self.back2.show()
        self.close()




























class Nafir(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Nafir()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()
























class Poshte(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Poshte()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()


























class Maryam(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Maryam()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()


























class Tatre(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Tatre()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()





























class Teryagh(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Teryagh()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()

























class Gonjeshkaka(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Gonjeshkaka()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()





























class Kavir_track(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Kavir_track()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Kavir()
        self.back2.show()
        self.close()



























class Marg(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Marg()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()

























class Toofan(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Toofan()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()






























class Toorbin(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Toorbin()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()


























class Pak(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Pak()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()



























class Tark(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Tark()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()



























class Atash(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Atash()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()


























class Morphin(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Morphin()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()




























class Jari(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Jari()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()

























class Keshti(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Keshti()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()
























class Naghsh(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Naghsh()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()


























class Negar_track(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Negar_track()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()

























class Berim(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Berim()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()






















class Tavalod(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Tavalod()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Negar()
        self.back2.show()
        self.close()

























class Nemitarsam(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Nemitarsam()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()




















class Shorou(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Shorou()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()






















class Majnoun(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Majnoun()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()


































class DoShab(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Doshab()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()























class Atal(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Atal()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()



























class BaMan(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Ba_Man()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()





















class Avar_track(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Avar_track()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()














class Bache(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Bache()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Aavar()
        self.back2.show()
        self.close()















class Bad(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Bad()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()



























class Vaghte(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Vaghte()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()



























class Khake(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Khake()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()



























class Haf(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Haf()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()
































class Doel(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Doel()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()





















class Zendegi(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Zendegi()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()






























class Masti(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Masti()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()
































class Taghsir(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Taghsir()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()






























class Beshnas(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Beshnas()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_max.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()


























class GharibeNisti(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_GharibeNisti()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_max.clicked.connect(self.back)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = MardeTanha()
        self.back2.show()
        self.close()























class Gavazn(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Gavazn()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_Harkat.clicked.connect(self.harkat)
        self.ui.pushButton_nakhoda.clicked.connect(self.nakhoda)
        self.ui.pushButton_daar.clicked.connect(self.daar)
        self.ui.pushButton_goriz.clicked.connect(self.goriz)
        self.ui.pushButton_birahe.clicked.connect(self.birahe)
        self.ui.pushButton_raghs.clicked.connect(self.raghs)
        self.ui.pushButton_bad_pichid.clicked.connect(self.bad_pichid)
        self.ui.pushButton_ghalbhaye.clicked.connect(self.ghalb)
        self.ui.pushButtoon_laghzeshh.clicked.connect(self.laghzesh)
        self.ui.pushButton_gavazn.clicked.connect(self.gavazn)
        self.ui.pushButton_istgah.clicked.connect(self.istgah)
        self.ui.pushButton_pelikan.clicked.connect(self.pelikan)
        self.ui.pushButton_na_mimiram.clicked.connect(self.namimiram)
        self.ui.pushButton_sixteen.clicked.connect(self.sixteen)
        self.ui.pushButton_asayeshgah.clicked.connect(self.asayeshgah)
        self.ui.pushButton_dashte.clicked.connect(self.dashte)
        self.ui.pushButtoon_cut.clicked.connect(self.cut)



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def back(self):
        self.back2 = Alboums()
        self.back2.show()
        self.close()



    def harkat(self):
        self.panel2 = Harkat()
        self.panel2.show()
        self.close()


    def nakhoda(self):
        self.panel2 = Nakhoda()
        self.panel2.show()
        self.close()


    def daar(self):
        self.panel2 = Dar()
        self.panel2.show()
        self.close()


    def goriz(self):
        self.panel2 = Goriz()
        self.panel2.show()
        self.close()



    def birahe(self):
        self.panel2 = Birahe()
        self.panel2.show()
        self.close()



    def raghs(self):
        self.panel2 = Raghs()
        self.panel2.show()
        self.close()



    def bad_pichid(self):
        self.panel2 = Bad_pichid()
        self.panel2.show()
        self.close()




    def ghalb(self):
        self.panel2 = Ghalb()
        self.panel2.show()
        self.close()


    def laghzesh(self):
        self.panel2 = Laghzesh()
        self.panel2.show()
        self.close()



    def gavazn(self):
        self.panel2 = Gavazn_track()
        self.panel2.show()
        self.close()



    def istgah(self):
        self.panel2 = Istgah()
        self.panel2.show()
        self.close()



    def pelikan(self):
        self.panel2 = Pelikan()
        self.panel2.show()
        self.close()




    def sixteen(self):
        self.panel2 = sixteen()
        self.panel2.show()
        self.close()



    def namimiram(self):
        self.panel2 = NaMimiram()
        self.panel2.show()
        self.close()



    def asayeshgah(self):
        self.panel2 = Asayeshgah()
        self.panel2.show()
        self.close()



    def dashte(self):
        self.panel2 = Dashte()
        self.panel2.show()
        self.close()



    def cut(self):
        self.panel2 = Cut()
        self.panel2.show()
        self.close()























class Kavir(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Kavir()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_kavir.clicked.connect(self.kavir)
        self.ui.pushButton_gonjeshkaka.clicked.connect(self.gonjeshkaka)
        self.ui.pushButton_Teryagh.clicked.connect(self.teryagh)
        self.ui.pushButton_tatre.clicked.connect(self.tatre)
        self.ui.pushButton_Maryam.clicked.connect(self.maryam)
        self.ui.pushButton_poshte.clicked.connect(self.poshte)
        self.ui.pushButtoon_nafir.clicked.connect(self.nafir)


    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def back(self):
        self.back2 = Alboums()
        self.back2.show()
        self.close()





    def kavir(self):
        self.panel2 = Kavir_track()
        self.panel2.show()
        self.close()


    def gonjeshkaka(self):
        self.panel2 = Gonjeshkaka()
        self.panel2.show()
        self.close()


    def teryagh(self):
        self.panel2 = Teryagh()
        self.panel2.show()
        self.close()


    def tatre(self):
        self.panel2 = Tatre()
        self.panel2.show()
        self.close()



    def maryam(self):
        self.panel2 = Maryam()
        self.panel2.show()
        self.close()



    def poshte(self):
        self.panel2 = Poshte()
        self.panel2.show()
        self.close()



    def nafir(self):
        self.panel2 = Nafir()
        self.panel2.show()
        self.close()


































class Negar(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Negar()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_tavalod.clicked.connect(self.tavalod)
        self.ui.pushButton_berim.clicked.connect(self.berim)
        self.ui.pushButton_nagar.clicked.connect(self.Negar)
        self.ui.pushButton_naghsh.clicked.connect(self.Naghsh)
        self.ui.pushButton_keshti.clicked.connect(self.Keshti)
        self.ui.pushButton_jari.clicked.connect(self.jari)
        self.ui.pushButtoon_morphin.clicked.connect(self.morphin)
        self.ui.pushButton_atash.clicked.connect(self.atash)
        self.ui.pushButton_tark.clicked.connect(self.tark)
        self.ui.pushButton_paak.clicked.connect(self.pak)
        self.ui.pushButton_toorbin.clicked.connect(self.Toorbin)
        self.ui.pushButton_toofan.clicked.connect(self.Toofan)
        self.ui.pushButton_marg.clicked.connect(self.marg)






    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def back(self):
        self.back2 = Alboums()
        self.back2.show()
        self.close()




    def tavalod(self):
        self.panel2 = Tavalod()
        self.panel2.show()
        self.close()


    def berim(self):
        self.panel2 = Berim()
        self.panel2.show()
        self.close()


    def Negar(self):
        self.panel2 = Negar_track()
        self.panel2.show()
        self.close()


    def Naghsh(self):
        self.panel2 = Naghsh()
        self.panel2.show()
        self.close()



    def Keshti(self):
        self.panel2 = Keshti()
        self.panel2.show()
        self.close()



    def jari(self):
        self.panel2 = Jari()
        self.panel2.show()
        self.close()



    def morphin(self):
        self.panel2 = Morphin()
        self.panel2.show()
        self.close()




    def atash(self):
        self.panel2 = Atash()
        self.panel2.show()
        self.close()


    def tark(self):
        self.panel2 = Tark()
        self.panel2.show()
        self.close()



    def pak(self):
        self.panel2 = Pak()
        self.panel2.show()
        self.close()



    def Toorbin(self):
        self.panel2 = Toorbin()
        self.panel2.show()
        self.close()



    def Toofan(self):
        self.panel2 = Toofan()
        self.panel2.show()
        self.close()




    def marg(self):
        self.panel2 = Marg()
        self.panel2.show()
        self.close()


















class Aavar(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Aavar()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_bachat.clicked.connect(self.bache)
        self.ui.pushButton_nemitarsam.clicked.connect(self.nemitarsam)
        self.ui.pushButton_shorou.clicked.connect(self.Shorou)
        self.ui.pushButton_majnoun.clicked.connect(self.majnoun)
        self.ui.pushButton_doshab.clicked.connect(self.doshab)
        self.ui.pushButton_atal.clicked.connect(self.atal)
        self.ui.pushButtoon_baman.clicked.connect(self.ba_man)
        self.ui.pushButton_avar.clicked.connect(self.avar_track)







    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def back(self):
        self.back2 = Alboums()
        self.back2.show()
        self.close()


    def bache(self):
        self.panel2 = Bache()
        self.panel2.show()
        self.close()


    def majnoun(self):
        self.panel2 = Majnoun()
        self.panel2.show()
        self.close()


    def nemitarsam(self):
        self.panel2 = Nemitarsam()
        self.panel2.show()
        self.close()


    def Shorou(self):
        self.panel2 = Shorou()
        self.panel2.show()
        self.close()



    def doshab(self):
        self.panel2 = DoShab()
        self.panel2.show()
        self.close()



    def atal(self):
        self.panel2 = Atal()
        self.panel2.show()
        self.close()



    def ba_man(self):
        self.panel2 = BaMan()
        self.panel2.show()
        self.close()




    def avar_track(self):
        self.panel2 = Avar_track()
        self.panel2.show()
        self.close()

























class MardeTanha(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Marde_Tanha()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_gharibe.clicked.connect(self.gharibe)
        self.ui.pushButton_beshnas.clicked.connect(self.beshnas)
        self.ui.pushButton_Taghsir.clicked.connect(self.taghsir)
        self.ui.pushButton_Masti.clicked.connect(self.masti)
        self.ui.pushButton_zendegi.clicked.connect(self.zendegi)
        self.ui.pushButton_doel.clicked.connect(self.doel)
        self.ui.pushButtoon_Haf.clicked.connect(self.haf)
        self.ui.pushButton_Khake.clicked.connect(self.khake)
        self.ui.pushButton_Vaghte.clicked.connect(self.vaghte)
        self.ui.pushButton_bad.clicked.connect(self.bad)




    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()


    def back(self):
        self.back2 = Alboums()
        self.back2.show()
        self.close()

    def gharibe(self):
        self.gharibe2 = GharibeNisti()
        self.gharibe2.show()
        self.close()



    def beshnas(self):
        self.beshnas2 = Beshnas()
        self.beshnas2.show()
        self.close()


    def taghsir(self):
        self.taghsir2 = Taghsir()
        self.taghsir2.show()
        self.close()


    def masti(self):
        self.masti2 = Masti()
        self.masti2.show()
        self.close()


    def zendegi(self):
        self.zendegi2 = Zendegi()
        self.zendegi2.show()
        self.close()


    def doel(self):
        self.doel2 = Doel()
        self.doel2.show()
        self.close()


    def haf(self):
        self.haf2 = Haf()
        self.haf2.show()
        self.close()


    def khake(self):
        self.khake2 = Khake()
        self.khake2.show()
        self.close()



    def vaghte(self):
        self.vaghte2 = Vaghte()
        self.vaghte2.show()
        self.close()




    def bad(self):
        self.bad2 = Bad()
        self.bad2.show()
        self.close()





















class Alboums(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Alboums()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_mard_tanha.clicked.connect(self.marde_tanha)
        self.ui.pushButton_avar.clicked.connect(self.aavar)
        self.ui.pushButton_negar.clicked.connect(self.negar)
        self.ui.pushButton_kavir.clicked.connect(self.kavir) 
        self.ui.pushButton_gavazn.clicked.connect(self.gavazn)



    def aavar(self):
        self.aavar2 = Aavar()
        self.aavar2.show()
        self.close()


    def kavir(self):
        self.kavir2 = Kavir()
        self.kavir2.show()
        self.close()


    def negar(self):
        self.negar2 = Negar()
        self.negar2.show()
        self.close()


    def gavazn(self):
        self.gavazn2 = Gavazn()
        self.gavazn2.show()
        self.close()



    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def back(self):
        self.back2 = Artists_names()
        self.back2.show()
        self.close()

    def marde_tanha(self):
        self.marde_tanha2 = MardeTanha()
        self.marde_tanha2.show()
        self.close()






























class Artists_names(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Panel()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.pushButton_back.clicked.connect(self.login)
        self.ui.pushButton_sorena.clicked.connect(self.alboums)

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

    def alboums(self):
        self.alboums2 = Alboums()
        self.alboums2.show()
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
            self.login()
            my_db.commit()   


        else:
            msg = QMessageBox.information(
                self,
                'Error',
                "Password dosn't match confirmation !",
                QMessageBox.Ok
            )
        
          

        



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


'''
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
'''    



































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

        my_cursor.execute('select * from info where password = %s ;' % self.ui.lineEdit_password.text())
        myresult = my_cursor.fetchall()


        if (user == myresult[0][0] and str(password) == str(myresult[0][1])) :
            
            self.paneluser = Artists_names()
            self.paneluser.show()
            self.close()

        else:

            msg = QMessageBox.information(
                self,
                'Error',
                'Username or password is wrong !',
                QMessageBox.Ok
            )



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = MainLoading()
    sys.exit(app.exec_())


    
my_db.close()
