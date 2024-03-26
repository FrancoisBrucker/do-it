from poker import Poker_methods, Card, Plot_stats
from button_methods import Button_methods
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QSlider, QLineEdit, QProgressBar, QComboBox, QRadioButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QPixmap, QIntValidator, QIcon
import matplotlib.pyplot as plt
import numpy as np
from sigfig import round
import random as rd
import time

class UI_stats(Plot_stats, Poker_methods):
    def __init__(self):
        super().__init__()
        ui_file_name = "main_window.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.main_window = loader.load(ui_file)
        ui_file.close()
        self.main_window.show()

        self.main_window.setWindowTitle("Fenêtre principale")

        ui_file_name = "window_hand_range.ui"
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        self.window_hand_range = loader.load(ui_file)
        ui_file.close()

        self.window_hand_range.setWindowTitle("Fenêtre d'aide au choix")

        # icon_main_window = QIcon("Logo Do_IT.png")
        # self.main_window.setWindowIcon(icon_main_window)
        self.button_plot_stats_combinations = self.main_window.findChild(QPushButton, "Button_plot_stats_combinations")
        self.button_plot_hands_ranking = self.main_window.findChild(QPushButton, "Button_plot_hands_ranking")
        self.button_get_winrate = self.main_window.findChild(QPushButton, "Button_get_winrate")
        self.button_plot_heatmap = self.main_window.findChild(QPushButton, "Button_plot_heatmap")

        self.button_plot_heatmap.clicked.connect(self.plot_heatmap_hands_ranking)

        self.button_plot_stats_combinations.clicked.connect(self.show_window_plot_stats_combinations)
        self.button_plot_hands_ranking.clicked.connect(self.show_window_hands_ranking)
        self.button_get_winrate.clicked.connect(self.show_window_get_winrate)

        ui_file_name2 = "window_plot_stats_combinations.ui"
        ui_file2 = QFile(ui_file_name2)
        loader2 = QUiLoader()
        self.window_plot_stats_combinations = loader2.load(ui_file2)
        ui_file2.close()
        self.window_plot_stats_combinations.setWindowTitle("Affichage des fréquences d'apparition des mains")

        self.line_edit_plot_stats_combinations = self.window_plot_stats_combinations.findChild(QLineEdit, "line_edit_plot_stats_combinations")
        self.button_valider_plot_stats_combinations = self.window_plot_stats_combinations.findChild(QPushButton, "button_valider_plot_stats_combinations")
        self.button_return_window_plot_stats_combinations = self.window_plot_stats_combinations.findChild(QPushButton, "button_return")
        self.progress_bar_plot_stats_combinations = self.window_plot_stats_combinations.findChild(QProgressBar, "progress_bar_plot_stats_combinations")
        self.progress_bar_plot_stats_combinations.setValue(0)

        onlyInt = QIntValidator()
        self.line_edit_plot_stats_combinations.setValidator(onlyInt)
        self.line_edit_plot_stats_combinations.textChanged.connect(self.line_edit_plot_stats_combinations_changed)
        self.line_edit_plot_stats_combinations.setText("100")
        self.button_valider_plot_stats_combinations.clicked.connect(self.valider_plot_stats_combinations)
        self.button_return_window_plot_stats_combinations.clicked.connect(self.return_main_window)
        self.N_plot_stats_combinations = 100


        ui_file_name3 = "window_plot_hands_ranking.ui"
        ui_file3 = QFile(ui_file_name3)
        loader3 = QUiLoader()
        self.window_plot_hands_ranking = loader3.load(ui_file3)
        ui_file3.close()
        self.window_plot_hands_ranking.setWindowTitle("Affichage du classement des meilleures mains")

        self.last_rank = 169        
        self.first_rank = 1
        self.button_valider_plot_hands_ranking = self.window_plot_hands_ranking.findChild(QPushButton, "button_valider_plot_hands_ranking")
        self.button_valider_plot_hands_ranking.clicked.connect(self.valider_plot_hands_ranking)
        self.line_edit_plot_hands_ranking_first_rank = self.window_plot_hands_ranking.findChild(QLineEdit, "line_edit_first_rank")
        self.line_edit_plot_hands_ranking_first_rank.setValidator(onlyInt)
        self.line_edit_plot_hands_ranking_first_rank.textChanged.connect(self.line_edit_plot_hands_ranking_first_rank_changed)
        self.line_edit_plot_hands_ranking_first_rank.setText("1")
        self.line_edit_plot_hands_ranking_last_rank = self.window_plot_hands_ranking.findChild(QLineEdit, "line_edit_last_rank")
        self.line_edit_plot_hands_ranking_last_rank.setValidator(onlyInt)
        self.line_edit_plot_hands_ranking_last_rank.textChanged.connect(self.line_edit_plot_hands_ranking_last_rank_changed)
        self.line_edit_plot_hands_ranking_last_rank.setText("169")
        self.button_return_plot_hands_ranking = self.window_plot_hands_ranking.findChild(QPushButton, "button_return_plot_hands_ranking")
        self.button_return_plot_hands_ranking.clicked.connect(self.return_main_window)

        ui_file_name4 = "window_get_winrate.ui"
        ui_file4 = QFile(ui_file_name4)
        loader4= QUiLoader()
        self.window_get_winrate = loader4.load(ui_file4)
        ui_file4.close()
        self.window_get_winrate.setWindowTitle("Affichage d'un taux de réussite")

        self.button_valider_get_winrate = self.window_get_winrate.findChild(QPushButton, "button_valider_get_winrate")
        self.button_valider_get_winrate.clicked.connect(self.valider_get_winrate)
        self.card1_player1 = self.window_get_winrate.findChild(QComboBox, "card1_player1")
        self.card2_player1 = self.window_get_winrate.findChild(QComboBox, "card2_player1")
        self.suit1_player1 = self.window_get_winrate.findChild(QComboBox, "suit1_player1")
        self.suit2_player1 = self.window_get_winrate.findChild(QComboBox, "suit2_player1")
        self.card1_player2 = self.window_get_winrate.findChild(QComboBox, "card1_player2")
        self.card2_player2 = self.window_get_winrate.findChild(QComboBox, "card2_player2")
        self.suit1_player2 = self.window_get_winrate.findChild(QComboBox, "suit1_player2")
        self.suit2_player2 = self.window_get_winrate.findChild(QComboBox, "suit2_player2")
        self.progress_bar_get_winrate = self.window_get_winrate.findChild(QProgressBar, "progress_bar_get_winrate")
        self.result_get_winrate = self.window_get_winrate.findChild(QLabel, "result_simulation_get_winrate")
        self.line_edit_get_winrate = self.window_get_winrate.findChild(QLineEdit, "line_edit_get_winrate")
        self.line_edit_get_winrate.setValidator(onlyInt)
        self.line_edit_get_winrate.textChanged.connect(self.line_edit_get_winrate_changed)
        self.line_edit_get_winrate.setText("100")
        self.N_get_winrate = 100
        self.label_erreur_get_winrate = self.window_get_winrate.findChild(QLabel, "label_erreur_get_winrate")
        self.label_erreur_get_winrate.setText("")
        self.button_return_get_winrate = self.window_get_winrate.findChild(QPushButton, "button_return_get_winrate")
        self.button_return_get_winrate.clicked.connect(self.return_main_window)

    def show_window_plot_stats_combinations(self):
        self.main_window.close()
        self.window_plot_stats_combinations.show()
    
    def line_edit_plot_stats_combinations_changed(self, value):
        if value != '':
            self.N_plot_stats_combinations = int(value)
            self.line_edit_plot_stats_combinations.setText(value)
            self.button_valider_plot_stats_combinations.setEnabled(True)
        else:
            self.button_valider_plot_stats_combinations.setEnabled(False)

    def valider_plot_stats_combinations(self):
        self.button_valider_plot_stats_combinations.setEnabled(False)
        combinations_type = ("Carte haute", "Une paire", "Deux paires", "Brelan", "Quinte", "Couleur", "Full", "Carré", "Quinte \nFlush", "Quinte Flush \nRoyale")
        results = [0 for i in range(len(combinations_type))]
        self.progress_plot_stats_combinations = 0
        for k in range(self.N_plot_stats_combinations):
            self.progress_plot_stats_combinations = (k / self.N_plot_stats_combinations) * 100
            player_hand = []
            board = []
            for i in range(2):
                card = self.draw()
                player_hand.append(card)
            for i in range(5):
                card = self.draw()
                board.append(card)
            score = self.get_score(player_hand, board)[0]
            results[score] += 1
            self.restart_deck()
            self.progress_bar_plot_stats_combinations.setValue(self.progress_plot_stats_combinations)
        results = [round(element/self.N_plot_stats_combinations * 100, sigfigs = 3) for element in results]
        ax = plt.axes()
        X = np.arange(len(combinations_type))
        ax.set_xticks(X, combinations_type)
        for i in range(len(X)):
            plt.text(i, results[i] + 0.6,f"{results[i]}%", ha = "center")
        plt.title(f"Fréquence d'apparition des différentes combinaisons pour {self.N_plot_stats_combinations} tirages")
        ax.set_xlabel("Combinaison")
        ax.set_ylabel("Fréquence d'apparition en %")
        plt.bar(X, results)
        plt.show()
        self.button_valider_plot_stats_combinations.setEnabled(True)
        self.return_main_window()

    def return_main_window(self):
        self.window_plot_stats_combinations.close()
        self.window_get_winrate.close()
        self.window_plot_hands_ranking.close()
        self.main_window.show()
    
    def show_window_hands_ranking(self):
        self.main_window.close()
        self.window_plot_hands_ranking.show()
    
    def show_window_get_winrate(self):
        self.main_window.close()
        self.window_get_winrate.show()

    def line_edit_plot_hands_ranking_first_rank_changed(self, value):
        if value != '':
            self.first_rank = int(value)
            if self.first_rank > self.last_rank:
                self.button_valider_plot_hands_ranking.setEnabled(False)
            else:
                self.button_valider_plot_hands_ranking.setEnabled(True)
        else:
            self.button_valider_plot_hands_ranking.setEnabled(False)
    
    def line_edit_plot_hands_ranking_last_rank_changed(self, value):
        if value != '':
            self.last_rank = int(value)
            if self.first_rank > self.last_rank:
                self.button_valider_plot_hands_ranking.setEnabled(False)
            else:
                self.button_valider_plot_hands_ranking.setEnabled(True)
        else:
            self.button_valider_plot_hands_ranking.setEnabled(False)
    
    def valider_plot_hands_ranking(self):
        self.plot_hands_ranking(self.first_rank, self.last_rank)
    
    def line_edit_get_winrate_changed(self, value):
        if value != '':
            self.N_get_winrate = int(value)
            if self.N_get_winrate > 0:
                self.button_valider_get_winrate.setEnabled(True)
            else:
                self.button_valider_get_winrate.setEnabled(False)
        else:
            self.button_valider_get_winrate.setEnabled(False)

    def valider_get_winrate(self):
        if self.card1_player1.currentText() == "As":
            value1_player1 = 14
        elif self.card1_player1.currentText() == "Roi":
            value1_player1 = 13
        elif self.card1_player1.currentText() == "Dame":
            value1_player1 = 12
        elif self.card1_player1.currentText() == "Valet":
            value1_player1 = 11
        else:
            value1_player1 = int(self.card1_player1.currentText())
        if self.card1_player2.currentText() == "As":
            value1_player2 = 14
        elif self.card1_player2.currentText() == "Roi":
            value1_player2 = 13
        elif self.card1_player2.currentText() == "Dame":
            value1_player2 = 12
        elif self.card1_player2.currentText() == "Valet":
            value1_player2 = 11
        else:
            value1_player2 = int(self.card1_player2.currentText())
    
        if self.card2_player1.currentText() == "As":
            value2_player1 = 14
        elif self.card2_player1.currentText() == "Roi":
            value2_player1 = 13
        elif self.card2_player1.currentText() == "Dame":
            value2_player1 = 12
        elif self.card2_player1.currentText() == "Valet":
            value2_player1 = 11
        else:
            value2_player1 = int(self.card2_player1.currentText())
        if self.card2_player2.currentText() == "As":
            value2_player2 = 14
        elif self.card2_player2.currentText() == "Roi":
            value2_player2 = 13
        elif self.card2_player2.currentText() == "Dame":
            value2_player2 = 12
        elif self.card2_player2.currentText() == "Valet":
            value2_player2 = 11
        else:
            value2_player2 = int(self.card2_player2.currentText())
        cards = [self.get_card_name(value1_player1, str(self.suit1_player1.currentText())), self.get_card_name(value2_player1, str(self.suit2_player1.currentText())), self.get_card_name(value1_player2, str(self.suit1_player2.currentText())), self.get_card_name(value2_player2, str(self.suit2_player2.currentText()))]
        cards_removed = list(set(cards))
        if len(cards_removed) == 4:
            self.button_valider_get_winrate.setEnabled(False)
            self.label_erreur_get_winrate.setText("")
            player1_hand = [Card(value1_player1, str(self.suit1_player1.currentText()).lower()), Card(value2_player1, str(self.suit2_player1.currentText()).lower())]
            player2_hand = [Card(value1_player2, str(self.suit1_player2.currentText()).lower()), Card(value2_player2, str(self.suit2_player2.currentText()).lower())]
            players_cards = []
            for k in range(2):
                players_cards.append(player1_hand[k].name)
                players_cards.append(player2_hand[k].name)
            current_deck = [card for card in self.deck if card.name not in players_cards]
            tot_wins_player1 = 0
            tot_wins_player2 = 0
            tot_draws = 0
            progression = 0
            for k in range(self.N_get_winrate):
                progression += 1
                current_progression = (progression / self.N_get_winrate) * 100
                board = []
                deck = current_deck[:]
                for i in range(5):
                    index = rd.randint(0, len(deck) - 1)
                    card = deck[index]
                    deck.pop(index)
                    board.append(card)
                result = self.do_first_player_win(player1_hand, player2_hand, board)
                if result == None:
                    tot_draws += 1
                elif result:
                    tot_wins_player1 += 1
                elif not result:
                    tot_wins_player2 += 1
                self.progress_bar_get_winrate.setValue(current_progression)
            self.result_get_winrate.setText(f"Taux de réussite de la première main: {round(tot_wins_player1/self.N_get_winrate * 100, sigfigs = 3)}% \nTaux de réussite de la deuxième main: {round(tot_wins_player2/self.N_get_winrate * 100, sigfigs = 3)}% \nTaux de parties nulles: {round(tot_draws/self.N_get_winrate * 100, sigfigs = 3)}%")
            self.button_valider_get_winrate.setEnabled(True)
        else:
            self.label_erreur_get_winrate.setText("Au moins une carte se répète")
    
                
                