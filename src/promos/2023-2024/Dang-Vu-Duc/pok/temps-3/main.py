from poker import Poker_methods, Card, Plot_stats
import json
from operator import itemgetter
from UI_poker import UI_stats
from PySide6.QtWidgets import QApplication
import sys

# test = Poker_methods()
# test.test_duels(100)
# print(test.get_winrate_from_database("7", "7", True, 12, 14, "trèfle", "carreau"))


# test.test_duels(100)
# hand1 = [Card(10, "coeur"), Card(9, "coeur")]
# hand2 = [Card(10, "trèfle"), Card(9, "pique")]
# board = [Card(4, "coeur"), Card(14, "coeur"), Card(11, "coeur"), Card(6, "pique"), Card(2, "carreau")]
# hand3 = [Card(10, "pique"), Card(13, "carreau")]
# print(test.do_first_player_win(hand1, hand2, board))


# list_results, list_results_detail = test.get_all_average_winrates(5000)
# list_results = sorted(list_results, key = itemgetter(1), reverse = True)

# print(list_results)

# with open("all_average_winrates5.json", "w") as fp:
#     json.dump(list_results, fp)

# with open("all_average_winrates_detail5.json", "w") as fp:
#     json.dump(list_results_detail, fp)

# results_list = test.all_average_winrates2


# test_plot = Plot_stats()

# test_plot.plot_hands_ranking(1, 20)

# test_plot.plot_stats_combinations(10000000)
# print(test.get_all_possible_hands[100][0].name,test.get_all_possible_hands[100][1].name)
# print(len(test.get_all_possible_hands))

# player_hand = [Card(14, "coeur"), Card(7, "coeur")]
# board = [Card(13, "coeur"), Card(10, "coeur"), Card(11, "coeur"), Card(12, "coeur"), Card(9, "coeur")]
# print(test.get_score(player_hand, board))


app = QApplication(sys.argv)
window = UI_stats()
app.exec()
