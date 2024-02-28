import random as rd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from sigfig import round
import json
from operator import itemgetter

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if value == 14:
            self.name = "As de " + suit
        elif value == 13:
            self.name = "Roi de " + suit
        elif value == 12:
            self.name = "Dame de " + suit
        elif value == 11:
            self.name = "Valet de " + suit
        else:
            self.name = f"{value} de " + suit

class Poker_methods():
    def __init__(self):
        self.restart_deck()
        self.all_possible_hands = self.get_all_possible_hands()
        self.all_possible_hands_2 = self.get_all_possible_hands_2()
        with open('all_average_winrates5.json', 'rb') as fp:
            self.all_average_winrates5 = json.load(fp)
        with open('all_average_winrates_detail5.json', 'rb') as fp:
            self.all_average_winrates_detail5 = json.load(fp)


    def restart_deck(self):
        self.deck = []
        for value in range(2, 15):
            for suit in ["coeur", "carreau", "trèfle", "pique"]:
                self.deck.append(Card(value, suit))

    def draw(self):
        index = rd.randint(0, len(self.deck) - 1)
        card = self.deck[index]
        self.deck.pop(index)
        return(card)

    def get_score(self, player_hand, board):
        # 0 = Carte haute
        # 1 = Une paire
        # 2 = Deux paires
        # 3 = Brelan
        # 4 = Quinte
        # 5 = Couleur
        # 6 = Full
        # 7 = Carré
        # 8 = Quinte Flush
        # 9 = Quinte Flush Royale
        cards = player_hand + board
        values = [card.value for card in cards]
        suits = [card.suit for card in cards]
        list_values = list(set(values))
        list_suits = list(set(suits))
        list_count_values = []
        list_count_suits = []
        for value in list_values:
            list_count_values.append(values.count(value))
        for suit in list_suits:
            list_count_suits.append(suits.count(suit))
        if (3 in list_count_values and 2 in list_count_values) : # Premier cas du Full
            index_first_kicker = list_count_values.index(3)
            index_second_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] == 2]
            first_kicker = list_values[index_first_kicker]
            list_candidates = [list_values[index] for index in index_second_kicker]
            second_kicker = max(list_candidates)
            return(6, [first_kicker, second_kicker])
        elif (list_count_values.count(3) == 2): # Deuxième cas du Full
            index_first_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] == 3]
            list_candidates = [list_values[index] for index in index_first_kicker]
            first_kicker = max(list_candidates)
            second_kicker = min(list_candidates)
            return(6, [first_kicker, second_kicker])
        elif 4 in list_count_values: # Carré
            index_first_kicker = list_count_values.index(4)
            index_second_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] != 4]
            list_candidates = [list_values[index] for index in index_second_kicker]
            second_kicker = max(list_candidates)
            first_kicker = list_values[index_first_kicker]
            return(7, [first_kicker, second_kicker])
        elif 5 in list_count_suits or 6 in list_count_suits or 7 in list_count_suits: # Couleur
            if 5 in list_count_suits:
                index_winner_suit = list_count_suits.index(5)
            elif 6 in list_count_suits:
                index_winner_suit = list_count_suits.index(6)
            elif 7 in list_count_suits:
                index_winner_suit = list_count_suits.index(7) 
            winner_suit = list_suits[index_winner_suit]
            list_candidates = [cards[i].value for i in range(len(cards)) if cards[i].suit == winner_suit]
            list_candidates_removed = list(set(list_candidates))
            if len(list_candidates_removed) >= 5:
                if 14 not in list_candidates_removed:
                    values_sorted = sorted(list_candidates_removed, reverse = True)
                    for k in range(len(list_candidates_removed) - 4):
                        current_list = values_sorted[k:k+5]
                        if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                            return(8, sorted(current_list, reverse = True))
                    return(5, sorted(list_candidates, reverse = True)[:5])
                elif 14 in list_candidates_removed:
                    values_sorted = sorted(list_candidates_removed, reverse = True)
                    for k in range(len(list_candidates_removed) - 4):
                        current_list = values_sorted[k:k+5]
                        if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                            if sorted(current_list, reverse = True)[0] == 14:
                                return(9, sorted(current_list, reverse = True))
                            return(8, sorted(current_list, reverse = True))
                    new_values = [element if element != 14 else 1 for element in list_candidates_removed]
                    values_sorted = sorted(new_values, reverse = True)
                    for k in range(len(list_candidates_removed) - 4):
                        current_list = values_sorted[k:k+5]
                        if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                            if sorted(current_list, reverse = True)[0] == 14:
                                return(9, sorted(current_list, reverse = True))
                            return(8, sorted(current_list, reverse = True))
                    return(5, sorted(list_candidates, reverse = True)[:5])
        if len(list_values) >= 5: # Quinte
            if 14 not in list_values:
                values_sorted = sorted(list_values, reverse = True)
                for k in range(len(list_values) - 4):
                    current_list = values_sorted[k:k+5]
                    if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                        return(4, sorted(current_list, reverse = True))
            elif 14 in list_values:
                values_sorted = sorted(list_values, reverse = True)
                for k in range(len(list_values) - 4):
                    current_list = values_sorted[k:k+5]
                    if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                        return(4, sorted(current_list, reverse = True))
                new_values = [element if element != 14 else 1 for element in list_values]
                values_sorted = sorted(new_values, reverse = True)
                for k in range(len(list_values) - 4):
                    current_list = values_sorted[k:k+5]
                    if sorted(current_list, reverse = True) == list(range(min(current_list), max(current_list) + 1))[::-1]:
                        return(4, sorted(current_list, reverse = True))
        if 3 in list_count_values: # Brelan
            index_first_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] == 3]
            list_candidates = [list_values[index] for index in index_first_kicker]
            first_kicker = max(list_candidates)
            index_second_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] != 3]
            list_candidates = [list_values[index] for index in index_second_kicker]
            list_kickers = sorted(list_candidates, reverse = True)
            return(3, [first_kicker] + list_kickers[:2])
        elif list_count_values.count(2) >= 2: # Deux paires
            index_first_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] == 2]
            list_candidates = [list_values[index] for index in index_first_kicker]
            list_first_kickers = sorted(list_candidates, reverse = True)
            index_second_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] != 2]
            list_candidates = [list_values[index] for index in index_second_kicker]
            list_kickers = sorted(list_candidates, reverse = True)
            return(2, list_first_kickers[:2] + list_kickers[:1])
        elif list_count_values.count(2) == 1: # Une paire
            index_first_kicker = list_count_values.index(2)
            first_kicker = list_values[index_first_kicker]
            index_second_kicker = [i for i in range(len(list_count_values)) if list_count_values[i] != 2]
            list_candidates = [list_values[index] for index in index_second_kicker]
            list_kickers = sorted(list_candidates, reverse = True)
            return(1, [first_kicker] + list_kickers[:3])
        else: # Carte haute
            return(0, sorted(values, reverse = True)[:5])
    
    def get_card_name(self, value, suit):
        if value == 14:
            return("As de " + suit)
        elif value == 13:
            return("Roi de " + suit)
        elif value == 12:
            return("Dame de " + suit)
        elif value == 11:
            return("Valet de " + suit)
        else:
            return(f"{value} de " + suit)

    def get_all_possible_hands(self):
        all_possible_hands = []
        list_card_names = []
        suits = ["coeur", "carreau", "trèfle", "pique"]
        values = range(2,15)
        for first_suit in suits:
            for first_value in values:
                first_card = Card(first_value, first_suit)
                for second_suit in suits:
                    for second_value in values:
                        second_card = Card(second_value, second_suit)
                        if first_card.name != second_card.name and [second_card.name, first_card.name] not in list_card_names:
                            all_possible_hands.append([first_card, second_card])
                            list_card_names.append([first_card.name, second_card.name])
        return(all_possible_hands)
    
    def get_all_possible_hands_2(self):
        all_possible_hands_2 = []
        values = range(2,15)
        for first_value in values:
            for second_value in range(first_value, 15):
                first_card = Card(first_value, "coeur")
                second_card = Card(second_value, "coeur")
                if first_card.name != second_card.name:
                    if first_value > second_value:
                        all_possible_hands_2.append([first_card, second_card])
                    else:
                        all_possible_hands_2.append([second_card, first_card])
                first_card = Card(first_value, "coeur")
                second_card = Card(second_value, "pique")
                if first_card.name != second_card.name:
                    if first_value > second_value:
                        all_possible_hands_2.append([first_card, second_card])
                    else:
                        all_possible_hands_2.append([second_card, first_card])
        return(all_possible_hands_2)

    def get_list_compare(self, kickers_player1, kickers_player2, score):
        list_compare = []
        for k in range(len(kickers_player1)):
            if kickers_player1[k] == kickers_player2[k]:
                list_compare.append(None)
            else:
                list_compare.append(kickers_player1[k] > kickers_player2[k])
        return(list_compare)

    def do_first_player_win(self, player1_hand, player2_hand, board):
        score_player1, kickers_player1 = self.get_score(player1_hand, board)
        score_player2, kickers_player2 = self.get_score(player2_hand, board)
        if score_player1 > score_player2:
            return(True)
        elif score_player1 < score_player2:
            return(False)
        else: # Cas de l'égalité
            list_compare = self.get_list_compare(kickers_player1, kickers_player2, score_player1)
            for element in list_compare:
                if element != None:
                    return(element)
            return(None)
    
    def test_duels(self, N):
        for k in range(N):
            self.restart_deck()
            player1_hand = []
            player2_hand = []
            board = []
            for i in range(2):
                card = self.draw()
                player1_hand.append(card)
            for i in range(2):
                card = self.draw()
                player2_hand.append(card)
            for i in range(5):
                card = self.draw()
                board.append(card)
            print('----------------------------------')
            print(f"Main n°{k+1}:")
            print("Main du joueur 1: ", [card.name for card in player1_hand])
            print("Main du joueur 2: ", [card.name for card in player2_hand])
            print("Board: ", [card.name for card in board])
            result = self.do_first_player_win(player1_hand, player2_hand, board)
            if result == None:
                score = self.get_score(player1_hand, board)
                print(f"Égalité! Score: {score}")
            elif result:
                score = self.get_score(player1_hand, board)
                print(f"Le joueur 1 a gagné avec un score de {score}")
            elif not result:
                score = self.get_score(player2_hand, board)
                print(f"Le joueur 2 a gagné avec un score de {score}")

    def get_winrate(self, player1_hand, player2_hand, N):
        players_cards = []
        for k in range(2):
            players_cards.append(player1_hand[k].name)
            players_cards.append(player2_hand[k].name)
        current_deck = [card for card in self.deck if card.name not in players_cards]
        tot_wins_player1 = 0
        tot_wins_player2 = 0
        tot_draws = 0
        for k in range(N):
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
        return(round(tot_wins_player1/N * 100, sigfigs = 3), round(tot_wins_player2/N * 100, sigfigs = 3), round(tot_draws/N * 100, sigfigs = 3))
    
    def get_average_winrate(self, hand, N):
        tot_winrate = 0
        winrates = []
        for possible_hand in tqdm(self.all_possible_hands, desc = "Progression de la boucle secondaire: ", position = 1, leave = False):
            if [hand[0].name, hand[1].name] != [possible_hand[0].name, possible_hand[1].name] and [hand[1].name, hand[0].name] != [possible_hand[0].name, possible_hand[1].name]:
                result = self.get_winrate(hand, possible_hand, N)[0]
                tot_winrate += result
                winrates.append(result)
            else:
                winrates.append(None)
        return(round(tot_winrate / (len(self.all_possible_hands) - 1), sigfigs = 4), winrates)
    
    def get_all_average_winrates(self, N):
        all_average_winrates = []
        all_average_winrates_detail = []
        for hand in tqdm(self.all_possible_hands_2, desc = "Progression de la boucle principale", position = 0):
            winrate, winrates_list = self.get_average_winrate(hand, N)
            first_value = str(hand[0].value)
            second_value = str(hand[1].value)
            if first_value == "10":
                first_value = "T"
            elif first_value == "11":
                first_value = "J"
            elif first_value == "12":
                first_value = "Q"
            elif first_value == "13":
                first_value = "K"
            elif first_value == "14":
                first_value = "A"
            if second_value == "10":
                second_value = "T"
            elif second_value == "11":
                second_value = "J"
            elif second_value == "12":
                second_value = "Q"
            elif second_value == "13":
                second_value = "K"
            elif second_value == "14":
                second_value = "A"
            if hand[0].value == hand[1].value:
                hand_name = first_value + second_value
            elif hand[0].suit == hand[1].suit:
                hand_name = first_value + second_value + "s"
            elif hand[0].suit != hand[1].suit:
                hand_name = first_value + second_value + "o"
            all_average_winrates.append([hand_name, winrate])
            all_average_winrates_detail.append([hand_name, winrates_list])
        return(all_average_winrates, all_average_winrates_detail)
    
    def get_winrate_from_database(self, value11, value12, is_suited1, value21, value22, suit21, suit22):
        if value11 == value12:
            hand_player1 = value11 + value12
        elif is_suited1:
            hand_player1 = value11 + value12 + "s"
        else:
            hand_player1 = value11 + value12 + "o"
        hand_player2 = [self.get_card_name(value21, suit21), self.get_card_name(value22, suit22)]
        for k in range(len(self.all_possible_hands)):
            current_hand = [self.all_possible_hands[k][0].name, self.all_possible_hands[k][1].name]
            if current_hand == hand_player2 or current_hand[::-1] == hand_player2:
                index = k
                break
        for k in range(len(self.all_average_winrates_detail5)):
            if self.all_average_winrates_detail5[k][0] == hand_player1:
                return("Taux de réussite de la main " + hand_player1 + " face à la main " + hand_player2[0] + "-" + hand_player2[1] + ":", self.all_average_winrates_detail5[k][1][index])
            

