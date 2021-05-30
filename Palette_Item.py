from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import *
from Hover_btn import *
import pyperclip

class Palette_item(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Palette_item, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.Frame = QFrame()
        self.layout.addWidget(self.Frame)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.Frame.setStyleSheet("background-color: " + color + ";")
        self.color = color
        self.copybtn = Hoverbtn()
        self.installEventFilter(self.copybtn)
        self.palette_name()
        self.setLayout(self.layout)

    def copy_btn_click(self):
        pyperclip.copy(self.color)
        self.copybtn.setToolTip("Hex Copied!")

    def palette_name(self):
        layout = QGridLayout()

        frametop = QFrame()
        frametop.setStyleSheet("background-color:  " + self.color + ";")
        frametop_layout = QVBoxLayout()
        self.copybtn.setIcon(QIcon("./Images/copy.png"))
        self.copybtn.setStyleSheet("background-color: transparent;")
        self.copybtn.setIconSize(QSize(30, 30))
        self.copybtn.clicked.connect(self.copy_btn_click)
        frametop_layout.addWidget(self.copybtn)
        frametop.setLayout(frametop_layout)

        framebottom = QFrame()
        framebottom.setStyleSheet("background-color: " + self.color + ";")
        framebottom_layout = QVBoxLayout()
        hex_label = QLabel()
        hex_label.setStyleSheet("color: white;")
        hex_label.setText(self.color)
        hex_label.setAlignment(Qt.AlignCenter)
        hex_label.setFont(QFont('Trebuchet MS', 12))
        framebottom_layout.addWidget(hex_label)
        framebottom_layout.setSpacing(0)
        framebottom_layout.setContentsMargins(0, 0, 0, 0)
        framebottom.setLayout(framebottom_layout)


        layout.addWidget(frametop, 0, 0, 4, 1)
        layout.addWidget(framebottom, 4, 0, 1, 1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.Frame.setLayout(layout)
