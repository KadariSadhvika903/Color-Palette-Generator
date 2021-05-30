from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
        # self.setFixedSize(500, 500)
        self.setScaledContents(True)


    def setPixmap(self, image):
        image.scaled(200, 200, Qt.KeepAspectRatioByExpanding)
        super().setPixmap(image)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Image Upload Window")
        self.setAcceptDrops(True)
        self.filepath = ""

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.btn = QPushButton("Upload Image")
        self.btn.clicked.connect(self.getfile)
        mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                            "c:\\", "Image files (*.jpg *.png)")

        self.set_image(fname)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.filepath = file_path
        self.photoViewer.setPixmap(QPixmap(file_path))