class Plot_stats(Poker_methods):
    def __init__(self):
        super().__init__()
    
    def plot_stats_combinations(self, N):
        combinations_type = ("Carte haute", "Une paire", "Deux paires", "Brelan", "Quinte", "Couleur", "Full", "Carré", "Quinte \nFlush", "Quinte Flush \nRoyale")
        results = [0 for i in range(len(combinations_type))]
        self.progress_plot_stats_combinations = 0
        for k in tqdm(range(N), desc = "Progression de la simulation: "):
            self.progress_plot_stats_combinations = (k / N) * 100
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
        results = [round(element/N * 100, sigfigs = 3) for element in results]
        ax = plt.axes()
        X = np.arange(len(combinations_type))
        ax.set_xticks(X, combinations_type)
        for i in range(len(X)):
            plt.text(i, results[i] + 0.6,f"{results[i]}%", ha = "center")
        plt.title(f"Fréquence d'apparition des différentes combinaisons pour {N} tirages")
        ax.set_xlabel("Combinaison")
        ax.set_ylabel("Fréquence d'apparition en %")
        plt.bar(X, results)
        plt.show()

    def plot_hands_ranking(self, first_rank, last_rank):
        hands = [f"{i+1}\n{self.all_average_winrates5[i][0]}" for i in range(len(self.all_average_winrates5))]
        hands_extract = hands[first_rank - 1:last_rank]
        results = [hand[1] for hand in self.all_average_winrates5]
        results_extract = results[first_rank - 1:last_rank]
        ax = plt.axes()
        X = np.arange(len(hands_extract))
        ax.set_xticks(X, hands_extract)
        for i in range(len(X)):
            plt.text(i, results_extract[i] + 0.6,f"{results_extract[i]}%", ha = "center", fontsize = 7)
        ax.set_xlabel("Main")
        ax.set_ylabel("Taux de réussite moyen en %")
        plt.bar(X, results_extract)
        plt.show()

