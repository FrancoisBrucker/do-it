from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import random

class Bataille(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file_name = "bataille.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.main_window = loader.load(ui_file)
        ui_file.close()
        self.main_window.setWindowTitle("Bataille")

        self.DealerCard = self.main_window.findChild(QLabel, "dealer_card")
        self.PlayerCard = self.main_window.findChild(QLabel, "player_card")
        self.DealerCount = self.main_window.findChild(QLabel, "dealer_count")
        self.PlayerCount = self.main_window.findChild(QLabel, "player_count")
        self.PlayerName = self.main_window.findChild(QLabel, "player_header")
        self.CardsLeft = self.main_window.findChild(QLabel, "cards_left")
        self.result = self.main_window.findChild(QLabel, "result")
        self.PlayButton = self.main_window.findChild(QPushButton, "play_button")
        self.RestartButton = self.main_window.findChild(QPushButton, "restart_button")
        self.ShuffleButton = self.main_window.findChild(QPushButton, "shuffle_button")

        self.PlayButton.clicked.connect(self.play)
        self.RestartButton.clicked.connect(self.restart)
        self.ShuffleButton.clicked.connect(self.newdeck)

        self.dealer_count = 0
        self.player_count = 0

        widget = QWidget()
        self.name_window = QMainWindow()
        self.name_window.setWindowTitle("Nom du joueur")
        self.name_window.setCentralWidget(widget)
        label = QLabel("Entrez votre nom:")
        self.line_edit = QLineEdit()
        button_valider = QPushButton("Valider")
        button_valider.clicked.connect(self.valider)
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        layout.addWidget(button_valider)
        widget.setLayout(layout)
        self.name_window.show()

        self.newdeck()
    
    def valider(self):
        name = self.line_edit.text()
        self.PlayerName.setText(f"Cartes du joueur {name}")
        self.main_window.show()
        self.name_window.close()

    def newdeck(self):
        suits = ["diamonds", "clubs" ,"hearts", "spades"]
        values = range(2,15)
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(f"{value}_of_{suit}", value))
        self.CardsLeft.setText(f"{len(self.deck)} cartes restantes")
    
    def play(self):
        card_dealer = random.choice(self.deck)
        self.deck.remove(card_dealer)
        pixmap_dealer = QPixmap(f'PNG-cards/{card_dealer.name}.png')
        self.DealerCard.setPixmap(pixmap_dealer)
        card_player = random.choice(self.deck)
        self.deck.remove(card_player)
        pixmap_player = QPixmap(f'PNG-cards/{card_player.name}.png')
        self.PlayerCard.setPixmap(pixmap_player)
        self.CardsLeft.setText(f"{len(self.deck)} cartes restantes")

        if card_dealer.value > card_player.value:
            self.result.setText("Le dealer a gagné!")
            self.dealer_count += 1
            self.DealerCount.setText(f"Le dealer a {self.dealer_count} points")

        if card_dealer.value < card_player.value:
            self.result.setText("Le joueur a gagné!")
            self.player_count += 1
            self.PlayerCount.setText(f"Le joueur a {self.player_count} points")

        if card_dealer.value == card_player.value:
            self.result.setText("Egalité!")
        
        if len(self.deck) == 0:
            self.newdeck()

    def restart(self):
        self.player_count = 0
        self.dealer_count = 0
        self.PlayerCount.setText("Le joueur a 0 points")
        self.DealerCount.setText("Le dealer a 0 points")
        pixmap = QPixmap('PNG-cards/dos.png')
        self.DealerCard.setPixmap(pixmap)
        self.PlayerCard.setPixmap(pixmap)
        self.newdeck()

class Card():
    def __init__(self, name, value):
        self.value = value
        self.name = name