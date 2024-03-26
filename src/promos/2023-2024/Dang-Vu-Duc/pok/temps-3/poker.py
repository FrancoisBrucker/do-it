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

    def value_name(self, value):
        if value == "A" or value == "As":
            return(14)
        elif value == "K" or value == "Roi":
            return(13)
        elif value == "Q" or value == "Dame":
            return(12)
        elif value == "J" or value == "Valet":
            return(11)
        elif value == "T":
            return(10)
        else:
            return(int(value))

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

    def get_winrate(self, player1_hand, player2_hand, N, current_board = []):
        players_cards = []
        for k in range(2):
            players_cards.append(player1_hand[k].name)
            players_cards.append(player2_hand[k].name)
        current_deck = [card for card in self.deck if card.name not in players_cards]
        tot_wins_player1 = 0
        tot_wins_player2 = 0
        tot_draws = 0
        if len(current_board) == 0:
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
        elif len(current_board) == 3:
            for k in range(N):
                board = current_board[:]
                deck = current_deck[:]
                for i in range(2):
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
        elif len(current_board) == 4:
            for k in range(N):
                board = current_board[:]
                deck = current_deck[:]
                for i in range(1):
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
        elif len(current_board) == 5:
            for k in range(N):
                board = current_board[:]
                deck = current_deck[:]
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
    
    def get_decision(self, pot: int, amount_to_call: int, suits: list, player_hand: list, N: int, current_board = []):
        pot_odd = amount_to_call /(pot + amount_to_call)
        tot_winrate = 0
        count = 0
        
        for combination in tqdm(self.range_selected):
            if len(combination) == 2 and len(suits) != 1:
                value = combination[0]
                value = self.value_name(value)
                for k in range(len(suits) - 1):
                    suit1 = suits[k]
                    card1 = Card(value, suit1)
                    suits2 = suits[k+1:]
                    for suit2 in suits2:
                        card2 = Card(value, suit2)
                        opponent_hand = [card1, card2]
                        tot_winrate += self.get_winrate(player_hand, opponent_hand, N, current_board)[0]
                        count += 1
            else:
                suited = combination[-1]
                if suited == "o" and len(suits) != 1:
                    value1 = combination[0]
                    value1 = self.value_name(value1)
                    value2 = combination[1]
                    value2 = self.value_name(value2)
                    for k in range(len(suits) - 1):
                        suit1 = suits[k]
                        card1 = Card(value1, suit1)
                        suits2 = suits[k+1:]
                        for suit2 in suits2:
                            card2 = Card(value2, suit2)
                            opponent_hand = [card1, card2]
                            tot_winrate += self.get_winrate(player_hand, opponent_hand, N, current_board)[0]
                            count += 1
                if suited == "s":
                    value1 = combination[0]
                    value1 = self.value_name(value1)
                    value2 = combination[1]
                    value2 = self.value_name(value2)
                    for k in range(len(suits)):
                        suit = suits[k]
                        card1 = Card(value1, suit)
                        card2 = Card(value2, suit)
                        opponent_hand = [card1, card2]
                        tot_winrate += self.get_winrate(player_hand, opponent_hand, N, current_board)[0]
                        count += 1
        average_winrate = round(tot_winrate/count, sigfigs = 3)
        return(average_winrate, pot_odd * 100)

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
    
    def plot_heatmap_hands_ranking(self):
        table_winrates = [[0 for j in range(13)] for i in range(13)]
        for k in range(len(self.all_average_winrates5)):
            first_value = self.all_average_winrates5[k][0][0:1]
            second_value = self.all_average_winrates5[k][0][1:2]
            if first_value == "A":
                first_value = 14
            elif first_value == "K":
                first_value = 13
            elif first_value == "Q":
                first_value = 12
            elif first_value == "J":
                first_value = 11
            elif first_value == "T":
                first_value = 10
            else:
                first_value = int(first_value)
            if second_value == "A":
                second_value = 14
            elif second_value == "K":
                second_value = 13
            elif second_value == "Q":
                second_value = 12
            elif second_value == "J":
                second_value = 11
            elif second_value == "T":
                second_value = 10
            else:
                second_value = int(second_value)
            if first_value != second_value:
                suit = self.all_average_winrates5[k][0][2:3]
                if suit == "s":
                    index1 = 14 - first_value
                    index2 = second_value - 2
                elif suit == "o":
                    index1 = 1 - second_value
                    index2 = first_value - 2
            else:
                index1 = 14 - first_value
                index2 = first_value - 2
            table_winrates[index1][index2] = self.all_average_winrates5[k][1]
        size_x = 13
        size_y = 13
        x_start = 0
        x_end = 13
        y_start = 0
        y_end = 13
        extent = [x_start, x_end, y_end, y_start]
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        axes = plt.gca()
        # axes.set_ylabel('Première carte du dealer')
        axes.yaxis.set_ticks(np.arange(0.5,13.5))
        axes.yaxis.set_ticklabels(reversed(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']), rotation = 0, fontsize = 12)
        # axes.set_xlabel('Main du joueur')
        axes.xaxis.set_ticks(np.arange(0.5,13.5))
        axes.xaxis.set_ticklabels(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'], rotation = 0,  verticalalignment = 'center',fontsize = 12)
        im = ax.imshow(table_winrates, extent = extent, cmap="RdYlGn", vmin = 28.7, vmax = 85.1)
        plt.title("Taux de réussite de chaque main possible\nMains associées en haut à gauche et mains dépareillées en bas à droite ", pad = 15)
        fig.colorbar(im)

        jump_x = (x_end - x_start) / (2.0 * size_x)
        jump_y = (y_end - y_start) / (2.0 * size_y)
        x_positions = np.linspace(start=x_start, stop=x_end, num=size_x, endpoint=False)
        y_positions = np.linspace(start=y_start, stop=y_end, num=size_y, endpoint=False)
        
        for y_index, y in enumerate(y_positions):
            for x_index, x in enumerate(x_positions):
                label = round(table_winrates[y_index][x_index], sigfigs = 3)
                text_x = x + jump_x
                text_y = y + jump_y
                ax.text(text_x, text_y, label, color='black', ha='center', va='center')
        plt.show()
    
    