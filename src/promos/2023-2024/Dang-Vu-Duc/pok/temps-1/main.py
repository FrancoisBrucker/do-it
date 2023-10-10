from UI_blackjack import Blackjack
from blackjack_methods import Blackjack_simulation
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = Blackjack()
app.exec()

simulation = Blackjack_simulation()
# 1: Graphique en barres des taux de réussite du joueur face à chaque première carte possible du dealer
# 2: Taux de réussite de chaque main possible (sans As ni double)
# 3: Taux de réussite de chaque main possible (seulement les doubles)
# 4: Taux de réussite de chaque main possible (avec un As en main)
# 5: Tout les graphes ci-dessus
# simulation.simulation(10000000, True, 5)
