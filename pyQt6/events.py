import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

times = 0
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(500, 400))

    def button_clicked(self):
        print("clicked!")
        global times
        times += 1
        print("This button was pressed" , times ,"Times!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()