from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from login           import Ui_MainWindow

class RootMain(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        self.show()

    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())