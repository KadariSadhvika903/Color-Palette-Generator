from PyQt5.QtWidgets import QApplication

from Qt_GUI import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setWindowIcon(QIcon("./Images/windowpalette.png"))
    sys.exit(app.exec_())
