import sys
import hello
from Bebop import Bebop
from PyQt5.QtWidgets import QApplication, QMainWindow


def land_close_exit(bebop):
    if (not bebop.is_landed()):
            bebop.emergency_land()
    sys.exit()


if __name__ == '__main__':
    bebop = Bebop()
    print("connecting")
    success = bebop.connect(10)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello.MyDroneGUI(bebop,MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    app.aboutToQuit.connect(lambda :land_close_exit(bebop))
    sys.exit(app.exec_())
