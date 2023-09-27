from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from blackjack_methods import Blackjack_methods
import random


class Blackjack(QMainWindow, Blackjack_methods):
    def __init__(self):
        super().__init__()

        ui_file_name = "Blackjack_main_window.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.main_window = loader.load(ui_file)
        ui_file.close()
        self.main_window.setWindowTitle("Blackjack")
        
        self.label_dealercard1 = self.main_window.findChild(QLabel, "DealerCard1")
        self.label_dealercard2 = self.main_window.findChild(QLabel, "DealerCard2")
        self.label_dealercard3 = self.main_window.findChild(QLabel, "DealerCard3")
        self.label_dealercard4 = self.main_window.findChild(QLabel, "DealerCard4")
        self.label_dealercard5 = self.main_window.findChild(QLabel, "DealerCard5")
        self.label_dealercard6 = self.main_window.findChild(QLabel, "DealerCard6")
        self.label_dealercard7 = self.main_window.findChild(QLabel, "DealerCard7")
        self.label_playercard1 = self.main_window.findChild(QLabel, "PlayerCard1")
        self.label_playercard2 = self.main_window.findChild(QLabel, "PlayerCard2")
        self.label_playercard3 = self.main_window.findChild(QLabel, "PlayerCard3")
        self.label_playercard4 = self.main_window.findChild(QLabel, "PlayerCard4")
        self.label_playercard5 = self.main_window.findChild(QLabel, "PlayerCard5")
        self.label_playercard6 = self.main_window.findChild(QLabel, "PlayerCard6")
        self.label_playercard7 = self.main_window.findChild(QLabel, "PlayerCard7")

        self.label_dealerheader = self.main_window.findChild(QLabel, "labelDealerCards")
        self.label_playerheader = self.main_window.findChild(QLabel, "labelPlayerCards")
        self.label_dealercount = self.main_window.findChild(QLabel, "labelDealerCount")
        self.label_playercount = self.main_window.findChild(QLabel, "labelPlayerCount")
        self.PlayerCount = self.main_window.findChild(QLabel, "PlayerCount")
        self.DealerCount = self.main_window.findChild(QLabel, "DealerCount")
        self.result = self.main_window.findChild(QLabel, "label_result")
        self.label_cards = self.main_window.findChild(QLabel, "label_cards")
        self.cardsLeft = self.main_window.findChild(QLabel, "cardsLeft")

        self.hitButton = self.main_window.findChild(QPushButton, "button_hit")
        self.stayButton = self.main_window.findChild(QPushButton, "button_stay")
        self.doubleButton = self.main_window.findChild(QPushButton, "button_double")
        self.restartButton = self.main_window.findChild(QPushButton, "button_restart")
        self.splitButton = self.main_window.findChild(QPushButton, "button_split")

        ui_file_name2 = "Blackjack_split_window.ui"
        ui_file2 = QFile(ui_file_name2)
        loader2 = QUiLoader()
        self.split_window = loader2.load(ui_file2)
        ui_file2.close()
        self.split_window.setWindowTitle("Blackjack: Split Window")

        self.label_split_dealercard1 = self.split_window.findChild(QLabel, "DealerCard1")
        self.label_split_dealercard2 = self.split_window.findChild(QLabel, "DealerCard2")
        self.label_split_dealercard3 = self.split_window.findChild(QLabel, "DealerCard3")
        self.label_split_dealercard4 = self.split_window.findChild(QLabel, "DealerCard4")
        self.label_split_dealercard5 = self.split_window.findChild(QLabel, "DealerCard5")
        self.label_split_dealercard6 = self.split_window.findChild(QLabel, "DealerCard6")
        self.label_split_dealercard7 = self.split_window.findChild(QLabel, "DealerCard7")
        self.label_split_playercard1_1 = self.split_window.findChild(QLabel, "PlayerCard1_1")
        self.label_split_playercard1_2 = self.split_window.findChild(QLabel, "PlayerCard1_2")
        self.label_split_playercard1_3 = self.split_window.findChild(QLabel, "PlayerCard1_3")
        self.label_split_playercard1_4 = self.split_window.findChild(QLabel, "PlayerCard1_4")
        self.label_split_playercard1_5 = self.split_window.findChild(QLabel, "PlayerCard1_5")
        self.label_split_playercard1_6 = self.split_window.findChild(QLabel, "PlayerCard1_6")
        self.label_split_playercard1_7 = self.split_window.findChild(QLabel, "PlayerCard1_7")
        self.label_split_playercard2_1 = self.split_window.findChild(QLabel, "PlayerCard2_1")
        self.label_split_playercard2_2 = self.split_window.findChild(QLabel, "PlayerCard2_2")
        self.label_split_playercard2_3 = self.split_window.findChild(QLabel, "PlayerCard2_3")
        self.label_split_playercard2_4 = self.split_window.findChild(QLabel, "PlayerCard2_4")
        self.label_split_playercard2_5 = self.split_window.findChild(QLabel, "PlayerCard2_5")
        self.label_split_playercard2_6 = self.split_window.findChild(QLabel, "PlayerCard2_6")
        self.label_split_playercard2_7 = self.split_window.findChild(QLabel, "PlayerCard2_7")
        self.split_PlayerCount1 = self.split_window.findChild(QLabel, "PlayerCount1")
        self.split_PlayerCount2 = self.split_window.findChild(QLabel, "PlayerCount2")
        self.split_DealerCount = self.split_window.findChild(QLabel, "DealerCount")
        self.cardsLeft_split = self.split_window.findChild(QLabel, "cardsLeft")

        self.split_hitButton1 = self.split_window.findChild(QPushButton, "button_hit1")
        self.split_stayButton1 = self.split_window.findChild(QPushButton, "button_stay1")
        self.split_doubleButton1 = self.split_window.findChild(QPushButton, "button_double1")
        self.split_hitButton2 = self.split_window.findChild(QPushButton, "button_hit2")
        self.split_stayButton2 = self.split_window.findChild(QPushButton, "button_stay2")
        self.split_doubleButton2 = self.split_window.findChild(QPushButton, "button_double2")
        self.split_buttonRestart = self.split_window.findChild(QPushButton, "button_restart")

        self.split_hitButton1.clicked.connect(self.hit_split)
        self.split_hitButton2.clicked.connect(self.hit_split)
        self.split_stayButton1.clicked.connect(self.stay_split_first)
        self.split_stayButton2.clicked.connect(self.stay_split)
        self.split_buttonRestart.clicked.connect(self.restart_split)
        
        self.restart()
        
        self.hitButton.clicked.connect(self.hit)
        self.restartButton.clicked.connect(self.restart)
        self.stayButton.clicked.connect(self.stay)
        self.splitButton.clicked.connect(self.split)
        self.main_window.show()
        
    def draw(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.cardsLeft.setText(f"{len(self.deck)}")
        self.cardsLeft_split.setText(f"{len(self.deck)}")
        return(card)

    def display_player_count(self):
        count = self.sum_hand(self.player_hand)
        if 1 in (card.value for card in self.player_hand) and (sum([card.value for card in self.player_hand]) + 10) < 21:
            self.PlayerCount.setText(f"{sum([card.value for card in self.player_hand])}" + "/" + f"{count}")
        else:
            self.PlayerCount.setText(f"{count}")
    
    def display_player_count_split(self):
        if self.IsFirst:
            count = self.sum_hand(self.player_hand_split_1)
            if 1 in (card.value for card in self.player_hand_split_1) and (sum([card.value for card in self.player_hand_split_1]) + 10) < 21:
                self.split_PlayerCount1.setText(f"{sum([card.value for card in self.player_hand_split_1])}" + "/" + f"{count}")
            else:
                self.split_PlayerCount1.setText(f"{count}")
        else:
            count = self.sum_hand(self.player_hand_split_2)
            if 1 in (card.value for card in self.player_hand_split_2) and (sum([card.value for card in self.player_hand_split_2]) + 10) < 21:
                self.split_PlayerCount2.setText(f"{sum([card.value for card in self.player_hand_split_2])}" + "/" + f"{count}")
            else:
                self.split_PlayerCount2.setText(f"{count}")
        

    def hit(self):
        self.splitButton.setEnabled(False)
        card = self.draw()
        self.player_hand.append(card)
        pixmap = QPixmap(f'PNG-cards/{card.name}.png')
        if self.player_spot == 0:
            self.label_playercard1.setPixmap(pixmap)
            self.player_spot += 1

        elif self.player_spot == 1:
            self.label_playercard2.setPixmap(pixmap)
            self.player_spot += 1
        
        elif self.player_spot == 2:
            self.label_playercard3.setPixmap(pixmap)
            self.player_spot += 1
        
        elif self.player_spot == 3:
            self.label_playercard4.setPixmap(pixmap)
            self.player_spot += 1
        
        elif self.player_spot == 4:
            self.label_playercard5.setPixmap(pixmap)
            self.player_spot += 1
        
        elif self.player_spot == 5:
            self.label_playercard6.setPixmap(pixmap)
            self.player_spot += 1
        
        elif self.player_spot == 6:
            self.label_playercard7.setPixmap(pixmap)
            self.player_spot += 1
        
        self.display_player_count()
        count = self.sum_hand(self.player_hand)
        if count > 21:
            self.player_bust = True
            self.result.setText("Le joueur a bust")
            self.PlayerCount.setStyleSheet("color : red")
            self.stay()
    
    def hit_split(self):
        if self.IsFirst:
            card = self.draw()
            self.player_hand_split_1.append(card)
            pixmap = QPixmap(f'PNG-cards/{card.name}.png')
            if self.player_spot_split_1 == 0:
                self.label_split_playercard1_1.setPixmap(pixmap)
                self.player_spot_split_1 += 1

            elif self.player_spot_split_1 == 1:
                self.label_split_playercard1_2.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            elif self.player_spot_split_1 == 2:
                self.label_split_playercard1_3.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            elif self.player_spot_split_1 == 3:
                self.label_split_playercard1_4.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            elif self.player_spot_split_1 == 4:
                self.label_split_playercard1_5.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            elif self.player_spot_split_1 == 5:
                self.label_split_playercard1_6.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            elif self.player_spot_split_1 == 6:
                self.label_split_playercard1_7.setPixmap(pixmap)
                self.player_spot_split_1 += 1
            
            self.display_player_count_split()
            count = self.sum_hand(self.player_hand_split_1)
            if count > 21:
                self.split_PlayerCount1.setStyleSheet("color : red")
                self.split_hitButton2.setEnabled(True)
                self.split_stayButton2.setEnabled(True)
                self.split_doubleButton2.setEnabled(True)
                self.split_hitButton1.setEnabled(False)
                self.split_stayButton1.setEnabled(False)
                self.split_doubleButton1.setEnabled(False)
                self.IsFirst = False
        
        else:
            card = self.draw()
            self.player_hand_split_2.append(card)
            pixmap = QPixmap(f'PNG-cards/{card.name}.png')
            if self.player_spot_split_2 == 0:
                self.label_split_playercard2_1.setPixmap(pixmap)
                self.player_spot_split_2 += 1

            elif self.player_spot_split_2 == 1:
                self.label_split_playercard2_2.setPixmap(pixmap)
                self.player_spot_split_2 += 1
            
            elif self.player_spot_split_2 == 2:
                self.label_split_playercard2_3.setPixmap(pixmap)
                self.player_spot_split_2 += 1
            
            elif self.player_spot_split_2 == 3:
                self.label_split_playercard2_4.setPixmap(pixmap)
                self.player_spot_split_2 += 1
            
            elif self.player_spot_split_2 == 4:
                self.label_split_playercard2_5.setPixmap(pixmap)
                self.player_spot_split_2 += 1
            
            elif self.player_spot_split_2 == 5:
                self.label_split_playercard2_6.setPixmap(pixmap)
                self.player_spot_split_2 += 1
            
            elif self.player_spot_split_2 == 6:
                self.label_split_playercard2_7.setPixmap(pixmap)
                self.player_spot_split_2 += 1

            self.display_player_count_split()
            count = self.sum_hand(self.player_hand_split_2)
            if count > 21:
                self.split_PlayerCount2.setStyleSheet("color : red")
                self.stay_split()            

    def split(self):
        if self.dealer_hand[0].value == 1:
            self.split_DealerCount.setText("1/11")
        else:
            self.split_DealerCount.setText(f"{self.sum_hand(self.dealer_hand)}")
        self.split_hitButton1.setEnabled(True)
        self.split_stayButton1.setEnabled(True)
        self.split_doubleButton1.setEnabled(True)
        self.player_hand_split_1 = [self.player_hand[0]]
        self.player_hand_split_2 = [self.player_hand[1]]
        count = self.sum_hand(self.player_hand_split_1)
        if 1 in (card.value for card in self.player_hand_split_1) and (sum([card.value for card in self.player_hand_split_1]) + 10) < 21:
            self.split_PlayerCount1.setText(f"{sum([card.value for card in self.player_hand_split_1])}" + "/" + f"{count}")
        else:
            self.split_PlayerCount1.setText(f"{count}")
        count = self.sum_hand(self.player_hand_split_2)
        if 1 in (card.value for card in self.player_hand_split_2) and (sum([card.value for card in self.player_hand_split_2]) + 10) < 21:
            self.split_PlayerCount2.setText(f"{sum([card.value for card in self.player_hand_split_2])}" + "/" + f"{count}")
        else:
            self.split_PlayerCount2.setText(f"{count}")
        self.label_split_dealercard1.setPixmap(QPixmap(f'PNG-cards/{self.dealer_hand[0].name}.png'))
        self.label_split_playercard1_1.setPixmap(QPixmap(f'PNG-cards/{self.player_hand[0].name}.png'))
        self.label_split_playercard2_1.setPixmap(QPixmap(f'PNG-cards/{self.player_hand[1].name}.png'))
        self.split_hitButton2.setEnabled(False)
        self.split_stayButton2.setEnabled(False)
        self.split_doubleButton2.setEnabled(False)
        self.IsFirst = True
        self.split_window.show()
        self.main_window.close()



    def stay(self):
        if 1 in (card.value for card in self.player_hand):
            self.PlayerCount.setText(f"{self.sum_hand(self.player_hand)}")
        while self.sum_hand(self.dealer_hand) < 17:
            card = self.draw()
            self.dealer_hand.append(card)
            pixmap = QPixmap(f'PNG-cards/{card.name}.png')
            if self.dealer_spot == 0:
                self.label_dealercard1.setPixmap(pixmap)
                self.dealer_spot += 1

            elif self.dealer_spot == 1:
                self.label_dealercard2.setPixmap(pixmap)
                self.dealer_spot += 1
            
            elif self.dealer_spot == 2:
                self.label_dealercard3.setPixmap(pixmap)
                self.dealer_spot += 1
            
            elif self.dealer_spot == 3:
                self.label_dealercard4.setPixmap(pixmap)
                self.dealer_spot += 1
            
            elif self.dealer_spot == 4:
                self.label_dealercard5.setPixmap(pixmap)
                self.dealer_spot += 1
            
            elif self.dealer_spot == 5:
                self.label_dealercard6.setPixmap(pixmap)
                self.dealer_spot += 1
            
            elif self.dealer_spot == 6:
                self.label_dealercard7.setPixmap(pixmap)
                self.dealer_spot += 1
            count = self.sum_hand(self.dealer_hand)
            self.DealerCount.setText(f"{count}")
            #time.sleep(1)
        if not self.player_bust and self.sum_hand(self.dealer_hand) > 21:
            self.result.setText("Le dealer a bust")
        if not self.player_bust and (self.sum_hand(self.dealer_hand) < self.sum_hand(self.player_hand) or self.sum_hand(self.dealer_hand) > 21):
            self.result.setText("Le joueur a gagné")
        if not self.player_bust and (self.sum_hand(self.dealer_hand) > self.sum_hand(self.player_hand) and self.sum_hand(self.dealer_hand) <= 21):
            self.result.setText("Le dealer a gagné")
        if not self.player_bust and self.sum_hand(self.dealer_hand) == self.sum_hand(self.player_hand):
            self.result.setText("Egalité!")
        if count > 21:
            self.DealerCount.setStyleSheet("color : red")
        self.restartButton.setStyleSheet("background-color: red")
        self.hitButton.setEnabled(False)
        self.stayButton.setEnabled(False)
        self.doubleButton.setEnabled(False)
        self.splitButton.setEnabled(False)

    def stay_split_first(self):
        self.IsFirst = False
        if 1 in (card.value for card in self.player_hand_split_1):
            self.split_PlayerCount1.setText(f"{self.sum_hand(self.player_hand_split_1)}")
        self.split_hitButton2.setEnabled(True)
        self.split_stayButton2.setEnabled(True)
        self.split_doubleButton2.setEnabled(True)
        self.split_hitButton1.setEnabled(False)
        self.split_stayButton1.setEnabled(False)
        self.split_doubleButton1.setEnabled(False)


    def stay_split(self):
        self.split_hitButton2.setEnabled(False)
        self.split_stayButton2.setEnabled(False)
        self.split_doubleButton2.setEnabled(False)
        while self.sum_hand(self.dealer_hand) < 17:
            card = self.draw()
            self.dealer_hand.append(card)
            pixmap = QPixmap(f'PNG-cards/{card.name}.png')
            if self.dealer_spot_split == 0:
                self.label_split_dealercard1.setPixmap(pixmap)
                self.dealer_spot_split += 1

            elif self.dealer_spot_split == 1:
                self.label_split_dealercard2.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            elif self.dealer_spot_split == 2:
                self.label_split_dealercard3.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            elif self.dealer_spot_split == 3:
                self.label_split_dealercard4.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            elif self.dealer_spot_split == 4:
                self.label_split_dealercard5.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            elif self.dealer_spot_split == 5:
                self.label_split_dealercard6.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            elif self.dealer_spot_split == 6:
                self.label_split_dealercard7.setPixmap(pixmap)
                self.dealer_spot_split += 1
            
            count = self.sum_hand(self.dealer_hand)
            self.split_DealerCount.setText(f"{count}")
        self.split_buttonRestart.setStyleSheet("background-color: red")
        if count > 21:
            self.split_DealerCount.setStyleSheet("color : red")

    def restart_split(self):
        self.main_window.show()
        self.split_window.close()
        pixmap = QPixmap(f'PNG-cards/dos.png')
        self.label_split_playercard1_2.setPixmap(pixmap)
        self.label_split_playercard1_3.setPixmap(pixmap)
        self.label_split_playercard1_4.setPixmap(pixmap)
        self.label_split_playercard1_5.setPixmap(pixmap)
        self.label_split_playercard1_6.setPixmap(pixmap)
        self.label_split_playercard1_7.setPixmap(pixmap)
        self.label_split_playercard2_2.setPixmap(pixmap)
        self.label_split_playercard2_3.setPixmap(pixmap)
        self.label_split_playercard2_4.setPixmap(pixmap)
        self.label_split_playercard2_5.setPixmap(pixmap)
        self.label_split_playercard2_6.setPixmap(pixmap)
        self.label_split_playercard2_7.setPixmap(pixmap)
        self.label_split_dealercard2.setPixmap(pixmap)
        self.label_split_dealercard3.setPixmap(pixmap)
        self.label_split_dealercard4.setPixmap(pixmap)
        self.label_split_dealercard5.setPixmap(pixmap)
        self.label_split_dealercard6.setPixmap(pixmap)
        self.label_split_dealercard7.setPixmap(pixmap)
        self.split_PlayerCount1.setStyleSheet("color : white")
        self.split_PlayerCount2.setStyleSheet("color : white")
        self.split_DealerCount.setStyleSheet("color : white")
        self.restart()

    def restart(self):
        if len(self.deck) <= 52:
            self.newdeck()
        self.player_bust = False
        self.hitButton.setEnabled(True)
        self.stayButton.setEnabled(True)
        self.doubleButton.setEnabled(True)
        self.result.setText("")
        self.DealerCount.setStyleSheet("color : white")
        self.PlayerCount.setStyleSheet("color : white")
        self.restartButton.setStyleSheet("background-color: white")
        self.split_buttonRestart.setStyleSheet("background-color: white")
        self.dealer_spot = 1
        self.dealer_spot_split = 1
        card = self.draw()
        self.dealer_hand = [card]
        if card.value == 1:
            self.DealerCount.setText("1/11")
        else:
            self.DealerCount.setText(f"{self.sum_hand(self.dealer_hand)}")
        pixmap = QPixmap(f'PNG-cards/{card.name}.png')
        self.label_dealercard1.setPixmap(pixmap)
        self.player_spot = 2
        self.player_spot_split_1 = 1
        self.player_spot_split_2 = 1
        card1 = self.draw()
        card2 = self.draw()
        pixmap1 = QPixmap(f'PNG-cards/{card1.name}.png')
        pixmap2 = QPixmap(f'PNG-cards/{card2.name}.png')
        self.player_hand = [card1, card2]
        self.label_playercard1.setPixmap(pixmap1)
        self.label_playercard2.setPixmap(pixmap2)
        self.display_player_count()
        pixmap = QPixmap(f'PNG-cards/dos.png')
        self.label_playercard3.setPixmap(pixmap)
        self.label_playercard4.setPixmap(pixmap)
        self.label_playercard5.setPixmap(pixmap)
        self.label_playercard6.setPixmap(pixmap)
        self.label_playercard7.setPixmap(pixmap)
        self.label_dealercard2.setPixmap(pixmap)
        self.label_dealercard3.setPixmap(pixmap)
        self.label_dealercard4.setPixmap(pixmap)
        self.label_dealercard5.setPixmap(pixmap)
        self.label_dealercard6.setPixmap(pixmap)
        self.label_dealercard7.setPixmap(pixmap)
        if card1.value == card2.value:
            self.splitButton.setEnabled(True)
        else:
            self.splitButton.setEnabled(False)
