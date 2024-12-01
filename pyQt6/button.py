import sys
from PyQt6.QtWidgets import QApplication, QPushButton # type: ignore

app = QApplication(sys.argv)

window = QPushButton("cool button")
window.show()

app.exec()
