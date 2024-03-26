from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QSlider, QLineEdit, QProgressBar, QComboBox, QRadioButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap, QIntValidator, QIcon
from poker import Card, Poker_methods
import json

class Button_methods(Poker_methods):
    def __init__(self):
        super().__init__()
        ui_file_name = "window_hand_range.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.window_hand_range = loader.load(ui_file)
        ui_file.close()
        self.window_hand_range.setWindowTitle("Fenêtre d'aide au choix")
        self.buttonA2s = self.window_hand_range.findChild(QPushButton, "buttonA2s")
        self.buttonA3s = self.window_hand_range.findChild(QPushButton, "buttonA3s")
        self.buttonA4s = self.window_hand_range.findChild(QPushButton, "buttonA4s")
        self.buttonA5s = self.window_hand_range.findChild(QPushButton, "buttonA5s")
        self.buttonA6s = self.window_hand_range.findChild(QPushButton, "buttonA6s")
        self.buttonA7s = self.window_hand_range.findChild(QPushButton, "buttonA7s")
        self.buttonA8s = self.window_hand_range.findChild(QPushButton, "buttonA8s")
        self.buttonA9s = self.window_hand_range.findChild(QPushButton, "buttonA9s")
        self.button22 = self.window_hand_range.findChild(QPushButton, "button22")
        self.button33 = self.window_hand_range.findChild(QPushButton, "button33")
        self.button32s = self.window_hand_range.findChild(QPushButton, "button32s")
        self.button32o = self.window_hand_range.findChild(QPushButton, "button32o")
        self.button44 = self.window_hand_range.findChild(QPushButton, "button44")
        self.button42s = self.window_hand_range.findChild(QPushButton, "button42s")
        self.button42o = self.window_hand_range.findChild(QPushButton, "button42o")
        self.button43s = self.window_hand_range.findChild(QPushButton, "button43s")
        self.button43o = self.window_hand_range.findChild(QPushButton, "button43o")
        self.button55 = self.window_hand_range.findChild(QPushButton, "button55")
        self.button52s = self.window_hand_range.findChild(QPushButton, "button52s")
        self.button52o = self.window_hand_range.findChild(QPushButton, "button52o")
        self.button53s = self.window_hand_range.findChild(QPushButton, "button53s")
        self.button53o = self.window_hand_range.findChild(QPushButton, "button53o")
        self.button54s = self.window_hand_range.findChild(QPushButton, "button54s")
        self.button54o = self.window_hand_range.findChild(QPushButton, "button54o")
        self.button66 = self.window_hand_range.findChild(QPushButton, "button66")
        self.button62s = self.window_hand_range.findChild(QPushButton, "button62s")
        self.button62o = self.window_hand_range.findChild(QPushButton, "button62o")
        self.button63s = self.window_hand_range.findChild(QPushButton, "button63s")
        self.button63o = self.window_hand_range.findChild(QPushButton, "button63o")
        self.button64s = self.window_hand_range.findChild(QPushButton, "button64s")
        self.button64o = self.window_hand_range.findChild(QPushButton, "button64o")
        self.button65s = self.window_hand_range.findChild(QPushButton, "button65s")
        self.button65o = self.window_hand_range.findChild(QPushButton, "button65o")
        self.button77 = self.window_hand_range.findChild(QPushButton, "button77")
        self.button72s = self.window_hand_range.findChild(QPushButton, "button72s")
        self.button72o = self.window_hand_range.findChild(QPushButton, "button72o")
        self.button73s = self.window_hand_range.findChild(QPushButton, "button73s")
        self.button73o = self.window_hand_range.findChild(QPushButton, "button73o")
        self.button74s = self.window_hand_range.findChild(QPushButton, "button74s")
        self.button74o = self.window_hand_range.findChild(QPushButton, "button74o")
        self.button75s = self.window_hand_range.findChild(QPushButton, "button75s")
        self.button75o = self.window_hand_range.findChild(QPushButton, "button75o")
        self.button76s = self.window_hand_range.findChild(QPushButton, "button76s")
        self.button76o = self.window_hand_range.findChild(QPushButton, "button76o")
        self.button88 = self.window_hand_range.findChild(QPushButton, "button88")
        self.button82s = self.window_hand_range.findChild(QPushButton, "button82s")
        self.button82o = self.window_hand_range.findChild(QPushButton, "button82o")
        self.button83s = self.window_hand_range.findChild(QPushButton, "button83s")
        self.button83o = self.window_hand_range.findChild(QPushButton, "button83o")
        self.button84s = self.window_hand_range.findChild(QPushButton, "button84s")
        self.button84o = self.window_hand_range.findChild(QPushButton, "button84o")
        self.button85s = self.window_hand_range.findChild(QPushButton, "button85s")
        self.button85o = self.window_hand_range.findChild(QPushButton, "button85o")
        self.button86s = self.window_hand_range.findChild(QPushButton, "button86s")
        self.button86o = self.window_hand_range.findChild(QPushButton, "button86o")
        self.button87s = self.window_hand_range.findChild(QPushButton, "button87s")
        self.button87o = self.window_hand_range.findChild(QPushButton, "button87o")
        self.button99 = self.window_hand_range.findChild(QPushButton, "button99")
        self.button92s = self.window_hand_range.findChild(QPushButton, "button92s")
        self.button92o = self.window_hand_range.findChild(QPushButton, "button92o")
        self.button93s = self.window_hand_range.findChild(QPushButton, "button93s")
        self.button93o = self.window_hand_range.findChild(QPushButton, "button93o")
        self.button94s = self.window_hand_range.findChild(QPushButton, "button94s")
        self.button94o = self.window_hand_range.findChild(QPushButton, "button94o")
        self.button95s = self.window_hand_range.findChild(QPushButton, "button95s")
        self.button95o = self.window_hand_range.findChild(QPushButton, "button95o")
        self.button96s = self.window_hand_range.findChild(QPushButton, "button96s")
        self.button96o = self.window_hand_range.findChild(QPushButton, "button96o")
        self.button97s = self.window_hand_range.findChild(QPushButton, "button97s")
        self.button97o = self.window_hand_range.findChild(QPushButton, "button97o")
        self.button98s = self.window_hand_range.findChild(QPushButton, "button98s")
        self.button98o = self.window_hand_range.findChild(QPushButton, "button98o")
        self.buttonTT = self.window_hand_range.findChild(QPushButton, "buttonTT")
        self.buttonT2s = self.window_hand_range.findChild(QPushButton, "buttonT2s")
        self.buttonT2o = self.window_hand_range.findChild(QPushButton, "buttonT2o")
        self.buttonT3s = self.window_hand_range.findChild(QPushButton, "buttonT3s")
        self.buttonT3o = self.window_hand_range.findChild(QPushButton, "buttonT3o")
        self.buttonT4s = self.window_hand_range.findChild(QPushButton, "buttonT4s")
        self.buttonT4o = self.window_hand_range.findChild(QPushButton, "buttonT4o")
        self.buttonT5s = self.window_hand_range.findChild(QPushButton, "buttonT5s")
        self.buttonT5o = self.window_hand_range.findChild(QPushButton, "buttonT5o")
        self.buttonT6s = self.window_hand_range.findChild(QPushButton, "buttonT6s")
        self.buttonT6o = self.window_hand_range.findChild(QPushButton, "buttonT6o")
        self.buttonT7s = self.window_hand_range.findChild(QPushButton, "buttonT7s")
        self.buttonT7o = self.window_hand_range.findChild(QPushButton, "buttonT7o")
        self.buttonT8s = self.window_hand_range.findChild(QPushButton, "buttonT8s")
        self.buttonT8o = self.window_hand_range.findChild(QPushButton, "buttonT8o")
        self.buttonT9s = self.window_hand_range.findChild(QPushButton, "buttonT9s")
        self.buttonT9o = self.window_hand_range.findChild(QPushButton, "buttonT9o")
        self.buttonJJ = self.window_hand_range.findChild(QPushButton, "buttonJJ")
        self.buttonJ2s = self.window_hand_range.findChild(QPushButton, "buttonJ2s")
        self.buttonJ2o = self.window_hand_range.findChild(QPushButton, "buttonJ2o")
        self.buttonJ3s = self.window_hand_range.findChild(QPushButton, "buttonJ3s")
        self.buttonJ3o = self.window_hand_range.findChild(QPushButton, "buttonJ3o")
        self.buttonJ4s = self.window_hand_range.findChild(QPushButton, "buttonJ4s")
        self.buttonJ4o = self.window_hand_range.findChild(QPushButton, "buttonJ4o")
        self.buttonJ5s = self.window_hand_range.findChild(QPushButton, "buttonJ5s")
        self.buttonJ5o = self.window_hand_range.findChild(QPushButton, "buttonJ5o")
        self.buttonJ6s = self.window_hand_range.findChild(QPushButton, "buttonJ6s")
        self.buttonJ6o = self.window_hand_range.findChild(QPushButton, "buttonJ6o")
        self.buttonJ7s = self.window_hand_range.findChild(QPushButton, "buttonJ7s")
        self.buttonJ7o = self.window_hand_range.findChild(QPushButton, "buttonJ7o")
        self.buttonJ8s = self.window_hand_range.findChild(QPushButton, "buttonJ8s")
        self.buttonJ8o = self.window_hand_range.findChild(QPushButton, "buttonJ8o")
        self.buttonJ9s = self.window_hand_range.findChild(QPushButton, "buttonJ9s")
        self.buttonJ9o = self.window_hand_range.findChild(QPushButton, "buttonJ9o")
        self.buttonJTs = self.window_hand_range.findChild(QPushButton, "buttonJTs")
        self.buttonJTo = self.window_hand_range.findChild(QPushButton, "buttonJTo")
        self.buttonQQ = self.window_hand_range.findChild(QPushButton, "buttonQQ")
        self.buttonQ2s = self.window_hand_range.findChild(QPushButton, "buttonQ2s")
        self.buttonQ2o = self.window_hand_range.findChild(QPushButton, "buttonQ2o")
        self.buttonQ3s = self.window_hand_range.findChild(QPushButton, "buttonQ3s")
        self.buttonQ3o = self.window_hand_range.findChild(QPushButton, "buttonQ3o")
        self.buttonQ4s = self.window_hand_range.findChild(QPushButton, "buttonQ4s")
        self.buttonQ4o = self.window_hand_range.findChild(QPushButton, "buttonQ4o")
        self.buttonQ5s = self.window_hand_range.findChild(QPushButton, "buttonQ5s")
        self.buttonQ5o = self.window_hand_range.findChild(QPushButton, "buttonQ5o")
        self.buttonQ6s = self.window_hand_range.findChild(QPushButton, "buttonQ6s")
        self.buttonQ6o = self.window_hand_range.findChild(QPushButton, "buttonQ6o")
        self.buttonQ7s = self.window_hand_range.findChild(QPushButton, "buttonQ7s")
        self.buttonQ7o = self.window_hand_range.findChild(QPushButton, "buttonQ7o")
        self.buttonQ8s = self.window_hand_range.findChild(QPushButton, "buttonQ8s")
        self.buttonQ8o = self.window_hand_range.findChild(QPushButton, "buttonQ8o")
        self.buttonQ9s = self.window_hand_range.findChild(QPushButton, "buttonQ9s")
        self.buttonQ9o = self.window_hand_range.findChild(QPushButton, "buttonQ9o")
        self.buttonQTs = self.window_hand_range.findChild(QPushButton, "buttonQTs")
        self.buttonQTo = self.window_hand_range.findChild(QPushButton, "buttonQTo")
        self.buttonQJs = self.window_hand_range.findChild(QPushButton, "buttonQJs")
        self.buttonQJo = self.window_hand_range.findChild(QPushButton, "buttonQJo")
        self.buttonKK = self.window_hand_range.findChild(QPushButton, "buttonKK")
        self.buttonK2s = self.window_hand_range.findChild(QPushButton, "buttonK2s")
        self.buttonK2o = self.window_hand_range.findChild(QPushButton, "buttonK2o")
        self.buttonK3s = self.window_hand_range.findChild(QPushButton, "buttonK3s")
        self.buttonK3o = self.window_hand_range.findChild(QPushButton, "buttonK3o")
        self.buttonK4s = self.window_hand_range.findChild(QPushButton, "buttonK4s")
        self.buttonK4o = self.window_hand_range.findChild(QPushButton, "buttonK4o")
        self.buttonK5s = self.window_hand_range.findChild(QPushButton, "buttonK5s")
        self.buttonK5o = self.window_hand_range.findChild(QPushButton, "buttonK5o")
        self.buttonK6s = self.window_hand_range.findChild(QPushButton, "buttonK6s")
        self.buttonK6o = self.window_hand_range.findChild(QPushButton, "buttonK6o")
        self.buttonK7s = self.window_hand_range.findChild(QPushButton, "buttonK7s")
        self.buttonK7o = self.window_hand_range.findChild(QPushButton, "buttonK7o")
        self.buttonK8s = self.window_hand_range.findChild(QPushButton, "buttonK8s")
        self.buttonK8o = self.window_hand_range.findChild(QPushButton, "buttonK8o")
        self.buttonK9s = self.window_hand_range.findChild(QPushButton, "buttonK9s")
        self.buttonK9o = self.window_hand_range.findChild(QPushButton, "buttonK9o")
        self.buttonKTs = self.window_hand_range.findChild(QPushButton, "buttonKTs")
        self.buttonKTo = self.window_hand_range.findChild(QPushButton, "buttonKTo")
        self.buttonKJs = self.window_hand_range.findChild(QPushButton, "buttonKJs")
        self.buttonKJo = self.window_hand_range.findChild(QPushButton, "buttonKJo")
        self.buttonKQs = self.window_hand_range.findChild(QPushButton, "buttonKQs")
        self.buttonKQo = self.window_hand_range.findChild(QPushButton, "buttonKQo")
        self.buttonAA = self.window_hand_range.findChild(QPushButton, "buttonAA")
        self.buttonA2s = self.window_hand_range.findChild(QPushButton, "buttonA2s")
        self.buttonA2o = self.window_hand_range.findChild(QPushButton, "buttonA2o")
        self.buttonA3s = self.window_hand_range.findChild(QPushButton, "buttonA3s")
        self.buttonA3o = self.window_hand_range.findChild(QPushButton, "buttonA3o")
        self.buttonA4s = self.window_hand_range.findChild(QPushButton, "buttonA4s")
        self.buttonA4o = self.window_hand_range.findChild(QPushButton, "buttonA4o")
        self.buttonA5s = self.window_hand_range.findChild(QPushButton, "buttonA5s")
        self.buttonA5o = self.window_hand_range.findChild(QPushButton, "buttonA5o")
        self.buttonA6s = self.window_hand_range.findChild(QPushButton, "buttonA6s")
        self.buttonA6o = self.window_hand_range.findChild(QPushButton, "buttonA6o")
        self.buttonA7s = self.window_hand_range.findChild(QPushButton, "buttonA7s")
        self.buttonA7o = self.window_hand_range.findChild(QPushButton, "buttonA7o")
        self.buttonA8s = self.window_hand_range.findChild(QPushButton, "buttonA8s")
        self.buttonA8o = self.window_hand_range.findChild(QPushButton, "buttonA8o")
        self.buttonA9s = self.window_hand_range.findChild(QPushButton, "buttonA9s")
        self.buttonA9o = self.window_hand_range.findChild(QPushButton, "buttonA9o")
        self.buttonATs = self.window_hand_range.findChild(QPushButton, "buttonATs")
        self.buttonATo = self.window_hand_range.findChild(QPushButton, "buttonATo")
        self.buttonAJs = self.window_hand_range.findChild(QPushButton, "buttonAJs")
        self.buttonAJo = self.window_hand_range.findChild(QPushButton, "buttonAJo")
        self.buttonAQs = self.window_hand_range.findChild(QPushButton, "buttonAQs")
        self.buttonAQo = self.window_hand_range.findChild(QPushButton, "buttonAQo")
        self.buttonAKs = self.window_hand_range.findChild(QPushButton, "buttonAKs")
        self.buttonAKo = self.window_hand_range.findChild(QPushButton, "buttonAKo")
        self.button22.clicked.connect(self.button22_clicked)
        self.button33.clicked.connect(self.button33_clicked)
        self.button32s.clicked.connect(self.button32s_clicked)
        self.button32o.clicked.connect(self.button32o_clicked)
        self.button44.clicked.connect(self.button44_clicked)
        self.button42s.clicked.connect(self.button42s_clicked)
        self.button42o.clicked.connect(self.button42o_clicked)
        self.button43s.clicked.connect(self.button43s_clicked)
        self.button43o.clicked.connect(self.button43o_clicked)
        self.button55.clicked.connect(self.button55_clicked)
        self.button52s.clicked.connect(self.button52s_clicked)
        self.button52o.clicked.connect(self.button52o_clicked)
        self.button53s.clicked.connect(self.button53s_clicked)
        self.button53o.clicked.connect(self.button53o_clicked)
        self.button54s.clicked.connect(self.button54s_clicked)
        self.button54o.clicked.connect(self.button54o_clicked)
        self.button66.clicked.connect(self.button66_clicked)
        self.button62s.clicked.connect(self.button62s_clicked)
        self.button62o.clicked.connect(self.button62o_clicked)
        self.button63s.clicked.connect(self.button63s_clicked)
        self.button63o.clicked.connect(self.button63o_clicked)
        self.button64s.clicked.connect(self.button64s_clicked)
        self.button64o.clicked.connect(self.button64o_clicked)
        self.button65s.clicked.connect(self.button65s_clicked)
        self.button65o.clicked.connect(self.button65o_clicked)
        self.button77.clicked.connect(self.button77_clicked)
        self.button72s.clicked.connect(self.button72s_clicked)
        self.button72o.clicked.connect(self.button72o_clicked)
        self.button73s.clicked.connect(self.button73s_clicked)
        self.button73o.clicked.connect(self.button73o_clicked)
        self.button74s.clicked.connect(self.button74s_clicked)
        self.button74o.clicked.connect(self.button74o_clicked)
        self.button75s.clicked.connect(self.button75s_clicked)
        self.button75o.clicked.connect(self.button75o_clicked)
        self.button76s.clicked.connect(self.button76s_clicked)
        self.button76o.clicked.connect(self.button76o_clicked)
        self.button88.clicked.connect(self.button88_clicked)
        self.button82s.clicked.connect(self.button82s_clicked)
        self.button82o.clicked.connect(self.button82o_clicked)
        self.button83s.clicked.connect(self.button83s_clicked)
        self.button83o.clicked.connect(self.button83o_clicked)
        self.button84s.clicked.connect(self.button84s_clicked)
        self.button84o.clicked.connect(self.button84o_clicked)
        self.button85s.clicked.connect(self.button85s_clicked)
        self.button85o.clicked.connect(self.button85o_clicked)
        self.button86s.clicked.connect(self.button86s_clicked)
        self.button86o.clicked.connect(self.button86o_clicked)
        self.button87s.clicked.connect(self.button87s_clicked)
        self.button87o.clicked.connect(self.button87o_clicked)
        self.button99.clicked.connect(self.button99_clicked)
        self.button92s.clicked.connect(self.button92s_clicked)
        self.button92o.clicked.connect(self.button92o_clicked)
        self.button93s.clicked.connect(self.button93s_clicked)
        self.button93o.clicked.connect(self.button93o_clicked)
        self.button94s.clicked.connect(self.button94s_clicked)
        self.button94o.clicked.connect(self.button94o_clicked)
        self.button95s.clicked.connect(self.button95s_clicked)
        self.button95o.clicked.connect(self.button95o_clicked)
        self.button96s.clicked.connect(self.button96s_clicked)
        self.button96o.clicked.connect(self.button96o_clicked)
        self.button97s.clicked.connect(self.button97s_clicked)
        self.button97o.clicked.connect(self.button97o_clicked)
        self.button98s.clicked.connect(self.button98s_clicked)
        self.button98o.clicked.connect(self.button98o_clicked)
        self.buttonTT.clicked.connect(self.buttonTT_clicked)
        self.buttonT2s.clicked.connect(self.buttonT2s_clicked)
        self.buttonT2o.clicked.connect(self.buttonT2o_clicked)
        self.buttonT3s.clicked.connect(self.buttonT3s_clicked)
        self.buttonT3o.clicked.connect(self.buttonT3o_clicked)
        self.buttonT4s.clicked.connect(self.buttonT4s_clicked)
        self.buttonT4o.clicked.connect(self.buttonT4o_clicked)
        self.buttonT5s.clicked.connect(self.buttonT5s_clicked)
        self.buttonT5o.clicked.connect(self.buttonT5o_clicked)
        self.buttonT6s.clicked.connect(self.buttonT6s_clicked)
        self.buttonT6o.clicked.connect(self.buttonT6o_clicked)
        self.buttonT7s.clicked.connect(self.buttonT7s_clicked)
        self.buttonT7o.clicked.connect(self.buttonT7o_clicked)
        self.buttonT8s.clicked.connect(self.buttonT8s_clicked)
        self.buttonT8o.clicked.connect(self.buttonT8o_clicked)
        self.buttonT9s.clicked.connect(self.buttonT9s_clicked)
        self.buttonT9o.clicked.connect(self.buttonT9o_clicked)
        self.buttonJJ.clicked.connect(self.buttonJJ_clicked)
        self.buttonJ2s.clicked.connect(self.buttonJ2s_clicked)
        self.buttonJ2o.clicked.connect(self.buttonJ2o_clicked)
        self.buttonJ3s.clicked.connect(self.buttonJ3s_clicked)
        self.buttonJ3o.clicked.connect(self.buttonJ3o_clicked)
        self.buttonJ4s.clicked.connect(self.buttonJ4s_clicked)
        self.buttonJ4o.clicked.connect(self.buttonJ4o_clicked)
        self.buttonJ5s.clicked.connect(self.buttonJ5s_clicked)
        self.buttonJ5o.clicked.connect(self.buttonJ5o_clicked)
        self.buttonJ6s.clicked.connect(self.buttonJ6s_clicked)
        self.buttonJ6o.clicked.connect(self.buttonJ6o_clicked)
        self.buttonJ7s.clicked.connect(self.buttonJ7s_clicked)
        self.buttonJ7o.clicked.connect(self.buttonJ7o_clicked)
        self.buttonJ8s.clicked.connect(self.buttonJ8s_clicked)
        self.buttonJ8o.clicked.connect(self.buttonJ8o_clicked)
        self.buttonJ9s.clicked.connect(self.buttonJ9s_clicked)
        self.buttonJ9o.clicked.connect(self.buttonJ9o_clicked)
        self.buttonJTs.clicked.connect(self.buttonJTs_clicked)
        self.buttonJTo.clicked.connect(self.buttonJTo_clicked)
        self.buttonQQ.clicked.connect(self.buttonQQ_clicked)
        self.buttonQ2s.clicked.connect(self.buttonQ2s_clicked)
        self.buttonQ2o.clicked.connect(self.buttonQ2o_clicked)
        self.buttonQ3s.clicked.connect(self.buttonQ3s_clicked)
        self.buttonQ3o.clicked.connect(self.buttonQ3o_clicked)
        self.buttonQ4s.clicked.connect(self.buttonQ4s_clicked)
        self.buttonQ4o.clicked.connect(self.buttonQ4o_clicked)
        self.buttonQ5s.clicked.connect(self.buttonQ5s_clicked)
        self.buttonQ5o.clicked.connect(self.buttonQ5o_clicked)
        self.buttonQ6s.clicked.connect(self.buttonQ6s_clicked)
        self.buttonQ6o.clicked.connect(self.buttonQ6o_clicked)
        self.buttonQ7s.clicked.connect(self.buttonQ7s_clicked)
        self.buttonQ7o.clicked.connect(self.buttonQ7o_clicked)
        self.buttonQ8s.clicked.connect(self.buttonQ8s_clicked)
        self.buttonQ8o.clicked.connect(self.buttonQ8o_clicked)
        self.buttonQ9s.clicked.connect(self.buttonQ9s_clicked)
        self.buttonQ9o.clicked.connect(self.buttonQ9o_clicked)
        self.buttonQTs.clicked.connect(self.buttonQTs_clicked)
        self.buttonQTo.clicked.connect(self.buttonQTo_clicked)
        self.buttonQJs.clicked.connect(self.buttonQJs_clicked)
        self.buttonQJo.clicked.connect(self.buttonQJo_clicked)
        self.buttonKK.clicked.connect(self.buttonKK_clicked)
        self.buttonK2s.clicked.connect(self.buttonK2s_clicked)
        self.buttonK2o.clicked.connect(self.buttonK2o_clicked)
        self.buttonK3s.clicked.connect(self.buttonK3s_clicked)
        self.buttonK3o.clicked.connect(self.buttonK3o_clicked)
        self.buttonK4s.clicked.connect(self.buttonK4s_clicked)
        self.buttonK4o.clicked.connect(self.buttonK4o_clicked)
        self.buttonK5s.clicked.connect(self.buttonK5s_clicked)
        self.buttonK5o.clicked.connect(self.buttonK5o_clicked)
        self.buttonK6s.clicked.connect(self.buttonK6s_clicked)
        self.buttonK6o.clicked.connect(self.buttonK6o_clicked)
        self.buttonK7s.clicked.connect(self.buttonK7s_clicked)
        self.buttonK7o.clicked.connect(self.buttonK7o_clicked)
        self.buttonK8s.clicked.connect(self.buttonK8s_clicked)
        self.buttonK8o.clicked.connect(self.buttonK8o_clicked)
        self.buttonK9s.clicked.connect(self.buttonK9s_clicked)
        self.buttonK9o.clicked.connect(self.buttonK9o_clicked)
        self.buttonKTs.clicked.connect(self.buttonKTs_clicked)
        self.buttonKTo.clicked.connect(self.buttonKTo_clicked)
        self.buttonKJs.clicked.connect(self.buttonKJs_clicked)
        self.buttonKJo.clicked.connect(self.buttonKJo_clicked)
        self.buttonKQs.clicked.connect(self.buttonKQs_clicked)
        self.buttonKQo.clicked.connect(self.buttonKQo_clicked)
        self.buttonAA.clicked.connect(self.buttonAA_clicked)
        self.buttonA2s.clicked.connect(self.buttonA2s_clicked)
        self.buttonA2o.clicked.connect(self.buttonA2o_clicked)
        self.buttonA3s.clicked.connect(self.buttonA3s_clicked)
        self.buttonA3o.clicked.connect(self.buttonA3o_clicked)
        self.buttonA4s.clicked.connect(self.buttonA4s_clicked)
        self.buttonA4o.clicked.connect(self.buttonA4o_clicked)
        self.buttonA5s.clicked.connect(self.buttonA5s_clicked)
        self.buttonA5o.clicked.connect(self.buttonA5o_clicked)
        self.buttonA6s.clicked.connect(self.buttonA6s_clicked)
        self.buttonA6o.clicked.connect(self.buttonA6o_clicked)
        self.buttonA7s.clicked.connect(self.buttonA7s_clicked)
        self.buttonA7o.clicked.connect(self.buttonA7o_clicked)
        self.buttonA8s.clicked.connect(self.buttonA8s_clicked)
        self.buttonA8o.clicked.connect(self.buttonA8o_clicked)
        self.buttonA9s.clicked.connect(self.buttonA9s_clicked)
        self.buttonA9o.clicked.connect(self.buttonA9o_clicked)
        self.buttonATs.clicked.connect(self.buttonATs_clicked)
        self.buttonATo.clicked.connect(self.buttonATo_clicked)
        self.buttonAJs.clicked.connect(self.buttonAJs_clicked)
        self.buttonAJo.clicked.connect(self.buttonAJo_clicked)
        self.buttonAQs.clicked.connect(self.buttonAQs_clicked)
        self.buttonAQo.clicked.connect(self.buttonAQo_clicked)
        self.buttonAKs.clicked.connect(self.buttonAKs_clicked)
        self.buttonAKo.clicked.connect(self.buttonAKo_clicked)

        self.button_suited = self.window_hand_range.findChild(QPushButton, "button_suited")
        self.button_offsuit = self.window_hand_range.findChild(QPushButton, "button_offsuit")
        self.button_suited.clicked.connect(self.select_suited)
        self.button_offsuit.clicked.connect(self.select_offsuit)

        self.button_select_board = self.window_hand_range.findChild(QPushButton, "button_select_board")
        self.button_select_board.clicked.connect(self.select_board)

        self.button_restart = self.window_hand_range.findChild(QPushButton, "button_restart")
        self.button_restart.clicked.connect(self.restart_buttons)
        self.restart_buttons()

        self.radio_button_heart = self.window_hand_range.findChild(QRadioButton, "radio_button_heart")
        self.radio_button_diamond = self.window_hand_range.findChild(QRadioButton, "radio_button_diamond")
        self.radio_button_club = self.window_hand_range.findChild(QRadioButton, "radio_button_club")
        self.radio_button_spade = self.window_hand_range.findChild(QRadioButton, "radio_button_spade")

        self.line_edit_top = self.window_hand_range.findChild(QLineEdit, "line_edit_top")
        self.line_edit_top.textChanged.connect(self.line_edit_top_changed)

        self.line_edit_pot = self.window_hand_range.findChild(QLineEdit, "line_edit_pot")
        self.line_edit_pot.textChanged.connect(self.line_edit_pot_changed)
        self.pot_value = 0
        self.line_edit_amount_to_call = self.window_hand_range.findChild(QLineEdit, "line_edit_amount_to_call")
        self.line_edit_amount_to_call.textChanged.connect(self.line_edit_amount_to_call_changed)
        self.amount_to_call_value = 0

        self.button_valider_selection = self.window_hand_range.findChild(QPushButton, "button_valider_selection")
        self.button_valider_selection.clicked.connect(self.button_valider_selection_clicked)

        with open('all_average_winrates5.json', 'rb') as fp:
            self.all_average_winrates = json.load(fp)
        self.ranking = [winrate[0] for winrate in self.all_average_winrates]
        self.value_line_edit = 0
        self.button_valider_line_edit = self.window_hand_range.findChild(QPushButton, "button_valider_line_edit")
        self.button_valider_line_edit.clicked.connect(self.valider_line_edit)

        self.range_selected = []
        
        self.button2_1 = self.window_hand_range.findChild(QPushButton, "button2_1")
        self.button2_1.clicked.connect(self.select_column_2)
        self.button2_2 = self.window_hand_range.findChild(QPushButton, "button2_2")
        self.button2_2.clicked.connect(self.select_line_2)
        self.button3_1 = self.window_hand_range.findChild(QPushButton, "button3_1")
        self.button3_1.clicked.connect(self.select_column_3)
        self.button3_2 = self.window_hand_range.findChild(QPushButton, "button3_2")
        self.button3_2.clicked.connect(self.select_line_3)
        self.button4_1 = self.window_hand_range.findChild(QPushButton, "button4_1")
        self.button4_1.clicked.connect(self.select_column_4)
        self.button4_2 = self.window_hand_range.findChild(QPushButton, "button4_2")
        self.button4_2.clicked.connect(self.select_line_4)
        self.button5_1 = self.window_hand_range.findChild(QPushButton, "button5_1")
        self.button5_1.clicked.connect(self.select_column_5)
        self.button5_2 = self.window_hand_range.findChild(QPushButton, "button5_2")
        self.button5_2.clicked.connect(self.select_line_5)
        self.button6_1 = self.window_hand_range.findChild(QPushButton, "button6_1")
        self.button6_1.clicked.connect(self.select_column_6)
        self.button6_2 = self.window_hand_range.findChild(QPushButton, "button6_2")
        self.button6_2.clicked.connect(self.select_line_6)
        self.button7_1 = self.window_hand_range.findChild(QPushButton, "button7_1")
        self.button7_1.clicked.connect(self.select_column_7)
        self.button7_2 = self.window_hand_range.findChild(QPushButton, "button7_2")
        self.button7_2.clicked.connect(self.select_line_7)
        self.button8_1 = self.window_hand_range.findChild(QPushButton, "button8_1")
        self.button8_1.clicked.connect(self.select_column_8)
        self.button8_2 = self.window_hand_range.findChild(QPushButton, "button8_2")
        self.button8_2.clicked.connect(self.select_line_8)
        self.button9_1 = self.window_hand_range.findChild(QPushButton, "button9_1")
        self.button9_1.clicked.connect(self.select_column_9)
        self.button9_2 = self.window_hand_range.findChild(QPushButton, "button9_2")
        self.button9_2.clicked.connect(self.select_line_9)
        self.buttonT_1 = self.window_hand_range.findChild(QPushButton, "buttonT_1")
        self.buttonT_1.clicked.connect(self.select_column_T)
        self.buttonT_2 = self.window_hand_range.findChild(QPushButton, "buttonT_2")
        self.buttonT_2.clicked.connect(self.select_line_T)
        self.buttonJ_1 = self.window_hand_range.findChild(QPushButton, "buttonJ_1")
        self.buttonJ_1.clicked.connect(self.select_column_J)
        self.buttonJ_2 = self.window_hand_range.findChild(QPushButton, "buttonJ_2")
        self.buttonJ_2.clicked.connect(self.select_line_J)
        self.buttonQ_1 = self.window_hand_range.findChild(QPushButton, "buttonQ_1")
        self.buttonQ_1.clicked.connect(self.select_column_Q)
        self.buttonQ_2 = self.window_hand_range.findChild(QPushButton, "buttonQ_2")
        self.buttonQ_2.clicked.connect(self.select_line_Q)
        self.buttonK_1 = self.window_hand_range.findChild(QPushButton, "buttonK_1")
        self.buttonK_1.clicked.connect(self.select_column_K)
        self.buttonK_2 = self.window_hand_range.findChild(QPushButton, "buttonK_2")
        self.buttonK_2.clicked.connect(self.select_line_K)
        self.buttonA_1 = self.window_hand_range.findChild(QPushButton, "buttonA_1")
        self.buttonA_1.clicked.connect(self.select_column_A)
        self.buttonA_2 = self.window_hand_range.findChild(QPushButton, "buttonA_2")
        self.buttonA_2.clicked.connect(self.select_line_A)

        self.combo_box_value1 = self.window_hand_range.findChild(QComboBox, "value1")
        self.combo_box_value2 = self.window_hand_range.findChild(QComboBox, "value2")
        self.combo_box_suit1 = self.window_hand_range.findChild(QComboBox, "suit1")
        self.combo_box_suit2 = self.window_hand_range.findChild(QComboBox, "suit2")

        ui_file_name = "window_board_cards.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.window_board_cards = loader.load(ui_file)
        ui_file.close()
        self.window_board_cards.setWindowTitle("Fenêtre de choix du tableau")

        self.radio_button_flop = self.window_board_cards.findChild(QRadioButton, "radio_button_flop")
        self.radio_button_turn = self.window_board_cards.findChild(QRadioButton, "radio_button_turn")
        self.radio_button_river = self.window_board_cards.findChild(QRadioButton, "radio_button_river")

        self.combo_box_board_value1 = self.window_board_cards.findChild(QComboBox, "value1")
        self.combo_box_board_value2 = self.window_board_cards.findChild(QComboBox, "value2")
        self.combo_box_board_value3 = self.window_board_cards.findChild(QComboBox, "value3")
        self.combo_box_board_value4 = self.window_board_cards.findChild(QComboBox, "value4")
        self.combo_box_board_value5 = self.window_board_cards.findChild(QComboBox, "value5")
        self.combo_box_board_suit1 = self.window_board_cards.findChild(QComboBox, "suit1")
        self.combo_box_board_suit2 = self.window_board_cards.findChild(QComboBox, "suit2")
        self.combo_box_board_suit3 = self.window_board_cards.findChild(QComboBox, "suit3")
        self.combo_box_board_suit4 = self.window_board_cards.findChild(QComboBox, "suit4")
        self.combo_box_board_suit5 = self.window_board_cards.findChild(QComboBox, "suit5")

        self.button_valider_current_board = self.window_board_cards.findChild(QPushButton, "button_valider")
        self.button_valider_current_board.clicked.connect(self.valider_current_board)

        self.current_board = []

        self.window_hand_range.show()

    def select_board(self):
        self.window_hand_range.close()
        self.window_board_cards.show()

    def valider_current_board(self):
        if self.radio_button_flop.isChecked() and not self.radio_button_turn.isChecked() and not self.radio_button_river.isChecked():
            value1 = self.value_name(self.combo_box_board_value1.currentText())
            value2 = self.value_name(self.combo_box_board_value2.currentText())
            value3 = self.value_name(self.combo_box_board_value3.currentText())
            suit1 = self.combo_box_board_suit1.currentText().lower()
            suit2 = self.combo_box_board_suit2.currentText().lower()
            suit3 = self.combo_box_board_suit3.currentText().lower()
            card1 = Card(value1, suit1)
            card2 = Card(value2, suit2)
            card3 = Card(value3, suit3)
            self.current_board = [card1, card2, card3]
        elif self.radio_button_flop.isChecked() and self.radio_button_turn.isChecked() and not self.radio_button_river.isChecked():
            value1 = self.value_name(self.combo_box_board_value1.currentText())
            value2 = self.value_name(self.combo_box_board_value2.currentText())
            value3 = self.value_name(self.combo_box_board_value3.currentText())
            value4 = self.value_name(self.combo_box_board_value4.currentText())
            suit1 = self.combo_box_board_suit1.currentText().lower()
            suit2 = self.combo_box_board_suit2.currentText().lower()
            suit3 = self.combo_box_board_suit3.currentText().lower()
            suit4 = self.combo_box_board_suit4.currentText().lower()
            card1 = Card(value1, suit1)
            card2 = Card(value2, suit2)
            card3 = Card(value3, suit3)
            card4 = Card(value4, suit4)
            self.current_board = [card1, card2, card3, card4]
        elif self.radio_button_flop.isChecked() and self.radio_button_turn.isChecked() and self.radio_button_river.isChecked():
            value1 = self.value_name(self.combo_box_board_value1.currentText())
            value2 = self.value_name(self.combo_box_board_value2.currentText())
            value3 = self.value_name(self.combo_box_board_value3.currentText())
            value4 = self.value_name(self.combo_box_board_value4.currentText())
            value5 = self.value_name(self.combo_box_board_value5.currentText())
            suit1 = self.combo_box_board_suit1.currentText().lower()
            suit2 = self.combo_box_board_suit2.currentText().lower()
            suit3 = self.combo_box_board_suit3.currentText().lower()
            suit4 = self.combo_box_board_suit4.currentText().lower()
            suit5 = self.combo_box_board_suit5.currentText().lower()
            card1 = Card(value1, suit1)
            card2 = Card(value2, suit2)
            card3 = Card(value3, suit3)
            card4 = Card(value4, suit4)
            card5 = Card(value5, suit5)
            self.current_board = [card1, card2, card3, card4, card5]
        else:
            self.current_board = []
        self.window_board_cards.close()
        self.window_hand_range.show()

    def select_suited(self):
        values = list(range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']
        for k, value1 in enumerate(values):
            values2 = values[:k]
            for value2 in values2:
                combination = str(value1) + str(value2) + "s"
                if combination not in self.range_selected:
                    self.range_selected.append(combination)
        self.color_buttons()

    def select_offsuit(self):
        values = list(range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']
        for k, value1 in enumerate(values):
            values2 = values[:k]
            for value2 in values2:
                combination = str(value1) + str(value2) + "o"
                if combination not in self.range_selected:
                    self.range_selected.append(combination)
        self.color_buttons()

    def line_edit_pot_changed(self, value):
        self.pot_value = int(value)
    
    def line_edit_amount_to_call_changed(self, value):
        self.amount_to_call_value = int(value)

    def button_valider_selection_clicked(self):
        if self.combo_box_value1.currentText() == "As":
            value1 = 14
        elif self.combo_box_value1.currentText() == "Roi":
            value1 = 13
        elif self.combo_box_value1.currentText() == "Dame":
            value1 = 12
        elif self.combo_box_value1.currentText() == "Valet":
            value1 = 11
        else:
            value1 = int(self.combo_box_value1.currentText())
        if self.combo_box_value2.currentText() == "As":
            value2 = 14
        elif self.combo_box_value2.currentText() == "Roi":
            value2 = 13
        elif self.combo_box_value2.currentText() == "Dame":
            value2 = 12
        elif self.combo_box_value2.currentText() == "Valet":
            value2 = 11
        else:
            value2 = int(self.combo_box_value2.currentText())
        suits = []
        if self.radio_button_heart.isChecked():
            suits.append("coeur")
        if self.radio_button_diamond.isChecked():
            suits.append("carreau")
        if self.radio_button_club.isChecked():
            suits.append("trèfle")
        if self.radio_button_spade.isChecked():
            suits.append("pique")
        player_hand = [Card(value1, str(self.combo_box_suit1.currentText()).lower()), Card(value2, str(self.combo_box_suit2.currentText()).lower())]
        print(self.get_decision(self.pot_value, self.amount_to_call_value, suits, player_hand, 3500, self.current_board))

    def button22_clicked(self):
        if '22' not in self.range_selected:
            self.button22.setStyleSheet('background-color: green')
            self.range_selected.append('22')
        else:
            self.range_selected.remove('22')
            self.button22.setStyleSheet('background-color: white')

    def button33_clicked(self):
        if '33' not in self.range_selected:
            self.button33.setStyleSheet('background-color: green')
            self.range_selected.append('33')
        else:
            self.range_selected.remove('33')
            self.button33.setStyleSheet('background-color: white')

    def button32s_clicked(self):
        if '32s' not in self.range_selected:
            self.button32s.setStyleSheet('background-color: green')
            self.range_selected.append('32s')
        else:
            self.range_selected.remove('32s')
            self.button32s.setStyleSheet('background-color: white')

    def button32o_clicked(self):
        if '32o' not in self.range_selected:
            self.button32o.setStyleSheet('background-color: green')
            self.range_selected.append('32o')
        else:
            self.range_selected.remove('32o')
            self.button32o.setStyleSheet('background-color: white')

    def button44_clicked(self):
        if '44' not in self.range_selected:
            self.button44.setStyleSheet('background-color: green')
            self.range_selected.append('44')
        else:
            self.range_selected.remove('44')
            self.button44.setStyleSheet('background-color: white')

    def button42s_clicked(self):
        if '42s' not in self.range_selected:
            self.button42s.setStyleSheet('background-color: green')
            self.range_selected.append('42s')
        else:
            self.range_selected.remove('42s')
            self.button42s.setStyleSheet('background-color: white')

    def button42o_clicked(self):
        if '42o' not in self.range_selected:
            self.button42o.setStyleSheet('background-color: green')
            self.range_selected.append('42o')
        else:
            self.range_selected.remove('42o')
            self.button42o.setStyleSheet('background-color: white')

    def button43s_clicked(self):
        if '43s' not in self.range_selected:
            self.button43s.setStyleSheet('background-color: green')
            self.range_selected.append('43s')
        else:
            self.range_selected.remove('43s')
            self.button43s.setStyleSheet('background-color: white')

    def button43o_clicked(self):
        if '43o' not in self.range_selected:
            self.button43o.setStyleSheet('background-color: green')
            self.range_selected.append('43o')
        else:
            self.range_selected.remove('43o')
            self.button43o.setStyleSheet('background-color: white')

    def button55_clicked(self):
        if '55' not in self.range_selected:
            self.button55.setStyleSheet('background-color: green')
            self.range_selected.append('55')
        else:
            self.range_selected.remove('55')
            self.button55.setStyleSheet('background-color: white')

    def button52s_clicked(self):
        if '52s' not in self.range_selected:
            self.button52s.setStyleSheet('background-color: green')
            self.range_selected.append('52s')
        else:
            self.range_selected.remove('52s')
            self.button52s.setStyleSheet('background-color: white')

    def button52o_clicked(self):
        if '52o' not in self.range_selected:
            self.button52o.setStyleSheet('background-color: green')
            self.range_selected.append('52o')
        else:
            self.range_selected.remove('52o')
            self.button52o.setStyleSheet('background-color: white')

    def button53s_clicked(self):
        if '53s' not in self.range_selected:
            self.button53s.setStyleSheet('background-color: green')
            self.range_selected.append('53s')
        else:
            self.range_selected.remove('53s')
            self.button53s.setStyleSheet('background-color: white')

    def button53o_clicked(self):
        if '53o' not in self.range_selected:
            self.button53o.setStyleSheet('background-color: green')
            self.range_selected.append('53o')
        else:
            self.range_selected.remove('53o')
            self.button53o.setStyleSheet('background-color: white')

    def button54s_clicked(self):
        if '54s' not in self.range_selected:
            self.button54s.setStyleSheet('background-color: green')
            self.range_selected.append('54s')
        else:
            self.range_selected.remove('54s')
            self.button54s.setStyleSheet('background-color: white')

    def button54o_clicked(self):
        if '54o' not in self.range_selected:
            self.button54o.setStyleSheet('background-color: green')
            self.range_selected.append('54o')
        else:
            self.range_selected.remove('54o')
            self.button54o.setStyleSheet('background-color: white')

    def button66_clicked(self):
        if '66' not in self.range_selected:
            self.button66.setStyleSheet('background-color: green')
            self.range_selected.append('66')
        else:
            self.range_selected.remove('66')
            self.button66.setStyleSheet('background-color: white')

    def button62s_clicked(self):
        if '62s' not in self.range_selected:
            self.button62s.setStyleSheet('background-color: green')
            self.range_selected.append('62s')
        else:
            self.range_selected.remove('62s')
            self.button62s.setStyleSheet('background-color: white')

    def button62o_clicked(self):
        if '62o' not in self.range_selected:
            self.button62o.setStyleSheet('background-color: green')
            self.range_selected.append('62o')
        else:
            self.range_selected.remove('62o')
            self.button62o.setStyleSheet('background-color: white')

    def button63s_clicked(self):
        if '63s' not in self.range_selected:
            self.button63s.setStyleSheet('background-color: green')
            self.range_selected.append('63s')
        else:
            self.range_selected.remove('63s')
            self.button63s.setStyleSheet('background-color: white')

    def button63o_clicked(self):
        if '63o' not in self.range_selected:
            self.button63o.setStyleSheet('background-color: green')
            self.range_selected.append('63o')
        else:
            self.range_selected.remove('63o')
            self.button63o.setStyleSheet('background-color: white')

    def button64s_clicked(self):
        if '64s' not in self.range_selected:
            self.button64s.setStyleSheet('background-color: green')
            self.range_selected.append('64s')
        else:
            self.range_selected.remove('64s')
            self.button64s.setStyleSheet('background-color: white')

    def button64o_clicked(self):
        if '64o' not in self.range_selected:
            self.button64o.setStyleSheet('background-color: green')
            self.range_selected.append('64o')
        else:
            self.range_selected.remove('64o')
            self.button64o.setStyleSheet('background-color: white')

    def button65s_clicked(self):
        if '65s' not in self.range_selected:
            self.button65s.setStyleSheet('background-color: green')
            self.range_selected.append('65s')
        else:
            self.range_selected.remove('65s')
            self.button65s.setStyleSheet('background-color: white')

    def button65o_clicked(self):
        if '65o' not in self.range_selected:
            self.button65o.setStyleSheet('background-color: green')
            self.range_selected.append('65o')
        else:
            self.range_selected.remove('65o')
            self.button65o.setStyleSheet('background-color: white')

    def button77_clicked(self):
        if '77' not in self.range_selected:
            self.button77.setStyleSheet('background-color: green')
            self.range_selected.append('77')
        else:
            self.range_selected.remove('77')
            self.button77.setStyleSheet('background-color: white')

    def button72s_clicked(self):
        if '72s' not in self.range_selected:
            self.button72s.setStyleSheet('background-color: green')
            self.range_selected.append('72s')
        else:
            self.range_selected.remove('72s')
            self.button72s.setStyleSheet('background-color: white')

    def button72o_clicked(self):
        if '72o' not in self.range_selected:
            self.button72o.setStyleSheet('background-color: green')
            self.range_selected.append('72o')
        else:
            self.range_selected.remove('72o')
            self.button72o.setStyleSheet('background-color: white')

    def button73s_clicked(self):
        if '73s' not in self.range_selected:
            self.button73s.setStyleSheet('background-color: green')
            self.range_selected.append('73s')
        else:
            self.range_selected.remove('73s')
            self.button73s.setStyleSheet('background-color: white')

    def button73o_clicked(self):
        if '73o' not in self.range_selected:
            self.button73o.setStyleSheet('background-color: green')
            self.range_selected.append('73o')
        else:
            self.range_selected.remove('73o')
            self.button73o.setStyleSheet('background-color: white')

    def button74s_clicked(self):
        if '74s' not in self.range_selected:
            self.button74s.setStyleSheet('background-color: green')
            self.range_selected.append('74s')
        else:
            self.range_selected.remove('74s')
            self.button74s.setStyleSheet('background-color: white')

    def button74o_clicked(self):
        if '74o' not in self.range_selected:
            self.button74o.setStyleSheet('background-color: green')
            self.range_selected.append('74o')
        else:
            self.range_selected.remove('74o')
            self.button74o.setStyleSheet('background-color: white')

    def button75s_clicked(self):
        if '75s' not in self.range_selected:
            self.button75s.setStyleSheet('background-color: green')
            self.range_selected.append('75s')
        else:
            self.range_selected.remove('75s')
            self.button75s.setStyleSheet('background-color: white')

    def button75o_clicked(self):
        if '75o' not in self.range_selected:
            self.button75o.setStyleSheet('background-color: green')
            self.range_selected.append('75o')
        else:
            self.range_selected.remove('75o')
            self.button75o.setStyleSheet('background-color: white')

    def button76s_clicked(self):
        if '76s' not in self.range_selected:
            self.button76s.setStyleSheet('background-color: green')
            self.range_selected.append('76s')
        else:
            self.range_selected.remove('76s')
            self.button76s.setStyleSheet('background-color: white')

    def button76o_clicked(self):
        if '76o' not in self.range_selected:
            self.button76o.setStyleSheet('background-color: green')
            self.range_selected.append('76o')
        else:
            self.range_selected.remove('76o')
            self.button76o.setStyleSheet('background-color: white')

    def button88_clicked(self):
        if '88' not in self.range_selected:
            self.button88.setStyleSheet('background-color: green')
            self.range_selected.append('88')
        else:
            self.range_selected.remove('88')
            self.button88.setStyleSheet('background-color: white')

    def button82s_clicked(self):
        if '82s' not in self.range_selected:
            self.button82s.setStyleSheet('background-color: green')
            self.range_selected.append('82s')
        else:
            self.range_selected.remove('82s')
            self.button82s.setStyleSheet('background-color: white')

    def button82o_clicked(self):
        if '82o' not in self.range_selected:
            self.button82o.setStyleSheet('background-color: green')
            self.range_selected.append('82o')
        else:
            self.range_selected.remove('82o')
            self.button82o.setStyleSheet('background-color: white')

    def button83s_clicked(self):
        if '83s' not in self.range_selected:
            self.button83s.setStyleSheet('background-color: green')
            self.range_selected.append('83s')
        else:
            self.range_selected.remove('83s')
            self.button83s.setStyleSheet('background-color: white')

    def button83o_clicked(self):
        if '83o' not in self.range_selected:
            self.button83o.setStyleSheet('background-color: green')
            self.range_selected.append('83o')
        else:
            self.range_selected.remove('83o')
            self.button83o.setStyleSheet('background-color: white')

    def button84s_clicked(self):
        if '84s' not in self.range_selected:
            self.button84s.setStyleSheet('background-color: green')
            self.range_selected.append('84s')
        else:
            self.range_selected.remove('84s')
            self.button84s.setStyleSheet('background-color: white')

    def button84o_clicked(self):
        if '84o' not in self.range_selected:
            self.button84o.setStyleSheet('background-color: green')
            self.range_selected.append('84o')
        else:
            self.range_selected.remove('84o')
            self.button84o.setStyleSheet('background-color: white')

    def button85s_clicked(self):
        if '85s' not in self.range_selected:
            self.button85s.setStyleSheet('background-color: green')
            self.range_selected.append('85s')
        else:
            self.range_selected.remove('85s')
            self.button85s.setStyleSheet('background-color: white')

    def button85o_clicked(self):
        if '85o' not in self.range_selected:
            self.button85o.setStyleSheet('background-color: green')
            self.range_selected.append('85o')
        else:
            self.range_selected.remove('85o')
            self.button85o.setStyleSheet('background-color: white')

    def button86s_clicked(self):
        if '86s' not in self.range_selected:
            self.button86s.setStyleSheet('background-color: green')
            self.range_selected.append('86s')
        else:
            self.range_selected.remove('86s')
            self.button86s.setStyleSheet('background-color: white')

    def button86o_clicked(self):
        if '86o' not in self.range_selected:
            self.button86o.setStyleSheet('background-color: green')
            self.range_selected.append('86o')
        else:
            self.range_selected.remove('86o')
            self.button86o.setStyleSheet('background-color: white')

    def button87s_clicked(self):
        if '87s' not in self.range_selected:
            self.button87s.setStyleSheet('background-color: green')
            self.range_selected.append('87s')
        else:
            self.range_selected.remove('87s')
            self.button87s.setStyleSheet('background-color: white')

    def button87o_clicked(self):
        if '87o' not in self.range_selected:
            self.button87o.setStyleSheet('background-color: green')
            self.range_selected.append('87o')
        else:
            self.range_selected.remove('87o')
            self.button87o.setStyleSheet('background-color: white')

    def button99_clicked(self):
        if '99' not in self.range_selected:
            self.button99.setStyleSheet('background-color: green')
            self.range_selected.append('99')
        else:
            self.range_selected.remove('99')
            self.button99.setStyleSheet('background-color: white')

    def button92s_clicked(self):
        if '92s' not in self.range_selected:
            self.button92s.setStyleSheet('background-color: green')
            self.range_selected.append('92s')
        else:
            self.range_selected.remove('92s')
            self.button92s.setStyleSheet('background-color: white')

    def button92o_clicked(self):
        if '92o' not in self.range_selected:
            self.button92o.setStyleSheet('background-color: green')
            self.range_selected.append('92o')
        else:
            self.range_selected.remove('92o')
            self.button92o.setStyleSheet('background-color: white')

    def button93s_clicked(self):
        if '93s' not in self.range_selected:
            self.button93s.setStyleSheet('background-color: green')
            self.range_selected.append('93s')
        else:
            self.range_selected.remove('93s')
            self.button93s.setStyleSheet('background-color: white')

    def button93o_clicked(self):
        if '93o' not in self.range_selected:
            self.button93o.setStyleSheet('background-color: green')
            self.range_selected.append('93o')
        else:
            self.range_selected.remove('93o')
            self.button93o.setStyleSheet('background-color: white')

    def button94s_clicked(self):
        if '94s' not in self.range_selected:
            self.button94s.setStyleSheet('background-color: green')
            self.range_selected.append('94s')
        else:
            self.range_selected.remove('94s')
            self.button94s.setStyleSheet('background-color: white')

    def button94o_clicked(self):
        if '94o' not in self.range_selected:
            self.button94o.setStyleSheet('background-color: green')
            self.range_selected.append('94o')
        else:
            self.range_selected.remove('94o')
            self.button94o.setStyleSheet('background-color: white')

    def button95s_clicked(self):
        if '95s' not in self.range_selected:
            self.button95s.setStyleSheet('background-color: green')
            self.range_selected.append('95s')
        else:
            self.range_selected.remove('95s')
            self.button95s.setStyleSheet('background-color: white')

    def button95o_clicked(self):
        if '95o' not in self.range_selected:
            self.button95o.setStyleSheet('background-color: green')
            self.range_selected.append('95o')
        else:
            self.range_selected.remove('95o')
            self.button95o.setStyleSheet('background-color: white')

    def button96s_clicked(self):
        if '96s' not in self.range_selected:
            self.button96s.setStyleSheet('background-color: green')
            self.range_selected.append('96s')
        else:
            self.range_selected.remove('96s')
            self.button96s.setStyleSheet('background-color: white')

    def button96o_clicked(self):
        if '96o' not in self.range_selected:
            self.button96o.setStyleSheet('background-color: green')
            self.range_selected.append('96o')
        else:
            self.range_selected.remove('96o')
            self.button96o.setStyleSheet('background-color: white')

    def button97s_clicked(self):
        if '97s' not in self.range_selected:
            self.button97s.setStyleSheet('background-color: green')
            self.range_selected.append('97s')
        else:
            self.range_selected.remove('97s')
            self.button97s.setStyleSheet('background-color: white')

    def button97o_clicked(self):
        if '97o' not in self.range_selected:
            self.button97o.setStyleSheet('background-color: green')
            self.range_selected.append('97o')
        else:
            self.range_selected.remove('97o')
            self.button97o.setStyleSheet('background-color: white')

    def button98s_clicked(self):
        if '98s' not in self.range_selected:
            self.button98s.setStyleSheet('background-color: green')
            self.range_selected.append('98s')
        else:
            self.range_selected.remove('98s')
            self.button98s.setStyleSheet('background-color: white')

    def button98o_clicked(self):
        if '98o' not in self.range_selected:
            self.button98o.setStyleSheet('background-color: green')
            self.range_selected.append('98o')
        else:
            self.range_selected.remove('98o')
            self.button98o.setStyleSheet('background-color: white')

    def buttonTT_clicked(self):
        if 'TT' not in self.range_selected:
            self.buttonTT.setStyleSheet('background-color: green')
            self.range_selected.append('TT')
        else:
            self.range_selected.remove('TT')
            self.buttonTT.setStyleSheet('background-color: white')

    def buttonT2s_clicked(self):
        if 'T2s' not in self.range_selected:
            self.buttonT2s.setStyleSheet('background-color: green')
            self.range_selected.append('T2s')
        else:
            self.range_selected.remove('T2s')
            self.buttonT2s.setStyleSheet('background-color: white')

    def buttonT2o_clicked(self):
        if 'T2o' not in self.range_selected:
            self.buttonT2o.setStyleSheet('background-color: green')
            self.range_selected.append('T2o')
        else:
            self.range_selected.remove('T2o')
            self.buttonT2o.setStyleSheet('background-color: white')

    def buttonT3s_clicked(self):
        if 'T3s' not in self.range_selected:
            self.buttonT3s.setStyleSheet('background-color: green')
            self.range_selected.append('T3s')
        else:
            self.range_selected.remove('T3s')
            self.buttonT3s.setStyleSheet('background-color: white')

    def buttonT3o_clicked(self):
        if 'T3o' not in self.range_selected:
            self.buttonT3o.setStyleSheet('background-color: green')
            self.range_selected.append('T3o')
        else:
            self.range_selected.remove('T3o')
            self.buttonT3o.setStyleSheet('background-color: white')

    def buttonT4s_clicked(self):
        if 'T4s' not in self.range_selected:
            self.buttonT4s.setStyleSheet('background-color: green')
            self.range_selected.append('T4s')
        else:
            self.range_selected.remove('T4s')
            self.buttonT4s.setStyleSheet('background-color: white')

    def buttonT4o_clicked(self):
        if 'T4o' not in self.range_selected:
            self.buttonT4o.setStyleSheet('background-color: green')
            self.range_selected.append('T4o')
        else:
            self.range_selected.remove('T4o')
            self.buttonT4o.setStyleSheet('background-color: white')

    def buttonT5s_clicked(self):
        if 'T5s' not in self.range_selected:
            self.buttonT5s.setStyleSheet('background-color: green')
            self.range_selected.append('T5s')
        else:
            self.range_selected.remove('T5s')
            self.buttonT5s.setStyleSheet('background-color: white')

    def buttonT5o_clicked(self):
        if 'T5o' not in self.range_selected:
            self.buttonT5o.setStyleSheet('background-color: green')
            self.range_selected.append('T5o')
        else:
            self.range_selected.remove('T5o')
            self.buttonT5o.setStyleSheet('background-color: white')

    def buttonT6s_clicked(self):
        if 'T6s' not in self.range_selected:
            self.buttonT6s.setStyleSheet('background-color: green')
            self.range_selected.append('T6s')
        else:
            self.range_selected.remove('T6s')
            self.buttonT6s.setStyleSheet('background-color: white')

    def buttonT6o_clicked(self):
        if 'T6o' not in self.range_selected:
            self.buttonT6o.setStyleSheet('background-color: green')
            self.range_selected.append('T6o')
        else:
            self.range_selected.remove('T6o')
            self.buttonT6o.setStyleSheet('background-color: white')

    def buttonT7s_clicked(self):
        if 'T7s' not in self.range_selected:
            self.buttonT7s.setStyleSheet('background-color: green')
            self.range_selected.append('T7s')
        else:
            self.range_selected.remove('T7s')
            self.buttonT7s.setStyleSheet('background-color: white')

    def buttonT7o_clicked(self):
        if 'T7o' not in self.range_selected:
            self.buttonT7o.setStyleSheet('background-color: green')
            self.range_selected.append('T7o')
        else:
            self.range_selected.remove('T7o')
            self.buttonT7o.setStyleSheet('background-color: white')

    def buttonT8s_clicked(self):
        if 'T8s' not in self.range_selected:
            self.buttonT8s.setStyleSheet('background-color: green')
            self.range_selected.append('T8s')
        else:
            self.range_selected.remove('T8s')
            self.buttonT8s.setStyleSheet('background-color: white')

    def buttonT8o_clicked(self):
        if 'T8o' not in self.range_selected:
            self.buttonT8o.setStyleSheet('background-color: green')
            self.range_selected.append('T8o')
        else:
            self.range_selected.remove('T8o')
            self.buttonT8o.setStyleSheet('background-color: white')

    def buttonT9s_clicked(self):
        if 'T9s' not in self.range_selected:
            self.buttonT9s.setStyleSheet('background-color: green')
            self.range_selected.append('T9s')
        else:
            self.range_selected.remove('T9s')
            self.buttonT9s.setStyleSheet('background-color: white')

    def buttonT9o_clicked(self):
        if 'T9o' not in self.range_selected:
            self.buttonT9o.setStyleSheet('background-color: green')
            self.range_selected.append('T9o')
        else:
            self.range_selected.remove('T9o')
            self.buttonT9o.setStyleSheet('background-color: white')

    def buttonJJ_clicked(self):
        if 'JJ' not in self.range_selected:
            self.buttonJJ.setStyleSheet('background-color: green')
            self.range_selected.append('JJ')
        else:
            self.range_selected.remove('JJ')
            self.buttonJJ.setStyleSheet('background-color: white')

    def buttonJ2s_clicked(self):
        if 'J2s' not in self.range_selected:
            self.buttonJ2s.setStyleSheet('background-color: green')
            self.range_selected.append('J2s')
        else:
            self.range_selected.remove('J2s')
            self.buttonJ2s.setStyleSheet('background-color: white')

    def buttonJ2o_clicked(self):
        if 'J2o' not in self.range_selected:
            self.buttonJ2o.setStyleSheet('background-color: green')
            self.range_selected.append('J2o')
        else:
            self.range_selected.remove('J2o')
            self.buttonJ2o.setStyleSheet('background-color: white')

    def buttonJ3s_clicked(self):
        if 'J3s' not in self.range_selected:
            self.buttonJ3s.setStyleSheet('background-color: green')
            self.range_selected.append('J3s')
        else:
            self.range_selected.remove('J3s')
            self.buttonJ3s.setStyleSheet('background-color: white')

    def buttonJ3o_clicked(self):
        if 'J3o' not in self.range_selected:
            self.buttonJ3o.setStyleSheet('background-color: green')
            self.range_selected.append('J3o')
        else:
            self.range_selected.remove('J3o')
            self.buttonJ3o.setStyleSheet('background-color: white')

    def buttonJ4s_clicked(self):
        if 'J4s' not in self.range_selected:
            self.buttonJ4s.setStyleSheet('background-color: green')
            self.range_selected.append('J4s')
        else:
            self.range_selected.remove('J4s')
            self.buttonJ4s.setStyleSheet('background-color: white')

    def buttonJ4o_clicked(self):
        if 'J4o' not in self.range_selected:
            self.buttonJ4o.setStyleSheet('background-color: green')
            self.range_selected.append('J4o')
        else:
            self.range_selected.remove('J4o')
            self.buttonJ4o.setStyleSheet('background-color: white')

    def buttonJ5s_clicked(self):
        if 'J5s' not in self.range_selected:
            self.buttonJ5s.setStyleSheet('background-color: green')
            self.range_selected.append('J5s')
        else:
            self.range_selected.remove('J5s')
            self.buttonJ5s.setStyleSheet('background-color: white')

    def buttonJ5o_clicked(self):
        if 'J5o' not in self.range_selected:
            self.buttonJ5o.setStyleSheet('background-color: green')
            self.range_selected.append('J5o')
        else:
            self.range_selected.remove('J5o')
            self.buttonJ5o.setStyleSheet('background-color: white')

    def buttonJ6s_clicked(self):
        if 'J6s' not in self.range_selected:
            self.buttonJ6s.setStyleSheet('background-color: green')
            self.range_selected.append('J6s')
        else:
            self.range_selected.remove('J6s')
            self.buttonJ6s.setStyleSheet('background-color: white')

    def buttonJ6o_clicked(self):
        if 'J6o' not in self.range_selected:
            self.buttonJ6o.setStyleSheet('background-color: green')
            self.range_selected.append('J6o')
        else:
            self.range_selected.remove('J6o')
            self.buttonJ6o.setStyleSheet('background-color: white')

    def buttonJ7s_clicked(self):
        if 'J7s' not in self.range_selected:
            self.buttonJ7s.setStyleSheet('background-color: green')
            self.range_selected.append('J7s')
        else:
            self.range_selected.remove('J7s')
            self.buttonJ7s.setStyleSheet('background-color: white')

    def buttonJ7o_clicked(self):
        if 'J7o' not in self.range_selected:
            self.buttonJ7o.setStyleSheet('background-color: green')
            self.range_selected.append('J7o')
        else:
            self.range_selected.remove('J7o')
            self.buttonJ7o.setStyleSheet('background-color: white')

    def buttonJ8s_clicked(self):
        if 'J8s' not in self.range_selected:
            self.buttonJ8s.setStyleSheet('background-color: green')
            self.range_selected.append('J8s')
        else:
            self.range_selected.remove('J8s')
            self.buttonJ8s.setStyleSheet('background-color: white')

    def buttonJ8o_clicked(self):
        if 'J8o' not in self.range_selected:
            self.buttonJ8o.setStyleSheet('background-color: green')
            self.range_selected.append('J8o')
        else:
            self.range_selected.remove('J8o')
            self.buttonJ8o.setStyleSheet('background-color: white')

    def buttonJ9s_clicked(self):
        if 'J9s' not in self.range_selected:
            self.buttonJ9s.setStyleSheet('background-color: green')
            self.range_selected.append('J9s')
        else:
            self.range_selected.remove('J9s')
            self.buttonJ9s.setStyleSheet('background-color: white')

    def buttonJ9o_clicked(self):
        if 'J9o' not in self.range_selected:
            self.buttonJ9o.setStyleSheet('background-color: green')
            self.range_selected.append('J9o')
        else:
            self.range_selected.remove('J9o')
            self.buttonJ9o.setStyleSheet('background-color: white')

    def buttonJTs_clicked(self):
        if 'JTs' not in self.range_selected:
            self.buttonJTs.setStyleSheet('background-color: green')
            self.range_selected.append('JTs')
        else:
            self.range_selected.remove('JTs')
            self.buttonJTs.setStyleSheet('background-color: white')

    def buttonJTo_clicked(self):
        if 'JTo' not in self.range_selected:
            self.buttonJTo.setStyleSheet('background-color: green')
            self.range_selected.append('JTo')
        else:
            self.range_selected.remove('JTo')
            self.buttonJTo.setStyleSheet('background-color: white')

    def buttonQQ_clicked(self):
        if 'QQ' not in self.range_selected:
            self.buttonQQ.setStyleSheet('background-color: green')
            self.range_selected.append('QQ')
        else:
            self.range_selected.remove('QQ')
            self.buttonQQ.setStyleSheet('background-color: white')

    def buttonQ2s_clicked(self):
        if 'Q2s' not in self.range_selected:
            self.buttonQ2s.setStyleSheet('background-color: green')
            self.range_selected.append('Q2s')
        else:
            self.range_selected.remove('Q2s')
            self.buttonQ2s.setStyleSheet('background-color: white')

    def buttonQ2o_clicked(self):
        if 'Q2o' not in self.range_selected:
            self.buttonQ2o.setStyleSheet('background-color: green')
            self.range_selected.append('Q2o')
        else:
            self.range_selected.remove('Q2o')
            self.buttonQ2o.setStyleSheet('background-color: white')

    def buttonQ3s_clicked(self):
        if 'Q3s' not in self.range_selected:
            self.buttonQ3s.setStyleSheet('background-color: green')
            self.range_selected.append('Q3s')
        else:
            self.range_selected.remove('Q3s')
            self.buttonQ3s.setStyleSheet('background-color: white')

    def buttonQ3o_clicked(self):
        if 'Q3o' not in self.range_selected:
            self.buttonQ3o.setStyleSheet('background-color: green')
            self.range_selected.append('Q3o')
        else:
            self.range_selected.remove('Q3o')
            self.buttonQ3o.setStyleSheet('background-color: white')

    def buttonQ4s_clicked(self):
        if 'Q4s' not in self.range_selected:
            self.buttonQ4s.setStyleSheet('background-color: green')
            self.range_selected.append('Q4s')
        else:
            self.range_selected.remove('Q4s')
            self.buttonQ4s.setStyleSheet('background-color: white')

    def buttonQ4o_clicked(self):
        if 'Q4o' not in self.range_selected:
            self.buttonQ4o.setStyleSheet('background-color: green')
            self.range_selected.append('Q4o')
        else:
            self.range_selected.remove('Q4o')
            self.buttonQ4o.setStyleSheet('background-color: white')

    def buttonQ5s_clicked(self):
        if 'Q5s' not in self.range_selected:
            self.buttonQ5s.setStyleSheet('background-color: green')
            self.range_selected.append('Q5s')
        else:
            self.range_selected.remove('Q5s')
            self.buttonQ5s.setStyleSheet('background-color: white')

    def buttonQ5o_clicked(self):
        if 'Q5o' not in self.range_selected:
            self.buttonQ5o.setStyleSheet('background-color: green')
            self.range_selected.append('Q5o')
        else:
            self.range_selected.remove('Q5o')
            self.buttonQ5o.setStyleSheet('background-color: white')

    def buttonQ6s_clicked(self):
        if 'Q6s' not in self.range_selected:
            self.buttonQ6s.setStyleSheet('background-color: green')
            self.range_selected.append('Q6s')
        else:
            self.range_selected.remove('Q6s')
            self.buttonQ6s.setStyleSheet('background-color: white')

    def buttonQ6o_clicked(self):
        if 'Q6o' not in self.range_selected:
            self.buttonQ6o.setStyleSheet('background-color: green')
            self.range_selected.append('Q6o')
        else:
            self.range_selected.remove('Q6o')
            self.buttonQ6o.setStyleSheet('background-color: white')

    def buttonQ7s_clicked(self):
        if 'Q7s' not in self.range_selected:
            self.buttonQ7s.setStyleSheet('background-color: green')
            self.range_selected.append('Q7s')
        else:
            self.range_selected.remove('Q7s')
            self.buttonQ7s.setStyleSheet('background-color: white')

    def buttonQ7o_clicked(self):
        if 'Q7o' not in self.range_selected:
            self.buttonQ7o.setStyleSheet('background-color: green')
            self.range_selected.append('Q7o')
        else:
            self.range_selected.remove('Q7o')
            self.buttonQ7o.setStyleSheet('background-color: white')

    def buttonQ8s_clicked(self):
        if 'Q8s' not in self.range_selected:
            self.buttonQ8s.setStyleSheet('background-color: green')
            self.range_selected.append('Q8s')
        else:
            self.range_selected.remove('Q8s')
            self.buttonQ8s.setStyleSheet('background-color: white')

    def buttonQ8o_clicked(self):
        if 'Q8o' not in self.range_selected:
            self.buttonQ8o.setStyleSheet('background-color: green')
            self.range_selected.append('Q8o')
        else:
            self.range_selected.remove('Q8o')
            self.buttonQ8o.setStyleSheet('background-color: white')

    def buttonQ9s_clicked(self):
        if 'Q9s' not in self.range_selected:
            self.buttonQ9s.setStyleSheet('background-color: green')
            self.range_selected.append('Q9s')
        else:
            self.range_selected.remove('Q9s')
            self.buttonQ9s.setStyleSheet('background-color: white')

    def buttonQ9o_clicked(self):
        if 'Q9o' not in self.range_selected:
            self.buttonQ9o.setStyleSheet('background-color: green')
            self.range_selected.append('Q9o')
        else:
            self.range_selected.remove('Q9o')
            self.buttonQ9o.setStyleSheet('background-color: white')

    def buttonQTs_clicked(self):
        if 'QTs' not in self.range_selected:
            self.buttonQTs.setStyleSheet('background-color: green')
            self.range_selected.append('QTs')
        else:
            self.range_selected.remove('QTs')
            self.buttonQTs.setStyleSheet('background-color: white')

    def buttonQTo_clicked(self):
        if 'QTo' not in self.range_selected:
            self.buttonQTo.setStyleSheet('background-color: green')
            self.range_selected.append('QTo')
        else:
            self.range_selected.remove('QTo')
            self.buttonQTo.setStyleSheet('background-color: white')

    def buttonQJs_clicked(self):
        if 'QJs' not in self.range_selected:
            self.buttonQJs.setStyleSheet('background-color: green')
            self.range_selected.append('QJs')
        else:
            self.range_selected.remove('QJs')
            self.buttonQJs.setStyleSheet('background-color: white')

    def buttonQJo_clicked(self):
        if 'QJo' not in self.range_selected:
            self.buttonQJo.setStyleSheet('background-color: green')
            self.range_selected.append('QJo')
        else:
            self.range_selected.remove('QJo')
            self.buttonQJo.setStyleSheet('background-color: white')

    def buttonKK_clicked(self):
        if 'KK' not in self.range_selected:
            self.buttonKK.setStyleSheet('background-color: green')
            self.range_selected.append('KK')
        else:
            self.range_selected.remove('KK')
            self.buttonKK.setStyleSheet('background-color: white')

    def buttonK2s_clicked(self):
        if 'K2s' not in self.range_selected:
            self.buttonK2s.setStyleSheet('background-color: green')
            self.range_selected.append('K2s')
        else:
            self.range_selected.remove('K2s')
            self.buttonK2s.setStyleSheet('background-color: white')

    def buttonK2o_clicked(self):
        if 'K2o' not in self.range_selected:
            self.buttonK2o.setStyleSheet('background-color: green')
            self.range_selected.append('K2o')
        else:
            self.range_selected.remove('K2o')
            self.buttonK2o.setStyleSheet('background-color: white')

    def buttonK3s_clicked(self):
        if 'K3s' not in self.range_selected:
            self.buttonK3s.setStyleSheet('background-color: green')
            self.range_selected.append('K3s')
        else:
            self.range_selected.remove('K3s')
            self.buttonK3s.setStyleSheet('background-color: white')

    def buttonK3o_clicked(self):
        if 'K3o' not in self.range_selected:
            self.buttonK3o.setStyleSheet('background-color: green')
            self.range_selected.append('K3o')
        else:
            self.range_selected.remove('K3o')
            self.buttonK3o.setStyleSheet('background-color: white')

    def buttonK4s_clicked(self):
        if 'K4s' not in self.range_selected:
            self.buttonK4s.setStyleSheet('background-color: green')
            self.range_selected.append('K4s')
        else:
            self.range_selected.remove('K4s')
            self.buttonK4s.setStyleSheet('background-color: white')

    def buttonK4o_clicked(self):
        if 'K4o' not in self.range_selected:
            self.buttonK4o.setStyleSheet('background-color: green')
            self.range_selected.append('K4o')
        else:
            self.range_selected.remove('K4o')
            self.buttonK4o.setStyleSheet('background-color: white')

    def buttonK5s_clicked(self):
        if 'K5s' not in self.range_selected:
            self.buttonK5s.setStyleSheet('background-color: green')
            self.range_selected.append('K5s')
        else:
            self.range_selected.remove('K5s')
            self.buttonK5s.setStyleSheet('background-color: white')

    def buttonK5o_clicked(self):
        if 'K5o' not in self.range_selected:
            self.buttonK5o.setStyleSheet('background-color: green')
            self.range_selected.append('K5o')
        else:
            self.range_selected.remove('K5o')
            self.buttonK5o.setStyleSheet('background-color: white')

    def buttonK6s_clicked(self):
        if 'K6s' not in self.range_selected:
            self.buttonK6s.setStyleSheet('background-color: green')
            self.range_selected.append('K6s')
        else:
            self.range_selected.remove('K6s')
            self.buttonK6s.setStyleSheet('background-color: white')

    def buttonK6o_clicked(self):
        if 'K6o' not in self.range_selected:
            self.buttonK6o.setStyleSheet('background-color: green')
            self.range_selected.append('K6o')
        else:
            self.range_selected.remove('K6o')
            self.buttonK6o.setStyleSheet('background-color: white')

    def buttonK7s_clicked(self):
        if 'K7s' not in self.range_selected:
            self.buttonK7s.setStyleSheet('background-color: green')
            self.range_selected.append('K7s')
        else:
            self.range_selected.remove('K7s')
            self.buttonK7s.setStyleSheet('background-color: white')

    def buttonK7o_clicked(self):
        if 'K7o' not in self.range_selected:
            self.buttonK7o.setStyleSheet('background-color: green')
            self.range_selected.append('K7o')
        else:
            self.range_selected.remove('K7o')
            self.buttonK7o.setStyleSheet('background-color: white')

    def buttonK8s_clicked(self):
        if 'K8s' not in self.range_selected:
            self.buttonK8s.setStyleSheet('background-color: green')
            self.range_selected.append('K8s')
        else:
            self.range_selected.remove('K8s')
            self.buttonK8s.setStyleSheet('background-color: white')

    def buttonK8o_clicked(self):
        if 'K8o' not in self.range_selected:
            self.buttonK8o.setStyleSheet('background-color: green')
            self.range_selected.append('K8o')
        else:
            self.range_selected.remove('K8o')
            self.buttonK8o.setStyleSheet('background-color: white')

    def buttonK9s_clicked(self):
        if 'K9s' not in self.range_selected:
            self.buttonK9s.setStyleSheet('background-color: green')
            self.range_selected.append('K9s')
        else:
            self.range_selected.remove('K9s')
            self.buttonK9s.setStyleSheet('background-color: white')

    def buttonK9o_clicked(self):
        if 'K9o' not in self.range_selected:
            self.buttonK9o.setStyleSheet('background-color: green')
            self.range_selected.append('K9o')
        else:
            self.range_selected.remove('K9o')
            self.buttonK9o.setStyleSheet('background-color: white')

    def buttonKTs_clicked(self):
        if 'KTs' not in self.range_selected:
            self.buttonKTs.setStyleSheet('background-color: green')
            self.range_selected.append('KTs')
        else:
            self.range_selected.remove('KTs')
            self.buttonKTs.setStyleSheet('background-color: white')

    def buttonKTo_clicked(self):
        if 'KTo' not in self.range_selected:
            self.buttonKTo.setStyleSheet('background-color: green')
            self.range_selected.append('KTo')
        else:
            self.range_selected.remove('KTo')
            self.buttonKTo.setStyleSheet('background-color: white')

    def buttonKJs_clicked(self):
        if 'KJs' not in self.range_selected:
            self.buttonKJs.setStyleSheet('background-color: green')
            self.range_selected.append('KJs')
        else:
            self.range_selected.remove('KJs')
            self.buttonKJs.setStyleSheet('background-color: white')

    def buttonKJo_clicked(self):
        if 'KJo' not in self.range_selected:
            self.buttonKJo.setStyleSheet('background-color: green')
            self.range_selected.append('KJo')
        else:
            self.range_selected.remove('KJo')
            self.buttonKJo.setStyleSheet('background-color: white')

    def buttonKQs_clicked(self):
        if 'KQs' not in self.range_selected:
            self.buttonKQs.setStyleSheet('background-color: green')
            self.range_selected.append('KQs')
        else:
            self.range_selected.remove('KQs')
            self.buttonKQs.setStyleSheet('background-color: white')

    def buttonKQo_clicked(self):
        if 'KQo' not in self.range_selected:
            self.buttonKQo.setStyleSheet('background-color: green')
            self.range_selected.append('KQo')
        else:
            self.range_selected.remove('KQo')
            self.buttonKQo.setStyleSheet('background-color: white')

    def buttonAA_clicked(self):
        if 'AA' not in self.range_selected:
            self.buttonAA.setStyleSheet('background-color: green')
            self.range_selected.append('AA')
        else:
            self.range_selected.remove('AA')
            self.buttonAA.setStyleSheet('background-color: white')

    def buttonA2s_clicked(self):
        if 'A2s' not in self.range_selected:
            self.buttonA2s.setStyleSheet('background-color: green')
            self.range_selected.append('A2s')
        else:
            self.range_selected.remove('A2s')
            self.buttonA2s.setStyleSheet('background-color: white')

    def buttonA2o_clicked(self):
        if 'A2o' not in self.range_selected:
            self.buttonA2o.setStyleSheet('background-color: green')
            self.range_selected.append('A2o')
        else:
            self.range_selected.remove('A2o')
            self.buttonA2o.setStyleSheet('background-color: white')

    def buttonA3s_clicked(self):
        if 'A3s' not in self.range_selected:
            self.buttonA3s.setStyleSheet('background-color: green')
            self.range_selected.append('A3s')
        else:
            self.range_selected.remove('A3s')
            self.buttonA3s.setStyleSheet('background-color: white')

    def buttonA3o_clicked(self):
        if 'A3o' not in self.range_selected:
            self.buttonA3o.setStyleSheet('background-color: green')
            self.range_selected.append('A3o')
        else:
            self.range_selected.remove('A3o')
            self.buttonA3o.setStyleSheet('background-color: white')

    def buttonA4s_clicked(self):
        if 'A4s' not in self.range_selected:
            self.buttonA4s.setStyleSheet('background-color: green')
            self.range_selected.append('A4s')
        else:
            self.range_selected.remove('A4s')
            self.buttonA4s.setStyleSheet('background-color: white')

    def buttonA4o_clicked(self):
        if 'A4o' not in self.range_selected:
            self.buttonA4o.setStyleSheet('background-color: green')
            self.range_selected.append('A4o')
        else:
            self.range_selected.remove('A4o')
            self.buttonA4o.setStyleSheet('background-color: white')

    def buttonA5s_clicked(self):
        if 'A5s' not in self.range_selected:
            self.buttonA5s.setStyleSheet('background-color: green')
            self.range_selected.append('A5s')
        else:
            self.range_selected.remove('A5s')
            self.buttonA5s.setStyleSheet('background-color: white')

    def buttonA5o_clicked(self):
        if 'A5o' not in self.range_selected:
            self.buttonA5o.setStyleSheet('background-color: green')
            self.range_selected.append('A5o')
        else:
            self.range_selected.remove('A5o')
            self.buttonA5o.setStyleSheet('background-color: white')

    def buttonA6s_clicked(self):
        if 'A6s' not in self.range_selected:
            self.buttonA6s.setStyleSheet('background-color: green')
            self.range_selected.append('A6s')
        else:
            self.range_selected.remove('A6s')
            self.buttonA6s.setStyleSheet('background-color: white')

    def buttonA6o_clicked(self):
        if 'A6o' not in self.range_selected:
            self.buttonA6o.setStyleSheet('background-color: green')
            self.range_selected.append('A6o')
        else:
            self.range_selected.remove('A6o')
            self.buttonA6o.setStyleSheet('background-color: white')

    def buttonA7s_clicked(self):
        if 'A7s' not in self.range_selected:
            self.buttonA7s.setStyleSheet('background-color: green')
            self.range_selected.append('A7s')
        else:
            self.range_selected.remove('A7s')
            self.buttonA7s.setStyleSheet('background-color: white')

    def buttonA7o_clicked(self):
        if 'A7o' not in self.range_selected:
            self.buttonA7o.setStyleSheet('background-color: green')
            self.range_selected.append('A7o')
        else:
            self.range_selected.remove('A7o')
            self.buttonA7o.setStyleSheet('background-color: white')

    def buttonA8s_clicked(self):
        if 'A8s' not in self.range_selected:
            self.buttonA8s.setStyleSheet('background-color: green')
            self.range_selected.append('A8s')
        else:
            self.range_selected.remove('A8s')
            self.buttonA8s.setStyleSheet('background-color: white')

    def buttonA8o_clicked(self):
        if 'A8o' not in self.range_selected:
            self.buttonA8o.setStyleSheet('background-color: green')
            self.range_selected.append('A8o')
        else:
            self.range_selected.remove('A8o')
            self.buttonA8o.setStyleSheet('background-color: white')

    def buttonA9s_clicked(self):
        if 'A9s' not in self.range_selected:
            self.buttonA9s.setStyleSheet('background-color: green')
            self.range_selected.append('A9s')
        else:
            self.range_selected.remove('A9s')
            self.buttonA9s.setStyleSheet('background-color: white')

    def buttonA9o_clicked(self):
        if 'A9o' not in self.range_selected:
            self.buttonA9o.setStyleSheet('background-color: green')
            self.range_selected.append('A9o')
        else:
            self.range_selected.remove('A9o')
            self.buttonA9o.setStyleSheet('background-color: white')

    def buttonATs_clicked(self):
        if 'ATs' not in self.range_selected:
            self.buttonATs.setStyleSheet('background-color: green')
            self.range_selected.append('ATs')
        else:
            self.range_selected.remove('ATs')
            self.buttonATs.setStyleSheet('background-color: white')

    def buttonATo_clicked(self):
        if 'ATo' not in self.range_selected:
            self.buttonATo.setStyleSheet('background-color: green')
            self.range_selected.append('ATo')
        else:
            self.range_selected.remove('ATo')
            self.buttonATo.setStyleSheet('background-color: white')

    def buttonAJs_clicked(self):
        if 'AJs' not in self.range_selected:
            self.buttonAJs.setStyleSheet('background-color: green')
            self.range_selected.append('AJs')
        else:
            self.range_selected.remove('AJs')
            self.buttonAJs.setStyleSheet('background-color: white')

    def buttonAJo_clicked(self):
        if 'AJo' not in self.range_selected:
            self.buttonAJo.setStyleSheet('background-color: green')
            self.range_selected.append('AJo')
        else:
            self.range_selected.remove('AJo')
            self.buttonAJo.setStyleSheet('background-color: white')

    def buttonAQs_clicked(self):
        if 'AQs' not in self.range_selected:
            self.buttonAQs.setStyleSheet('background-color: green')
            self.range_selected.append('AQs')
        else:
            self.range_selected.remove('AQs')
            self.buttonAQs.setStyleSheet('background-color: white')

    def buttonAQo_clicked(self):
        if 'AQo' not in self.range_selected:
            self.buttonAQo.setStyleSheet('background-color: green')
            self.range_selected.append('AQo')
        else:
            self.range_selected.remove('AQo')
            self.buttonAQo.setStyleSheet('background-color: white')

    def buttonAKs_clicked(self):
        if 'AKs' not in self.range_selected:
            self.buttonAKs.setStyleSheet('background-color: green')
            self.range_selected.append('AKs')
        else:
            self.range_selected.remove('AKs')
            self.buttonAKs.setStyleSheet('background-color: white')

    def buttonAKo_clicked(self):
        if 'AKo' not in self.range_selected:
            self.buttonAKo.setStyleSheet('background-color: green')
            self.range_selected.append('AKo')
        else:
            self.range_selected.remove('AKo')
            self.buttonAKo.setStyleSheet('background-color: white')

    def color_buttons(self):
        if '22' in self.range_selected:
            self.button22.setStyleSheet('background-color: green')
        else:
            self.button22.setStyleSheet('background-color: white')
        if '33' in self.range_selected:
            self.button33.setStyleSheet('background-color: green')
        else:
            self.button33.setStyleSheet('background-color: white')
        if '32s' in self.range_selected:
            self.button32s.setStyleSheet('background-color: green')
        else:
            self.button32s.setStyleSheet('background-color: white')
        if '32o' in self.range_selected:
            self.button32o.setStyleSheet('background-color: green')
        else:
            self.button32o.setStyleSheet('background-color: white')
        if '44' in self.range_selected:
            self.button44.setStyleSheet('background-color: green')
        else:
            self.button44.setStyleSheet('background-color: white')
        if '42s' in self.range_selected:
            self.button42s.setStyleSheet('background-color: green')
        else:
            self.button42s.setStyleSheet('background-color: white')
        if '42o' in self.range_selected:
            self.button42o.setStyleSheet('background-color: green')
        else:
            self.button42o.setStyleSheet('background-color: white')
        if '43s' in self.range_selected:
            self.button43s.setStyleSheet('background-color: green')
        else:
            self.button43s.setStyleSheet('background-color: white')
        if '43o' in self.range_selected:
            self.button43o.setStyleSheet('background-color: green')
        else:
            self.button43o.setStyleSheet('background-color: white')
        if '55' in self.range_selected:
            self.button55.setStyleSheet('background-color: green')
        else:
            self.button55.setStyleSheet('background-color: white')
        if '52s' in self.range_selected:
            self.button52s.setStyleSheet('background-color: green')
        else:
            self.button52s.setStyleSheet('background-color: white')
        if '52o' in self.range_selected:
            self.button52o.setStyleSheet('background-color: green')
        else:
            self.button52o.setStyleSheet('background-color: white')
        if '53s' in self.range_selected:
            self.button53s.setStyleSheet('background-color: green')
        else:
            self.button53s.setStyleSheet('background-color: white')
        if '53o' in self.range_selected:
            self.button53o.setStyleSheet('background-color: green')
        else:
            self.button53o.setStyleSheet('background-color: white')
        if '54s' in self.range_selected:
            self.button54s.setStyleSheet('background-color: green')
        else:
            self.button54s.setStyleSheet('background-color: white')
        if '54o' in self.range_selected:
            self.button54o.setStyleSheet('background-color: green')
        else:
            self.button54o.setStyleSheet('background-color: white')
        if '66' in self.range_selected:
            self.button66.setStyleSheet('background-color: green')
        else:
            self.button66.setStyleSheet('background-color: white')
        if '62s' in self.range_selected:
            self.button62s.setStyleSheet('background-color: green')
        else:
            self.button62s.setStyleSheet('background-color: white')
        if '62o' in self.range_selected:
            self.button62o.setStyleSheet('background-color: green')
        else:
            self.button62o.setStyleSheet('background-color: white')
        if '63s' in self.range_selected:
            self.button63s.setStyleSheet('background-color: green')
        else:
            self.button63s.setStyleSheet('background-color: white')
        if '63o' in self.range_selected:
            self.button63o.setStyleSheet('background-color: green')
        else:
            self.button63o.setStyleSheet('background-color: white')
        if '64s' in self.range_selected:
            self.button64s.setStyleSheet('background-color: green')
        else:
            self.button64s.setStyleSheet('background-color: white')
        if '64o' in self.range_selected:
            self.button64o.setStyleSheet('background-color: green')
        else:
            self.button64o.setStyleSheet('background-color: white')
        if '65s' in self.range_selected:
            self.button65s.setStyleSheet('background-color: green')
        else:
            self.button65s.setStyleSheet('background-color: white')
        if '65o' in self.range_selected:
            self.button65o.setStyleSheet('background-color: green')
        else:
            self.button65o.setStyleSheet('background-color: white')
        if '77' in self.range_selected:
            self.button77.setStyleSheet('background-color: green')
        else:
            self.button77.setStyleSheet('background-color: white')
        if '72s' in self.range_selected:
            self.button72s.setStyleSheet('background-color: green')
        else:
            self.button72s.setStyleSheet('background-color: white')
        if '72o' in self.range_selected:
            self.button72o.setStyleSheet('background-color: green')
        else:
            self.button72o.setStyleSheet('background-color: white')
        if '73s' in self.range_selected:
            self.button73s.setStyleSheet('background-color: green')
        else:
            self.button73s.setStyleSheet('background-color: white')
        if '73o' in self.range_selected:
            self.button73o.setStyleSheet('background-color: green')
        else:
            self.button73o.setStyleSheet('background-color: white')
        if '74s' in self.range_selected:
            self.button74s.setStyleSheet('background-color: green')
        else:
            self.button74s.setStyleSheet('background-color: white')
        if '74o' in self.range_selected:
            self.button74o.setStyleSheet('background-color: green')
        else:
            self.button74o.setStyleSheet('background-color: white')
        if '75s' in self.range_selected:
            self.button75s.setStyleSheet('background-color: green')
        else:
            self.button75s.setStyleSheet('background-color: white')
        if '75o' in self.range_selected:
            self.button75o.setStyleSheet('background-color: green')
        else:
            self.button75o.setStyleSheet('background-color: white')
        if '76s' in self.range_selected:
            self.button76s.setStyleSheet('background-color: green')
        else:
            self.button76s.setStyleSheet('background-color: white')
        if '76o' in self.range_selected:
            self.button76o.setStyleSheet('background-color: green')
        else:
            self.button76o.setStyleSheet('background-color: white')
        if '88' in self.range_selected:
            self.button88.setStyleSheet('background-color: green')
        else:
            self.button88.setStyleSheet('background-color: white')
        if '82s' in self.range_selected:
            self.button82s.setStyleSheet('background-color: green')
        else:
            self.button82s.setStyleSheet('background-color: white')
        if '82o' in self.range_selected:
            self.button82o.setStyleSheet('background-color: green')
        else:
            self.button82o.setStyleSheet('background-color: white')
        if '83s' in self.range_selected:
            self.button83s.setStyleSheet('background-color: green')
        else:
            self.button83s.setStyleSheet('background-color: white')
        if '83o' in self.range_selected:
            self.button83o.setStyleSheet('background-color: green')
        else:
            self.button83o.setStyleSheet('background-color: white')
        if '84s' in self.range_selected:
            self.button84s.setStyleSheet('background-color: green')
        else:
            self.button84s.setStyleSheet('background-color: white')
        if '84o' in self.range_selected:
            self.button84o.setStyleSheet('background-color: green')
        else:
            self.button84o.setStyleSheet('background-color: white')
        if '85s' in self.range_selected:
            self.button85s.setStyleSheet('background-color: green')
        else:
            self.button85s.setStyleSheet('background-color: white')
        if '85o' in self.range_selected:
            self.button85o.setStyleSheet('background-color: green')
        else:
            self.button85o.setStyleSheet('background-color: white')
        if '86s' in self.range_selected:
            self.button86s.setStyleSheet('background-color: green')
        else:
            self.button86s.setStyleSheet('background-color: white')
        if '86o' in self.range_selected:
            self.button86o.setStyleSheet('background-color: green')
        else:
            self.button86o.setStyleSheet('background-color: white')
        if '87s' in self.range_selected:
            self.button87s.setStyleSheet('background-color: green')
        else:
            self.button87s.setStyleSheet('background-color: white')
        if '87o' in self.range_selected:
            self.button87o.setStyleSheet('background-color: green')
        else:
            self.button87o.setStyleSheet('background-color: white')
        if '99' in self.range_selected:
            self.button99.setStyleSheet('background-color: green')
        else:
            self.button99.setStyleSheet('background-color: white')
        if '92s' in self.range_selected:
            self.button92s.setStyleSheet('background-color: green')
        else:
            self.button92s.setStyleSheet('background-color: white')
        if '92o' in self.range_selected:
            self.button92o.setStyleSheet('background-color: green')
        else:
            self.button92o.setStyleSheet('background-color: white')
        if '93s' in self.range_selected:
            self.button93s.setStyleSheet('background-color: green')
        else:
            self.button93s.setStyleSheet('background-color: white')
        if '93o' in self.range_selected:
            self.button93o.setStyleSheet('background-color: green')
        else:
            self.button93o.setStyleSheet('background-color: white')
        if '94s' in self.range_selected:
            self.button94s.setStyleSheet('background-color: green')
        else:
            self.button94s.setStyleSheet('background-color: white')
        if '94o' in self.range_selected:
            self.button94o.setStyleSheet('background-color: green')
        else:
            self.button94o.setStyleSheet('background-color: white')
        if '95s' in self.range_selected:
            self.button95s.setStyleSheet('background-color: green')
        else:
            self.button95s.setStyleSheet('background-color: white')
        if '95o' in self.range_selected:
            self.button95o.setStyleSheet('background-color: green')
        else:
            self.button95o.setStyleSheet('background-color: white')
        if '96s' in self.range_selected:
            self.button96s.setStyleSheet('background-color: green')
        else:
            self.button96s.setStyleSheet('background-color: white')
        if '96o' in self.range_selected:
            self.button96o.setStyleSheet('background-color: green')
        else:
            self.button96o.setStyleSheet('background-color: white')
        if '97s' in self.range_selected:
            self.button97s.setStyleSheet('background-color: green')
        else:
            self.button97s.setStyleSheet('background-color: white')
        if '97o' in self.range_selected:
            self.button97o.setStyleSheet('background-color: green')
        else:
            self.button97o.setStyleSheet('background-color: white')
        if '98s' in self.range_selected:
            self.button98s.setStyleSheet('background-color: green')
        else:
            self.button98s.setStyleSheet('background-color: white')
        if '98o' in self.range_selected:
            self.button98o.setStyleSheet('background-color: green')
        else:
            self.button98o.setStyleSheet('background-color: white')
        if 'TT' in self.range_selected:
            self.buttonTT.setStyleSheet('background-color: green')
        else:
            self.buttonTT.setStyleSheet('background-color: white')
        if 'T2s' in self.range_selected:
            self.buttonT2s.setStyleSheet('background-color: green')
        else:
            self.buttonT2s.setStyleSheet('background-color: white')
        if 'T2o' in self.range_selected:
            self.buttonT2o.setStyleSheet('background-color: green')
        else:
            self.buttonT2o.setStyleSheet('background-color: white')
        if 'T3s' in self.range_selected:
            self.buttonT3s.setStyleSheet('background-color: green')
        else:
            self.buttonT3s.setStyleSheet('background-color: white')
        if 'T3o' in self.range_selected:
            self.buttonT3o.setStyleSheet('background-color: green')
        else:
            self.buttonT3o.setStyleSheet('background-color: white')
        if 'T4s' in self.range_selected:
            self.buttonT4s.setStyleSheet('background-color: green')
        else:
            self.buttonT4s.setStyleSheet('background-color: white')
        if 'T4o' in self.range_selected:
            self.buttonT4o.setStyleSheet('background-color: green')
        else:
            self.buttonT4o.setStyleSheet('background-color: white')
        if 'T5s' in self.range_selected:
            self.buttonT5s.setStyleSheet('background-color: green')
        else:
            self.buttonT5s.setStyleSheet('background-color: white')
        if 'T5o' in self.range_selected:
            self.buttonT5o.setStyleSheet('background-color: green')
        else:
            self.buttonT5o.setStyleSheet('background-color: white')
        if 'T6s' in self.range_selected:
            self.buttonT6s.setStyleSheet('background-color: green')
        else:
            self.buttonT6s.setStyleSheet('background-color: white')
        if 'T6o' in self.range_selected:
            self.buttonT6o.setStyleSheet('background-color: green')
        else:
            self.buttonT6o.setStyleSheet('background-color: white')
        if 'T7s' in self.range_selected:
            self.buttonT7s.setStyleSheet('background-color: green')
        else:
            self.buttonT7s.setStyleSheet('background-color: white')
        if 'T7o' in self.range_selected:
            self.buttonT7o.setStyleSheet('background-color: green')
        else:
            self.buttonT7o.setStyleSheet('background-color: white')
        if 'T8s' in self.range_selected:
            self.buttonT8s.setStyleSheet('background-color: green')
        else:
            self.buttonT8s.setStyleSheet('background-color: white')
        if 'T8o' in self.range_selected:
            self.buttonT8o.setStyleSheet('background-color: green')
        else:
            self.buttonT8o.setStyleSheet('background-color: white')
        if 'T9s' in self.range_selected:
            self.buttonT9s.setStyleSheet('background-color: green')
        else:
            self.buttonT9s.setStyleSheet('background-color: white')
        if 'T9o' in self.range_selected:
            self.buttonT9o.setStyleSheet('background-color: green')
        else:
            self.buttonT9o.setStyleSheet('background-color: white')
        if 'JJ' in self.range_selected:
            self.buttonJJ.setStyleSheet('background-color: green')
        else:
            self.buttonJJ.setStyleSheet('background-color: white')
        if 'J2s' in self.range_selected:
            self.buttonJ2s.setStyleSheet('background-color: green')
        else:
            self.buttonJ2s.setStyleSheet('background-color: white')
        if 'J2o' in self.range_selected:
            self.buttonJ2o.setStyleSheet('background-color: green')
        else:
            self.buttonJ2o.setStyleSheet('background-color: white')
        if 'J3s' in self.range_selected:
            self.buttonJ3s.setStyleSheet('background-color: green')
        else:
            self.buttonJ3s.setStyleSheet('background-color: white')
        if 'J3o' in self.range_selected:
            self.buttonJ3o.setStyleSheet('background-color: green')
        else:
            self.buttonJ3o.setStyleSheet('background-color: white')
        if 'J4s' in self.range_selected:
            self.buttonJ4s.setStyleSheet('background-color: green')
        else:
            self.buttonJ4s.setStyleSheet('background-color: white')
        if 'J4o' in self.range_selected:
            self.buttonJ4o.setStyleSheet('background-color: green')
        else:
            self.buttonJ4o.setStyleSheet('background-color: white')
        if 'J5s' in self.range_selected:
            self.buttonJ5s.setStyleSheet('background-color: green')
        else:
            self.buttonJ5s.setStyleSheet('background-color: white')
        if 'J5o' in self.range_selected:
            self.buttonJ5o.setStyleSheet('background-color: green')
        else:
            self.buttonJ5o.setStyleSheet('background-color: white')
        if 'J6s' in self.range_selected:
            self.buttonJ6s.setStyleSheet('background-color: green')
        else:
            self.buttonJ6s.setStyleSheet('background-color: white')
        if 'J6o' in self.range_selected:
            self.buttonJ6o.setStyleSheet('background-color: green')
        else:
            self.buttonJ6o.setStyleSheet('background-color: white')
        if 'J7s' in self.range_selected:
            self.buttonJ7s.setStyleSheet('background-color: green')
        else:
            self.buttonJ7s.setStyleSheet('background-color: white')
        if 'J7o' in self.range_selected:
            self.buttonJ7o.setStyleSheet('background-color: green')
        else:
            self.buttonJ7o.setStyleSheet('background-color: white')
        if 'J8s' in self.range_selected:
            self.buttonJ8s.setStyleSheet('background-color: green')
        else:
            self.buttonJ8s.setStyleSheet('background-color: white')
        if 'J8o' in self.range_selected:
            self.buttonJ8o.setStyleSheet('background-color: green')
        else:
            self.buttonJ8o.setStyleSheet('background-color: white')
        if 'J9s' in self.range_selected:
            self.buttonJ9s.setStyleSheet('background-color: green')
        else:
            self.buttonJ9s.setStyleSheet('background-color: white')
        if 'J9o' in self.range_selected:
            self.buttonJ9o.setStyleSheet('background-color: green')
        else:
            self.buttonJ9o.setStyleSheet('background-color: white')
        if 'JTs' in self.range_selected:
            self.buttonJTs.setStyleSheet('background-color: green')
        else:
            self.buttonJTs.setStyleSheet('background-color: white')
        if 'JTo' in self.range_selected:
            self.buttonJTo.setStyleSheet('background-color: green')
        else:
            self.buttonJTo.setStyleSheet('background-color: white')
        if 'QQ' in self.range_selected:
            self.buttonQQ.setStyleSheet('background-color: green')
        else:
            self.buttonQQ.setStyleSheet('background-color: white')
        if 'Q2s' in self.range_selected:
            self.buttonQ2s.setStyleSheet('background-color: green')
        else:
            self.buttonQ2s.setStyleSheet('background-color: white')
        if 'Q2o' in self.range_selected:
            self.buttonQ2o.setStyleSheet('background-color: green')
        else:
            self.buttonQ2o.setStyleSheet('background-color: white')
        if 'Q3s' in self.range_selected:
            self.buttonQ3s.setStyleSheet('background-color: green')
        else:
            self.buttonQ3s.setStyleSheet('background-color: white')
        if 'Q3o' in self.range_selected:
            self.buttonQ3o.setStyleSheet('background-color: green')
        else:
            self.buttonQ3o.setStyleSheet('background-color: white')
        if 'Q4s' in self.range_selected:
            self.buttonQ4s.setStyleSheet('background-color: green')
        else:
            self.buttonQ4s.setStyleSheet('background-color: white')
        if 'Q4o' in self.range_selected:
            self.buttonQ4o.setStyleSheet('background-color: green')
        else:
            self.buttonQ4o.setStyleSheet('background-color: white')
        if 'Q5s' in self.range_selected:
            self.buttonQ5s.setStyleSheet('background-color: green')
        else:
            self.buttonQ5s.setStyleSheet('background-color: white')
        if 'Q5o' in self.range_selected:
            self.buttonQ5o.setStyleSheet('background-color: green')
        else:
            self.buttonQ5o.setStyleSheet('background-color: white')
        if 'Q6s' in self.range_selected:
            self.buttonQ6s.setStyleSheet('background-color: green')
        else:
            self.buttonQ6s.setStyleSheet('background-color: white')
        if 'Q6o' in self.range_selected:
            self.buttonQ6o.setStyleSheet('background-color: green')
        else:
            self.buttonQ6o.setStyleSheet('background-color: white')
        if 'Q7s' in self.range_selected:
            self.buttonQ7s.setStyleSheet('background-color: green')
        else:
            self.buttonQ7s.setStyleSheet('background-color: white')
        if 'Q7o' in self.range_selected:
            self.buttonQ7o.setStyleSheet('background-color: green')
        else:
            self.buttonQ7o.setStyleSheet('background-color: white')
        if 'Q8s' in self.range_selected:
            self.buttonQ8s.setStyleSheet('background-color: green')
        else:
            self.buttonQ8s.setStyleSheet('background-color: white')
        if 'Q8o' in self.range_selected:
            self.buttonQ8o.setStyleSheet('background-color: green')
        else:
            self.buttonQ8o.setStyleSheet('background-color: white')
        if 'Q9s' in self.range_selected:
            self.buttonQ9s.setStyleSheet('background-color: green')
        else:
            self.buttonQ9s.setStyleSheet('background-color: white')
        if 'Q9o' in self.range_selected:
            self.buttonQ9o.setStyleSheet('background-color: green')
        else:
            self.buttonQ9o.setStyleSheet('background-color: white')
        if 'QTs' in self.range_selected:
            self.buttonQTs.setStyleSheet('background-color: green')
        else:
            self.buttonQTs.setStyleSheet('background-color: white')
        if 'QTo' in self.range_selected:
            self.buttonQTo.setStyleSheet('background-color: green')
        else:
            self.buttonQTo.setStyleSheet('background-color: white')
        if 'QJs' in self.range_selected:
            self.buttonQJs.setStyleSheet('background-color: green')
        else:
            self.buttonQJs.setStyleSheet('background-color: white')
        if 'QJo' in self.range_selected:
            self.buttonQJo.setStyleSheet('background-color: green')
        else:
            self.buttonQJo.setStyleSheet('background-color: white')
        if 'KK' in self.range_selected:
            self.buttonKK.setStyleSheet('background-color: green')
        else:
            self.buttonKK.setStyleSheet('background-color: white')
        if 'K2s' in self.range_selected:
            self.buttonK2s.setStyleSheet('background-color: green')
        else:
            self.buttonK2s.setStyleSheet('background-color: white')
        if 'K2o' in self.range_selected:
            self.buttonK2o.setStyleSheet('background-color: green')
        else:
            self.buttonK2o.setStyleSheet('background-color: white')
        if 'K3s' in self.range_selected:
            self.buttonK3s.setStyleSheet('background-color: green')
        else:
            self.buttonK3s.setStyleSheet('background-color: white')
        if 'K3o' in self.range_selected:
            self.buttonK3o.setStyleSheet('background-color: green')
        else:
            self.buttonK3o.setStyleSheet('background-color: white')
        if 'K4s' in self.range_selected:
            self.buttonK4s.setStyleSheet('background-color: green')
        else:
            self.buttonK4s.setStyleSheet('background-color: white')
        if 'K4o' in self.range_selected:
            self.buttonK4o.setStyleSheet('background-color: green')
        else:
            self.buttonK4o.setStyleSheet('background-color: white')
        if 'K5s' in self.range_selected:
            self.buttonK5s.setStyleSheet('background-color: green')
        else:
            self.buttonK5s.setStyleSheet('background-color: white')
        if 'K5o' in self.range_selected:
            self.buttonK5o.setStyleSheet('background-color: green')
        else:
            self.buttonK5o.setStyleSheet('background-color: white')
        if 'K6s' in self.range_selected:
            self.buttonK6s.setStyleSheet('background-color: green')
        else:
            self.buttonK6s.setStyleSheet('background-color: white')
        if 'K6o' in self.range_selected:
            self.buttonK6o.setStyleSheet('background-color: green')
        else:
            self.buttonK6o.setStyleSheet('background-color: white')
        if 'K7s' in self.range_selected:
            self.buttonK7s.setStyleSheet('background-color: green')
        else:
            self.buttonK7s.setStyleSheet('background-color: white')
        if 'K7o' in self.range_selected:
            self.buttonK7o.setStyleSheet('background-color: green')
        else:
            self.buttonK7o.setStyleSheet('background-color: white')
        if 'K8s' in self.range_selected:
            self.buttonK8s.setStyleSheet('background-color: green')
        else:
            self.buttonK8s.setStyleSheet('background-color: white')
        if 'K8o' in self.range_selected:
            self.buttonK8o.setStyleSheet('background-color: green')
        else:
            self.buttonK8o.setStyleSheet('background-color: white')
        if 'K9s' in self.range_selected:
            self.buttonK9s.setStyleSheet('background-color: green')
        else:
            self.buttonK9s.setStyleSheet('background-color: white')
        if 'K9o' in self.range_selected:
            self.buttonK9o.setStyleSheet('background-color: green')
        else:
            self.buttonK9o.setStyleSheet('background-color: white')
        if 'KTs' in self.range_selected:
            self.buttonKTs.setStyleSheet('background-color: green')
        else:
            self.buttonKTs.setStyleSheet('background-color: white')
        if 'KTo' in self.range_selected:
            self.buttonKTo.setStyleSheet('background-color: green')
        else:
            self.buttonKTo.setStyleSheet('background-color: white')
        if 'KJs' in self.range_selected:
            self.buttonKJs.setStyleSheet('background-color: green')
        else:
            self.buttonKJs.setStyleSheet('background-color: white')
        if 'KJo' in self.range_selected:
            self.buttonKJo.setStyleSheet('background-color: green')
        else:
            self.buttonKJo.setStyleSheet('background-color: white')
        if 'KQs' in self.range_selected:
            self.buttonKQs.setStyleSheet('background-color: green')
        else:
            self.buttonKQs.setStyleSheet('background-color: white')
        if 'KQo' in self.range_selected:
            self.buttonKQo.setStyleSheet('background-color: green')
        else:
            self.buttonKQo.setStyleSheet('background-color: white')
        if 'AA' in self.range_selected:
            self.buttonAA.setStyleSheet('background-color: green')
        else:
            self.buttonAA.setStyleSheet('background-color: white')
        if 'A2s' in self.range_selected:
            self.buttonA2s.setStyleSheet('background-color: green')
        else:
            self.buttonA2s.setStyleSheet('background-color: white')
        if 'A2o' in self.range_selected:
            self.buttonA2o.setStyleSheet('background-color: green')
        else:
            self.buttonA2o.setStyleSheet('background-color: white')
        if 'A3s' in self.range_selected:
            self.buttonA3s.setStyleSheet('background-color: green')
        else:
            self.buttonA3s.setStyleSheet('background-color: white')
        if 'A3o' in self.range_selected:
            self.buttonA3o.setStyleSheet('background-color: green')
        else:
            self.buttonA3o.setStyleSheet('background-color: white')
        if 'A4s' in self.range_selected:
            self.buttonA4s.setStyleSheet('background-color: green')
        else:
            self.buttonA4s.setStyleSheet('background-color: white')
        if 'A4o' in self.range_selected:
            self.buttonA4o.setStyleSheet('background-color: green')
        else:
            self.buttonA4o.setStyleSheet('background-color: white')
        if 'A5s' in self.range_selected:
            self.buttonA5s.setStyleSheet('background-color: green')
        else:
            self.buttonA5s.setStyleSheet('background-color: white')
        if 'A5o' in self.range_selected:
            self.buttonA5o.setStyleSheet('background-color: green')
        else:
            self.buttonA5o.setStyleSheet('background-color: white')
        if 'A6s' in self.range_selected:
            self.buttonA6s.setStyleSheet('background-color: green')
        else:
            self.buttonA6s.setStyleSheet('background-color: white')
        if 'A6o' in self.range_selected:
            self.buttonA6o.setStyleSheet('background-color: green')
        else:
            self.buttonA6o.setStyleSheet('background-color: white')
        if 'A7s' in self.range_selected:
            self.buttonA7s.setStyleSheet('background-color: green')
        else:
            self.buttonA7s.setStyleSheet('background-color: white')
        if 'A7o' in self.range_selected:
            self.buttonA7o.setStyleSheet('background-color: green')
        else:
            self.buttonA7o.setStyleSheet('background-color: white')
        if 'A8s' in self.range_selected:
            self.buttonA8s.setStyleSheet('background-color: green')
        else:
            self.buttonA8s.setStyleSheet('background-color: white')
        if 'A8o' in self.range_selected:
            self.buttonA8o.setStyleSheet('background-color: green')
        else:
            self.buttonA8o.setStyleSheet('background-color: white')
        if 'A9s' in self.range_selected:
            self.buttonA9s.setStyleSheet('background-color: green')
        else:
            self.buttonA9s.setStyleSheet('background-color: white')
        if 'A9o' in self.range_selected:
            self.buttonA9o.setStyleSheet('background-color: green')
        else:
            self.buttonA9o.setStyleSheet('background-color: white')
        if 'ATs' in self.range_selected:
            self.buttonATs.setStyleSheet('background-color: green')
        else:
            self.buttonATs.setStyleSheet('background-color: white')
        if 'ATo' in self.range_selected:
            self.buttonATo.setStyleSheet('background-color: green')
        else:
            self.buttonATo.setStyleSheet('background-color: white')
        if 'AJs' in self.range_selected:
            self.buttonAJs.setStyleSheet('background-color: green')
        else:
            self.buttonAJs.setStyleSheet('background-color: white')
        if 'AJo' in self.range_selected:
            self.buttonAJo.setStyleSheet('background-color: green')
        else:
            self.buttonAJo.setStyleSheet('background-color: white')
        if 'AQs' in self.range_selected:
            self.buttonAQs.setStyleSheet('background-color: green')
        else:
            self.buttonAQs.setStyleSheet('background-color: white')
        if 'AQo' in self.range_selected:
            self.buttonAQo.setStyleSheet('background-color: green')
        else:
            self.buttonAQo.setStyleSheet('background-color: white')
        if 'AKs' in self.range_selected:
            self.buttonAKs.setStyleSheet('background-color: green')
        else:
            self.buttonAKs.setStyleSheet('background-color: white')
        if 'AKo' in self.range_selected:
            self.buttonAKo.setStyleSheet('background-color: green')
        else:
            self.buttonAKo.setStyleSheet('background-color: white')

    def select_line_A(self):
        combination = 'A' + 'A'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J', 'Q', 'K']
        for value2 in values:
            combination = "A" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = []
        for value2 in values:
            combination = str(value2) + "A" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_K(self):
        combination = 'K' + 'K'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J', 'Q']
        for value2 in values:
            combination = "K"+ str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['A']
        for value2 in values:
            combination = str(value2) + "K" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_Q(self):
        combination = 'Q' + 'Q'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J']
        for value2 in values:
            combination = "Q" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['K', 'A']
        for value2 in values:
            combination = str(value2) + "Q" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_J(self):
        combination = 'J' + 'J'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T']
        for value2 in values:
            combination = "J" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "J" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_T(self):
        combination = 'T' + 'T'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10))
        for value2 in values:
            combination = "T" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "T" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_9(self):
        combination = '9' + '9'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 9))
        for value2 in values:
            combination = "9" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "9" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_8(self):
        combination = '8' + '8'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 8))
        for value2 in values:
            combination = "8" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "8" + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_7(self):
        combination = '7' + '7'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 7))
        for value2 in values:
            combination = "7" + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(7) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_6(self):
        combination = '6' + '6'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 6))
        for value2 in values:
            combination = str(6) + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(6) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_5(self):
        combination = '5' + '5'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 5))
        for value2 in values:
            combination = str(5) + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(5) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_4(self):
        combination = '4' + '4'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 4))
        for value2 in values:
            combination = str(4) + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(4) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_3(self):
        combination = '3' + '3'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 3))
        for value2 in values:
            combination = str(3) + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(3) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_line_2(self):
        combination = '2' + '2'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 2))
        for value2 in values:
            combination = str(2) + str(value2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_A(self):
        combination = 'A' + 'A'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J', 'Q', 'K']
        for value2 in values:
            combination = "A" + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = []
        for value2 in values:
            combination = str(value2) + "A" + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_K(self):
        combination = 'K' + 'K'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J', 'Q']
        for value2 in values:
            combination = "K" + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['A']
        for value2 in values:
            combination = str(value2) + "K" + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_Q(self):
        combination = 'Q' + 'Q'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T', 'J']
        for value2 in values:
            combination = "Q" + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['K', 'A']
        for value2 in values:
            combination = str(value2) + "Q" + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_J(self):
        combination = 'J' + 'J'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10)) + ['T']
        for value2 in values:
            combination = "J" + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "J" + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_T(self):
        combination = 'T' + 'T'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 10))
        for value2 in values:
            combination = "T" + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + "T" + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_9(self):
        combination = '9' + '9'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 9))
        for value2 in values:
            combination = str(9) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(9) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_8(self):
        combination = '8' + '8'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 8))
        for value2 in values:
            combination = str(8) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(8) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_7(self):
        combination = '7' + '7'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 7))
        for value2 in values:
            combination = str(7) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(7) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_6(self):
        combination = '6' + '6'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 6))
        for value2 in values:
            combination = str(6) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(6) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_5(self):
        combination = '5' + '5'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 5))
        for value2 in values:
            combination = str(5) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(5) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_4(self):
        combination = '4' + '4'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 4))
        for value2 in values:
            combination = str(4) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(4) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_3(self):
        combination = '3' + '3'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 3))
        for value2 in values:
            combination = str(3) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(3) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def select_column_2(self):
        combination = '2' + '2'
        if combination not in self.range_selected:
            self.range_selected.append(combination)
        values = list(range(2, 2))
        for value2 in values:
            combination = str(2) + str(value2) + "o"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for value2 in values:
            combination = str(value2) + str(2) + "s"
            if combination not in self.range_selected:
                self.range_selected.append(combination)
        self.color_buttons()

    def restart_buttons(self):
        self.range_selected = []
        self.color_buttons()

    def line_edit_top_changed(self, value):
        self.value_line_edit = int(value)

    def valider_line_edit(self):
        nb_selected = (self.value_line_edit * 169) // 100
        self.range_selected = self.ranking[:nb_selected]
        self.color_buttons()