import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow

app = QApplication(sys.argv)
w = MainWindow(app)
w.show()
app.exec()
