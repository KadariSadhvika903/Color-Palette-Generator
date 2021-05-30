from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QColorDialog

from Colors import *
from Img_dailogbox import *
from Palette_Item import *
from Palette_generator import *
from Save_file import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.uploader = AppDemo()
        self.title = 'Color Palette Generator'
        self.setWindowIcon(QIcon("./Images/windowpalette.png"))
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 900
        self.panel_btns = []
        self.mode = 0
        self.layout_palette = QHBoxLayout()
        self.layout_palette.setContentsMargins(0, 0, 0, 0)
        self.layout_palette.setSpacing(0)

        self.color_selected = ""
        self.palette = []
        self.grid_layout()
        self.initUI()

    def grid_layout(self):
        layout = QGridLayout()

        frametop = QFrame()
        self.top_frame(frametop)

        # frame.setGeometry()

        framebottom = QFrame()
        framebottom.setStyleSheet('background-color: ' + framebottomcolor + ";")
        self.down_frame(framebottom)

        layout.addWidget(frametop, 0, 0, 7, 1)
        layout.addWidget(framebottom, 7, 0, 1, 1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Set the layout on the application's window
        self.setLayout(layout)

    def down_frame(self, framebottom):
        layout = QGridLayout()

        frameleft = QFrame()
        self.UiComponents(frameleft)

        frameright = QFrame()
        self.btn_right(frameright)

        layout.addWidget(frameleft, 0, 0, 1, 3)
        layout.addWidget(frameright, 0, 3, 1, 1)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        framebottom.setLayout(layout)

    def top_frame(self, frametop):
        frametop.setLayout(self.layout_palette)

    def update_palette(self, palette):
        for i in reversed(range(self.layout_palette.count())):
            widgetToRemove = self.layout_palette.itemAt(i).widget()
            self.layout_palette.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        for color in palette:
            self.layout_palette.addWidget(Palette_item(color))


    def generate_palette(self):
        palette = get_general_palette()
        if self.color_selected != "" and self.mode == 1:
            palette = get_light_palette(self.color_selected)
        if self.color_selected != "" and self.mode == 2:
            palette = get_dark_palette(self.color_selected)
        if self.uploader.filepath != "":
            palette = generate_Kmeans_palette(self.uploader.filepath, 10)
        self.palette = palette
        self.update_palette(palette)



    def create_btn(self, name, function, img, layout):
        button = QPushButton(name)
        button.clicked.connect(function)
        button.setIcon(QIcon(img))
        button.setFont(QFont('Trebuchet MS', 12))
        button.setIconSize(QSize(30, 30))
        button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : transparent;"
                             "color: white; "
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : " + blue + ";"
                                                            "}"
                             )
        self.panel_btns.append(button)
        layout.addWidget(button)

    def UiComponents(self, frameleft):
        layout = QHBoxLayout()
        self.create_btn("Color Picker", self.on_click, "./Images/color-picker.png", layout)
        self.create_btn("Upload Image", self.img_uploader, "./Images/upload-img.png", layout)
        # self.create_btn("View", self.clickme, "./Images/view.png", layout)
        self.create_btn("Export", self.export, "./Images/share.png", layout)
        self.dropdown(layout)
        frameleft.setLayout(layout)

    def export(self):
        filepath = 'C:/Users/Kadari Sadhvika/Downloads/color-palette.txt'
        savefile(filepath, self.palette)

    def btn_right(self, frameright):
        layout = QHBoxLayout()
        self.create_btn("Generate Palette", self.generate_palette, "./Images/color-palette.png", layout)
        frameright.setLayout(layout)

    # action method
    def clickme(self):
        print("pressed")

    def img_uploader(self):
        self.uploader.show()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_selected = color.name()
            self.uploader.filepath = ""
            self.panel_btns[0].setStyleSheet(
                "QPushButton"
                "{"
                "background-color : " + color.name() + ";"
                                                       "color: white; "

                                                       "}"
            )

    def on_click(self):
        self.openColorDialog()

    def dropdown(self, layout):
        combo_box = QComboBox()
        combo_box.setStyleSheet("color: white;")
        combo_box.setMaximumWidth(250)
        combo_box.setFont(QFont('Trebuchet MS', 12))
        drop_list = ["Select Mode", "Same Shade Light Combo", "Same Shade Dark Combo"]
        combo_box.setEditable(False)
        combo_box.addItems(drop_list)
        combo_box.currentIndexChanged.connect(self.mode_click)
        view = combo_box.view()
        view.setRowHidden(0, True)
        layout.addWidget(combo_box)

    def mode_click(self, i):
        self.mode = i



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
