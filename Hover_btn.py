from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import *

class Hoverbtn(QPushButton):
    def __init__(self, *args, **kwargs):
        super(Hoverbtn, self).__init__(*args, **kwargs)
        self.setVisible(False)


    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        if event.type() == QEvent.Enter:
            self.setVisible(True)
        elif event.type() == QEvent.Leave:
            self.setVisible(False)
        return super(Hoverbtn, self).eventFilter(obj, event)
