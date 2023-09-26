from UI_blackjack import Blackjack  
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = Blackjack()
app.exec()

