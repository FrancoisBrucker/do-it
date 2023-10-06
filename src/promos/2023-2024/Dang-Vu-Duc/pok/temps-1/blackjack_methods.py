import random
import matplotlib.pyplot as plt
import numpy as np

class Blackjack_methods():
    def __init__(self):
        self.newdeck()
    
    def newdeck(self):
        suits = ["diamonds", "clubs" ,"hearts", "spades"]
        values = range(1,14)
        initial_deck = []
        for suit in suits:
            for value in values:
                if value < 10:
                    initial_deck.append(Card(f"{value}_of_{suit}", value))
                if value >= 10:
                    initial_deck.append(Card(f"{value}_of_{suit}", 10))
        self.deck = initial_deck * 6
    
    def sum_hand(self, hand):
        if 1 in (card.value for card in hand):
            sum1 = sum([card.value for card in hand]) + 10
            if sum1 > 21:
                return(sum([card.value for card in hand]))
            else:
                return(sum1)
        else:
            return(sum([card.value for card in hand]))

class Card():
    def __init__(self, name, value):
        self.value = value
        self.name = name

class Blackjack_simulation(Blackjack_methods):
    def __init__(self):
        super().__init__()
        #0: stay
        #1: hit
        #2: double
        #3: split
        self.true_count = 0
        self.running_count = 0
        self.strat1 = [[0 for j in range(10)] for i in range(13)]
        for i in range(4):
            for j in range(10):
                self.strat1[i][j] = 1
        for j in range(5,10):
            self.strat1[4][j] = 1
        for i in range(7,11):
            for j in range(5,10):
                self.strat1[i][j] = 1
        self.strat1[4][0] = 1
        self.strat1[5][8] = 1
        self.strat1[5][9] = 1
        self.strat1[7][0] = 1
        self.strat1[7][1] = 1
        for j in range(1,5):
            self.strat1[4][j] = 2
        for j in range(8):
            self.strat1[5][j] = 2
        for j in range(10):
            self.strat1[6][j] = 2
        self.strat2 = [[3 for j in range(10)] for i in range(10)]
        for i in range(0,3):
            for j in range(6,10):
                self.strat2[i][j] = 1
        for j in range(3):
            self.strat2[2][j] = 1
        self.strat2[2][5] = 1
        for i in range(4,6):
            for j in range(6,10):
                self.strat2[i][j] = 1
        self.strat2[4][5] = 1
        self.strat2[3][8] = 1
        self.strat2[3][9] = 1
        for j in range(10):
            self.strat2[8][j] = 0
        self.strat2[7][5] = 0
        self.strat2[7][8] = 0
        self.strat2[7][9] = 0
        for j in range(8):
            self.strat2[3][j] = 2
        self.strat3 = [[2 for j in range(10)] for i in range(9)]
        for i in range(5):
            for j in range(5,10):
                self.strat3[i][j] = 1
        for j in range(7,10):
            self.strat3[5][j] = 1
        for i in range(6,9):
            for j in range(10):
                self.strat3[i][j] = 0
        self.strat3[5][5] = 0
        self.strat3[5][6] = 0
        for i in range(4):
            for j in range(2):
                self.strat3[i][j] = 1
        self.strat3[4][0] = 1
        self.strat3[0][2] = 1
        self.strat3[1][2] = 1
    
    def draw(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return(card)
    
    def count(self,card):
        if card.value >= 2 and card.value <= 6:
            self.running_count += 1
        if card.value == 10 or card.value == 1:
            self.running_count -= 1
        nb_deck = len(self.deck)/52
        self.true_count = self.running_count/nb_deck
    
    def play_casino(self,hand):
        while self.sum_hand(hand) <= 16:
            card = self.draw()
            self.count(card)
            hand.append(card)
    
    def simulation(self,n,count,graph_type):
        gain = 0
        winrate_player = 0
        bust_player = 0
        bust_casino = 0
        list_card_winrate = [0 for i in range(10)]
        list_card_played = [0 for i in range(10)]
        played = False
        number_count = 0
        hands_played_normal = [[0 for i in range(15)] for k in range(10)]
        winrates_normal = [[0 for i in range(15)] for k in range(10)]
        hands_played_split = [[0 for i in range(10)] for k in range(10)]
        winrates_split = [[0 for i in range(10)] for k in range(10)]
        hands_played_ace = [[0 for i in range(9)] for k in range(10)]
        winrates_ace = [[0 for i in range(9)] for k in range(10)]
        for game in range(n):
            played = False
            factor = 1
            if len(self.deck) < 52:
                self.newdeck()
                self.true_count, self.running_count = 0, 0
            if count and self.true_count >= 3:
                factor *= (self.true_count + 4)
                number_count += 1
            # if self.true_count >= count_threshold and count:
            #     factor *= (count_factor)
            #     number_count += 1
            card1 = self.draw()
            card3 = self.draw()
            card2 = self.draw()
            card4 = self.draw()
            self.count(card1)
            self.count(card2)
            self.count(card3)
            self.count(card4)
            if card3.value == 1:
                index3 = 9
            else:
                index3 = card3.value - 2
            hand_player = [card1, card2]
            hand_casino = [card3, card4]
            list_card_played[index3] += 1
            played_normal = False
            played_split = False
            played_ace = False
            if card1.value != 1 and card2.value != 1 and card1.value != card2.value:
                index_player = card1.value + card2.value - 5
                if card3.value == 1:
                    index_casino = 0
                else:
                    index_casino = 11 - card3.value
                hands_played_normal[index_casino][index_player] += 1
                played_normal = True
            if card1.value == card2.value:
                if card1.value == 1:
                    index_player = 9
                else:
                    index_player = card1.value - 2
                if card3.value == 1:
                    index_casino = 0
                else:
                    index_casino = 11 - card3.value
                hands_played_split[index_casino][index_player] += 1
                played_split = True
            if ((card1.value == 1) ^ (card2.value == 1)):
                no_ace = max(card1.value,card2.value)
                if card3.value == 1:
                    index_casino = 0
                else:
                    index_casino = 11 - card3.value
                index_player = no_ace - 2
                hands_played_ace[index_casino][index_player] += 1
                played_ace = True
            #Cas du Blackjack
            if ((card1.value == 1 and card2.value == 10) or (card1.value == 10 and card2.value == 1)) and not ((card3.value == 1 and card4.value == 10) or (card3.value == 10 and card4.value == 1)):
                played = True
                gain += factor * 1.5
                winrate_player += 1
                list_card_winrate[index3] += 1
                winrates_ace[index_casino][index_player] += 1
            if ((card3.value == 1 and card4.value == 10) or (card3.value == 10 and card4.value == 1)) and not ((card1.value == 1 and card2.value == 10) or (card1.value == 10 and card2.value == 1)):
                played = True
                gain -= factor * 1
            if ((card3.value == 1 and card4.value == 10) or (card3.value == 10 and card4.value == 1)) and ((card1.value == 1 and card2.value == 10) or (card1.value == 10 and card2.value == 1)):
                played = True
                winrates_ace[index_casino][index_player] += 1/2
                gain += 0
                winrate_player += 1/2
                list_card_winrate[index3] += 1/2
            #Cas du split
            if card1.value == card2.value:
                if card1.value == 1:
                    index1 = 9
                else:
                    index1 = card1.value - 2
                    
                if card3.value == 1:
                    index2 = 9
                else:
                    index2 = card3.value - 2
                if self.strat2[index1][index2] == 1:
                    card = self.draw()
                    hand_player.append(card)
                    self.count(card)
                elif self.strat2[index1][index2] == 2 and len(hand_player) == 2:
                    card = self.draw()
                    hand_player.append(card)
                    self.count(card)
                    factor *= 2
                    played = True
                    if self.sum_hand(hand_player) <= 21:
                        self.play_casino(hand_casino)
                        if self.sum_hand(hand_casino) > 21:
                            bust_casino += 1
                        if self.sum_hand(hand_casino) < self.sum_hand(hand_player) or self.sum_hand(hand_casino)>21:
                            gain += factor*1
                            winrate_player += 1
                            list_card_winrate[index3] += 1
                            if played_split:
                                winrates_split[index_casino][index_player] += 1
                        if self.sum_hand(hand_casino) > self.sum_hand(hand_player) and self.sum_hand(hand_casino)<=21:
                            gain -= factor*1
                    else:
                        bust_player += 1
                        gain -= factor*1
                elif self.strat2[index1][index2] == 3:
                    played = True
                    card11 = self.draw()
                    self.count(card11)
                    card22 = self.draw()
                    self.count(card22)
                    hands = []
                    hand_player1 = [card1,card11]
                    hand_player2 = [card2,card22]
                    hands = [hand_player1,hand_player2]
                    for k in range(2):
                        card1 = hands[k][0]
                        card2 = hands[k][1]
                        if (card1.value == 1 and card2.value == 10) or (card2.value == 1 and card1.value == 10):
                            self.play_casino(hand_casino)
                            if self.sum_hand(hand_casino) != 21 or len(hand_casino) != 2:
                                gain += factor*1.5*0.5
                                winrate_player += 1/2
                                list_card_winrate[index3] += 1/2
                                if played_split:
                                    winrates_split[index_casino][index_player] += 1/2
                            else:
                                gain += 0
                                if played_split:
                                    winrates_split[index_casino][index_player] += 1/4
                        else:
                            index1 = self.sum_hand(hands[k]) - 5
                            if index1 < 0:
                                index1 = 0
                            if index1 > 12:
                                index1 = 12
                            if card3.value == 1:
                                index2 = 9
                            if card3.value != 1:
                                index2 = card3.value - 2
                            while (self.strat1[index1][index2] == 1 or self.strat1[index1][index2] == 2) and self.sum_hand(hands[k]) <= 21:
                                if self.strat1[index1][index2] == 2 and len(hands[k]) == 2:
                                    card = self.draw()
                                    hands[k].append(card)
                                    self.count(card)
                                    factor *= 2
                                    break
                                card = self.draw()
                                self.count(card)
                                hands[k].append(card)
                                index1 = self.sum_hand(hands[k]) - 5
                                if index1 < 0:
                                    index1 = 0
                                if index1 > 12:
                                    index1 = 12
                            if self.sum_hand(hands[k]) <= 21:
                                self.play_casino(hand_casino)
                                if self.sum_hand(hand_casino) > 21:
                                    bust_casino += 1
                                if self.sum_hand(hand_casino) < self.sum_hand(hands[k]) or self.sum_hand(hand_casino)>21:
                                    gain += factor*1*0.5
                                    winrate_player += 1/2
                                    list_card_winrate[index3] += 1/2
                                    if played_split:
                                        winrates_split[index_casino][index_player] += 1/2
                                if self.sum_hand(hand_casino) > self.sum_hand(hands[k]) and self.sum_hand(hand_casino)<=21:
                                    gain -= factor*1*0.5
                                if self.sum_hand(hand_casino) == self.sum_hand(hands[k]):
                                    winrates_split[index_casino][index_player] += 1/4
                            else:
                                bust_player += 1
                                gain -= factor*1*0.5
            #Cas de l'As
            if ((card1.value == 1) ^ (card2.value == 1)) and not played:
                played = True
                index1 = max(card1.value,card2.value) - 2
                if card3.value == 1:
                    index2 = 9
                if card3.value != 1:
                    index2 = card3.value - 2
                while (self.strat1[index1][index2] == 1 or self.strat1[index1][index2] == 2) and self.sum_hand(hand_player) <= 21:
                    if self.strat1[index1][index2] == 2 and len(hand_player) == 2:
                        card = self.draw()
                        hand_player.append(card)
                        self.count(card)
                        factor *= 2
                        break
                    card = self.draw()
                    self.count(card)
                    hand_player.append(card)
                    index1 = self.sum_hand(hand_player) - 5
                    if index1 < 0:
                        index1 = 0
                    if index1 > 12:
                        index1 = 12
                if self.sum_hand(hand_player) <= 21:
                    self.play_casino(hand_casino)
                    if self.sum_hand(hand_casino) > 21:
                        bust_casino += 1
                    if self.sum_hand(hand_casino) < self.sum_hand(hand_player) or self.sum_hand(hand_casino)>21:
                        gain += factor*1
                        winrate_player += 1
                        list_card_winrate[index3] += 1
                        if played_ace:
                            winrates_ace[index_casino][index_player] += 1
                    if self.sum_hand(hand_casino) > self.sum_hand(hand_player) and self.sum_hand(hand_casino)<=21:
                        gain -= factor*1
                else:
                    bust_player += 1
                    gain -= factor*1
            #Cas normal
            elif not played:
                index1 = self.sum_hand(hand_player) - 5
                if index1 < 0:
                    index1 = 0
                if index1 > 12:
                    index1 = 12
                if card3.value == 1:
                    index2 = 9
                if card3.value != 1:
                    index2 = card3.value - 2
                while (self.strat1[index1][index2] == 1 or self.strat1[index1][index2] == 2) and self.sum_hand(hand_player) <= 21:
                    if self.strat1[index1][index2] == 2 and len(hand_player) == 2:
                        card = self.draw()
                        hand_player.append(card)
                        self.count(card)
                        factor *= 2
                        break
                    card = self.draw()
                    self.count(card)
                    hand_player.append(card)
                    index1 = self.sum_hand(hand_player) - 5
                    if index1 < 0:
                        index1 = 0
                    if index1 > 12:
                        index1 = 12
                if self.sum_hand(hand_player) <= 21:
                    self.play_casino(hand_casino)
                    if self.sum_hand(hand_casino) > 21:
                        bust_casino += 1
                    if self.sum_hand(hand_casino) < self.sum_hand(hand_player) or self.sum_hand(hand_casino)>21:
                        gain += factor*1
                        winrate_player += 1
                        list_card_winrate[index3] += 1
                        if played_normal:
                            winrates_normal[index_casino][index_player] += 1
                        if played_split:
                            winrates_split[index_casino][index_player] += 1
                    if self.sum_hand(hand_casino) == self.sum_hand(hand_player):
                        if played_normal:
                            winrates_normal[index_casino][index_player] += 1/2
                        if played_split:
                            winrates_split[index_casino][index_player] += 1/2
                    if self.sum_hand(hand_casino) > self.sum_hand(hand_player) and self.sum_hand(hand_casino)<=21:
                        gain -= factor*1
                else:
                    bust_player += 1
                    gain -= factor*1
        for k in range(10):
            list_card_winrate[k] = round(list_card_winrate[k] * 100 /list_card_played[k],2)
        if graph_type == 1 or graph_type == 5:
            x = ('2','3','4','5','6','7','8','9','10','A')
            X = np.arange(len(x))
            ax = plt.axes()
            ax.set_xticks(X, x)
            for i in range(len(X)):
                plt.text(i,list_card_winrate[i] + 1,f"{list_card_winrate[i]}%", ha = "center")
            plt.text(8, 55, f"Espérance de gain: {round(gain*100/n, 2)}%", ha = "center")
            plt.bar(X, list_card_winrate)
            ax.set_xlabel("Première carte du dealer")
            ax.set_ylabel("Taux de réussite (en %)")
            plt.title(f"Taux de réussite du joueur face à chaque première carte possible du dealer. Taux de réussite moyen: {round(winrate_player * 100 /n, 2)}%")

        if graph_type == 2 or graph_type == 5:
            for i in range(10):
                for j in range(15):
                    winrates_normal[i][j] = round((winrates_normal[i][j]/hands_played_normal[i][j])*100,1)
            size_x = 15
            size_y = 10
            x_start = 0
            x_end = 15
            y_start = 0
            y_end = 10
            extent = [x_start,x_end, y_end, y_start]
            fig = plt.figure(figsize=(8,8))
            ax = fig.add_subplot(111)
            axes = plt.gca()
            axes.set_ylabel('Première carte du dealer')
            axes.yaxis.set_ticks(np.arange(0.5,10.5))
            axes.yaxis.set_ticklabels(['A','10','9','8','7','6','5','4','3','2'], rotation = 0, color = 'red',fontsize = 12)
            axes.set_xlabel('Main du joueur')
            axes.xaxis.set_ticks(np.arange(0.5,15.5))
            axes.xaxis.set_ticklabels([str(i) for i in range(5,20)], rotation = 0, color = 'green', verticalalignment = 'center',fontsize = 12)
            im = ax.imshow(winrates_normal,extent = extent, cmap="RdYlGn",vmin = 0, vmax = 100)
            plt.title("Taux de réussite de chaque main possible (sans As ni double)", pad = 22)
            
            jump_x = (x_end - x_start) / (2.0 * size_x)
            jump_y = (y_end - y_start) / (2.0 * size_y)
            x_positions = np.linspace(start=x_start, stop=x_end, num=size_x, endpoint=False)
            y_positions = np.linspace(start=y_start, stop=y_end, num=size_y, endpoint=False)
            
            for y_index, y in enumerate(y_positions):
                for x_index, x in enumerate(x_positions):
                    label = winrates_normal[y_index][x_index]
                    text_x = x + jump_x
                    text_y = y + jump_y
                    ax.text(text_x, text_y, label, color='black', ha='center', va='center')
            for dealerhand in range(10):
                S = 0
                S2 = 0
                for winrate in range(15):
                    S += winrates_normal[dealerhand][winrate] * hands_played_normal[dealerhand][winrate]
                    S2 += hands_played_normal[dealerhand][winrate]
                S = S/S2
                ax.text(15 + jump_x, dealerhand + jump_y, round(S,1), color='black', ha='center', va='center')
            for winrate in range(15):
                S = 0
                S2 = 0
                for dealerhand in range(10):
                    S += winrates_normal[dealerhand][winrate] * hands_played_normal[dealerhand][winrate]
                    S2 += hands_played_normal[dealerhand][winrate]
                S = S/S2
                ax.text(winrate + jump_x, -jump_y/2, round(S,1), color='black', ha='center', va='center')
            fig.colorbar(im)
        
        if graph_type == 3 or graph_type == 5:
            for i in range(10):
                for j in range(10):
                    winrates_split[i][j] = round((winrates_split[i][j]/hands_played_split[i][j])*100,1)
            size_x = 10
            size_y = 10
            x_start = 0
            x_end = 10
            y_start = 0
            y_end = 10
            extent = [x_start,x_end, y_end, y_start]
            fig = plt.figure(figsize=(8,8))
            ax = fig.add_subplot(111)
            axes = plt.gca()
            axes.set_ylabel('Première carte du dealer')
            axes.yaxis.set_ticks(np.arange(0.5,10.5))
            axes.yaxis.set_ticklabels(['A','10','9','8','7','6','5','4','3','2'], rotation = 0, color = 'red',fontsize = 12)
            axes.set_xlabel('Main du joueur')
            axes.xaxis.set_ticks(np.arange(0.5,10.5))
            axes.xaxis.set_ticklabels([f"{i}-{i}" for i in range(2,11)] + ["A-A"], rotation = 0, color = 'green', verticalalignment = 'center',fontsize = 12)
            im = ax.imshow(winrates_split,extent = extent, cmap="RdYlGn",vmin = 0, vmax = 100)
            plt.title("Taux de réussite de chaque main possible (seulement les doubles)", pad = 22)
            
            jump_x = (x_end - x_start) / (2.0 * size_x)
            jump_y = (y_end - y_start) / (2.0 * size_y)
            x_positions = np.linspace(start=x_start, stop=x_end, num=size_x, endpoint=False)
            y_positions = np.linspace(start=y_start, stop=y_end, num=size_y, endpoint=False)
            
            for y_index, y in enumerate(y_positions):
                for x_index, x in enumerate(x_positions):
                    label = winrates_split[y_index][x_index]
                    text_x = x + jump_x
                    text_y = y + jump_y
                    ax.text(text_x, text_y, label, color='black', ha='center', va='center')
            for dealerhand in range(10):
                S = 0
                S2 = 0
                for winrate in range(10):
                    S += winrates_split[dealerhand][winrate] * hands_played_split[dealerhand][winrate]
                    S2 += hands_played_split[dealerhand][winrate]
                S = S/S2
                ax.text(10 + jump_x, dealerhand + jump_y, round(S,1), color='black', ha='center', va='center')
            for winrate in range(10):
                S = 0
                S2 = 0
                for dealerhand in range(10):
                    S += winrates_split[dealerhand][winrate] * hands_played_split[dealerhand][winrate]
                    S2 += hands_played_split[dealerhand][winrate]
                S = S/S2
                ax.text(winrate + jump_x, -jump_y/2, round(S,1), color='black', ha='center', va='center')
            fig.colorbar(im)
        
        if graph_type == 4 or graph_type == 5:
            for i in range(10):
                for j in range(9):
                    winrates_ace[i][j] = round((winrates_ace[i][j]/hands_played_ace[i][j])*100,1)
            size_x = 9
            size_y = 10
            x_start = 0
            x_end = 9
            y_start = 0
            y_end = 10
            extent = [x_start,x_end, y_end, y_start]
            fig = plt.figure(figsize=(8,8))
            ax = fig.add_subplot(111)
            axes = plt.gca()
            axes.set_ylabel('Première carte du dealer')
            axes.yaxis.set_ticks(np.arange(0.5,10.5))
            axes.yaxis.set_ticklabels(['A','10','9','8','7','6','5','4','3','2'], rotation = 0, color = 'red',fontsize = 12)
            axes.set_xlabel('Main du joueur')
            axes.xaxis.set_ticks(np.arange(0.5,9.5))
            axes.xaxis.set_ticklabels(['A-2','A-3','A-4','A-5','A-6','A-7','A-8','A-9','A-10'], rotation = 0, color = 'green', verticalalignment = 'center',fontsize = 12)
            im = ax.imshow(winrates_ace,extent = extent, cmap="RdYlGn",vmin = 0, vmax = 100)
            plt.title("Taux de réussite de chaque main possible (avec un As dans la main)", pad = 22)
            
            jump_x = (x_end - x_start) / (2.0 * size_x)
            jump_y = (y_end - y_start) / (2.0 * size_y)
            x_positions = np.linspace(start=x_start, stop=x_end, num=size_x, endpoint=False)
            y_positions = np.linspace(start=y_start, stop=y_end, num=size_y, endpoint=False)
            
            for y_index, y in enumerate(y_positions):
                for x_index, x in enumerate(x_positions):
                    label = winrates_ace[y_index][x_index]
                    text_x = x + jump_x
                    text_y = y + jump_y
                    ax.text(text_x, text_y, label, color='black', ha='center', va='center')
            for dealerhand in range(10):
                S = 0
                S2 = 0
                for winrate in range(9):
                    S += winrates_ace[dealerhand][winrate] * hands_played_ace[dealerhand][winrate]
                    S2 += hands_played_ace[dealerhand][winrate]
                S = S/S2
                ax.text(9 + jump_x, dealerhand + jump_y, round(S,1), color='black', ha='center', va='center')
            for winrate in range(9):
                S = 0
                S2 = 0
                for dealerhand in range(10):
                    S += winrates_ace[dealerhand][winrate] * hands_played_ace[dealerhand][winrate]
                    S2 += hands_played_ace[dealerhand][winrate]
                S = S/S2
                ax.text(winrate + jump_x, -jump_y/2, round(S,1), color='black', ha='center', va='center')
            fig.colorbar(im)

        # print(gain/n,winrate_player/n,bust_player/n,bust_casino/n,number_count/n)
        if graph_type >= 1:
            plt.show()
        return(round(gain*100/n,2))

