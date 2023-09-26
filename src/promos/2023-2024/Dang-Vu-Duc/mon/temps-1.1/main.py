from UI_bataille import Bataille  
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = Bataille()
app.exec()
