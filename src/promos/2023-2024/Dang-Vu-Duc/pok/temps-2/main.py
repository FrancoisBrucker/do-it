from chess_code import Chessboard, Cell

test = Chessboard()

print(test.solve('8/2B4p/2p2R1K/1Pk3N1/1n1r1n2/NQP5/8/8 w - - 0 1', True, 3))  
# print(test.solve('r1b1r1k1/p5pp/2p3q1/2pP1p2/5Bn1/1PNB1K2/P1PQ1PP1/R4R2 b - - 0 1', False, 3))

# Mat en 2 trouvé en 7.7sec (mat avec deux promotions)   ['e1=n+', 'Kh2', 'f1=n#']
# print(test.solve('8/8/8/8/4n1k1/3b4/4ppK1/6NQ b - - 0 1', False, 3))

# Mat en 3 trouvé en 2min et 46.5sec (sacrifice et sous-promotion)   ['Qg8+', 'rxg8', 'f8=N+', 'kh8', 'Rh7#']
# print(test.solve('5r2/2R2P1k/7p/4q3/7K/8/6Q1/8 w - - 0 1', True, 5))

# Mat en 3 trouvé en 4min 55.5sec   ['Kd7', 'kg7', 'Nd6', 'kf8', 'Ne6#']
# print(test.solve('7b/1N3B2/3K1k2/5pN1/5P2/8/8/8 w - - 0 1', True, 5))

# Mat en 3 trouvé en 14min et 53.4sec   ['qh1+', 'Kxh1', 'rxh4+', 'Kg1', 'rh1#']
# print(test.solve('5k2/pbQ3pp/1p6/8/2P1r2N/6Pq/P4P2/5RK1 b - - 0 1', False, 5))

# Mat en 3 trouvé en 11min et 41 sec   ['Qg7', 'kxc4', 'Qd4+', 'kb3', 'Qb4#']
# print(test.solve('8/8/8/2k5/2P5/2N5/2N3Q1/3K4 w - - 0 1', True, 5))

# Mat en 3 trouvé en 16 sec   ['Bf6', 'gxf6', 'Kf8', 'f5', 'Nf7#']
# print(test.solve('7k/4K1pp/7N/8/8/8/8/B7 w - - 0 1', True, 5))

# Mat en 3 trouvé en 59 sec   ['Be3', 'bc3', 'Bg5', 'ba1', 'g4#']
# print(test.solve('8/8/8/5K1k/5B2/6P1/6P1/4b3 w - - 0 1', True, 5))  

# Mat en 3 trouvé en 9min et 10.8sec   ['Qh1', 'kxg5', 'Ng2', 'hxg2', 'h4#']
# print(test.solve('Q7/5p2/5P1p/5PPN/6Pk/4N1Rp/7P/6K1 w - - 0 1', True, 5))

# Mat en 3 trouvé en 24min   ['Ke2', 'nc1+', 'Ke3', 'na2', 'd4#']
# print(test.solve('4r1b1/1p4B1/pN2pR2/RB2k3/1P2N2p/2p3b1/n2P1p1r/5K1n w - - 0 1', True, 5))

# Mat en 3 trouvé en 27min et 36.5sec   ['Qxc6+', 'qd6', 'Nd4+', 'nxd4', 'Qxd6#']
# print(test.solve('2b3r1/R4p2/2p1kBpp/2qpPn2/Qp4P1/5N2/5P1P/6K1 w - - 0 1', True, 5))  

# Mat en 3 trouvé en 8min et 54.5sec   ['Bh3', 'e4', 'Qg4', 'e3', 'Qc8#']
# print(test.solve('8/pk1B4/p7/2K1p3/8/8/4Q3/8 w - - 0 1', True, 5))

# Mat en 3 trouvé en 8min et 41.1sec   ['Nd4', 'nd2', 'Rxc3+', 'qc2', 'Rxc2#']
# print(test.solve('7K/p1p5/P1P5/8/q1P5/p1pRNN1p/Bp5P/1nk5 w - - 0 1', True, 5))

# Mat en 4 trouvé en 12min et 51.7sec   ['Bh5', 'kxh5', 'Kg7', 'h6', 'Kf6', 'kh4', 'Kg6#']
# print(test.solve('3BB2K/7p/7k/8/8/5P1p/7P/8 w - - 0 1', True, 7))



# test.board = test.get_position_from_fen('4n3/8/Q3N1pR/3rk1K1/3Bq3/8/B7/4R3 w - - 0 1')[0]
# test.update_possible_moves()
# moves = test.get_all_possible_moves(True)
# moves2 = []
# for k in range(len(moves)):
#     letter = test.board[moves[k][0].row][moves[k][0].column][1].letter
#     for i in range(len(moves[k][1])):
#         moves2.append(letter + moves[k][1][i].name)
# print(moves2)
# print(test.IsCheckmate(False))

# piece = test.board[1][4][1]
# moves = piece.possible_moves
# print("----------------------------------")
# piece.get_possible_moves(test.board)
# moves2 = [move.name for move in moves]
# print(piece.letter, moves2)

# test.update_possible_moves()
# print(test.IsCheck(True))
# test.move(Cell(4,7), Cell(4,6))
# print(test.IsCheck(True))

# piece = test_board[2][0][1]
# print(f"current cell: {piece.current_cell.name}")
# for move in piece.possible_moves:
#     print(move.name)
