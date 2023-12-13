import copy
import time

class Cell():
    def __init__(self, row, column, promote = None):
        self.name = chr(column + 97) + f"{row+1}"
        self.row = row
        self.column = column
        self.promote = promote

class Piece():
    def __init__(self, IsWhite, value, letter, current_cell):
        self.possible_moves = []
        self.current_cell = current_cell
        self.IsWhite = IsWhite
        self.value = value
        self.letter = letter

class King(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 1000, "K", current_cell)
        else:
            super().__init__(IsWhite, -1000, "k", current_cell)

    def get_possible_moves(self, board):
        self.possible_moves = []
        column = self.current_cell.column
        row = self.current_cell.row
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if not (k == 0 and l == 0):
                    new_column = column + k
                    new_row = row + l
                    if new_row <= 7 and new_column <= 7 and new_row >= 0 and new_column >= 0 :
                        if board[new_row][new_column][1] is None: 
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                        else:
                            obstacle_color = board[new_row][new_column][1].IsWhite
                            if obstacle_color ^ self.IsWhite:
                                new_cell = Cell(new_row, new_column)
                                self.possible_moves.append(new_cell)

class Rook(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 5, "R", current_cell)
        else:
            super().__init__(IsWhite, -5, "r", current_cell)
    
    def get_possible_moves(self, board):
        self.possible_moves = []
        for k in [-1, 1]:
            new_column = self.current_cell.column + k
            new_row = self.current_cell.row
            while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                if board[new_row][new_column][1] is None: 
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                else:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                    break
                new_column = new_column + k
        for l in [-1, 1]:
            new_column = self.current_cell.column
            new_row = self.current_cell.row + l
            while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                if board[new_row][new_column][1] is None: 
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                else:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                    break
                new_row = new_row + l

class Knight(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 3, "N", current_cell)
        else:
            super().__init__(IsWhite, -3, "n", current_cell)

    def get_possible_moves(self, board):
        self.possible_moves = []
        column = self.current_cell.column
        row = self.current_cell.row
        L = [-1, -2, 1, 2]
        for k in L:
            temp_L = [-1, -2, 1, 2]
            temp_L.remove(k)
            temp_L.remove(-k)
            for l in temp_L:
                new_column = column + k
                new_row = row + l
                if new_row <= 7 and new_column <= 7 and new_row >= 0 and new_column >= 0:
                    if board[new_row][new_column][1] is None: 
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                    else:
                        obstacle_color = board[new_row][new_column][1].IsWhite
                        if obstacle_color ^ self.IsWhite:
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
        
class Bishop(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 3, "B", current_cell)
        else:
            super().__init__(IsWhite, -3, "b", current_cell)
    
    def get_possible_moves(self, board):
        self.possible_moves = []
        for k in [-1, 1]:
            for l in [-1, 1]:
                new_column = self.current_cell.column + k
                new_row = self.current_cell.row + l
                while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                    if board[new_row][new_column][1] is None: 
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                    else:
                        obstacle_color = board[new_row][new_column][1].IsWhite
                        if obstacle_color ^ self.IsWhite:
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                        break
                    new_column = new_column + k
                    new_row = new_row + l

class Queen(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 9, "Q", current_cell)
        else:
            super().__init__(IsWhite, -9, "q", current_cell)
    
    def get_possible_moves(self, board):
        self.possible_moves = []
        for k in [-1, 1]:
            new_column = self.current_cell.column + k
            new_row = self.current_cell.row
            while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                if board[new_row][new_column][1] is None: 
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                else:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                    break
                new_column = new_column + k
        for l in [-1, 1]:
            new_column = self.current_cell.column
            new_row = self.current_cell.row + l
            while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                if board[new_row][new_column][1] is None: 
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                else:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
                    break
                new_row = new_row + l
        for k in [-1, 1]:
            for l in [-1, 1]:
                new_column = self.current_cell.column + k
                new_row = self.current_cell.row + l
                while new_column >= 0 and new_column <= 7 and new_row >= 0 and new_row <= 7:
                    if board[new_row][new_column][1] is None: 
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                    else:
                        obstacle_color = board[new_row][new_column][1].IsWhite
                        if obstacle_color ^ self.IsWhite:
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                        break
                    new_column = new_column + k
                    new_row = new_row + l

class Pawn(Piece):
    def __init__(self, IsWhite, current_cell):
        if IsWhite:
            super().__init__(IsWhite, 1, "", current_cell)
        else:
            super().__init__(IsWhite, -1, "", current_cell)
    
    
    def get_possible_moves(self, board):
        if self.IsWhite:
            move = 1
        else:
            move = -1
        self.possible_moves = []
        if self.current_cell.row == 6 and self.IsWhite:
            new_column = self.current_cell.column + 0
            new_row = self.current_cell.row + move
            if new_column >= 0 and new_column <= 7:
                self.possible_moves.append(Cell(new_row, new_column, "Q"))
                self.possible_moves.append(Cell(new_row, new_column, "N"))
                self.possible_moves.append(Cell(new_row, new_column, "B"))
                self.possible_moves.append(Cell(new_row, new_column, "R"))
            for k in [-1, 1]:
                new_column = self.current_cell.column + k
                new_row = self.current_cell.row + move
                if new_column >= 0 and new_column <= 7:
                    if board[new_row][new_column][1] is not None:
                        obstacle_color = board[new_row][new_column][1].IsWhite
                        if obstacle_color ^ self.IsWhite:
                            self.possible_moves.append(Cell(new_row, new_column, "Q"))
                            self.possible_moves.append(Cell(new_row, new_column, "N"))
                            self.possible_moves.append(Cell(new_row, new_column, "B"))
                            self.possible_moves.append(Cell(new_row, new_column, "R"))

        elif self.current_cell.row == 1 and not self.IsWhite:
            new_column = self.current_cell.column + 0
            new_row = self.current_cell.row + move
            if new_column >= 0 and new_column <= 7:
                self.possible_moves.append(Cell(new_row, new_column, "q"))
                self.possible_moves.append(Cell(new_row, new_column, "n"))
                self.possible_moves.append(Cell(new_row, new_column, "b"))
                self.possible_moves.append(Cell(new_row, new_column, "r"))
            for k in [-1, 1]:
                new_column = self.current_cell.column + k
                new_row = self.current_cell.row + move
                if new_column >= 0 and new_column <= 7:
                    if board[new_row][new_column][1] is not None:
                        obstacle_color = board[new_row][new_column][1].IsWhite
                        if obstacle_color ^ self.IsWhite:
                            self.possible_moves.append(Cell(new_row, new_column, "q"))
                            self.possible_moves.append(Cell(new_row, new_column, "n"))
                            self.possible_moves.append(Cell(new_row, new_column, "b"))
                            self.possible_moves.append(Cell(new_row, new_column, "r"))
        else:
            if self.current_cell.row == 1 or self.current_cell.row == 6:
                for k in [1, 2]:
                    new_row = self.current_cell.row + k * move
                    new_column = self.current_cell.column + 0
                    if new_row >= 0 and new_row <= 7:
                        if board[new_row][new_column][1] is None: 
                            new_cell = Cell(new_row, new_column)
                            self.possible_moves.append(new_cell)
                        else:
                            break
                    else:
                        break
            else:
                new_row = self.current_cell.row + move
                new_column = self.current_cell.column + 0
                if new_row >= 0 and new_row <= 7:
                    if board[new_row][new_column][1] is None: 
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
            new_row = self.current_cell.row + move
            new_column = self.current_cell.column - 1
            if new_column >= 0 and new_row <= 7 and new_row >= 0:
                if board[new_row][new_column][1] is not None:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)

            new_column = self.current_cell.column + 1
            if new_column <= 7 and new_row <= 7 and new_row >= 0:
                if board[new_row][new_column][1] is not None:
                    obstacle_color = board[new_row][new_column][1].IsWhite
                    if obstacle_color ^ self.IsWhite:
                        new_cell = Cell(new_row, new_column)
                        self.possible_moves.append(new_cell)
            

class Chessboard():
    def __init__(self):
        self.board = [ [None for j in range(8)] for i in range(8) ]
        for i in range(8):
            for j in range(8):
                self.board[i][j] = [Cell(i, j), None]
    
    def get_position_from_fen(self, fen_position):
        new_board = [ [None for j in range(8)] for i in range(8) ]
        for i in range(8):
            for j in range(8):
                new_board[i][j] = [Cell(i, j), None]
        row_list = []
        word = ''
        count = 0
        for char in fen_position:
            if char != "/" and char != ' ':
                word += char
            elif char == "/":
                row_list.append(word)
                word = ''
            elif char == ' ':
                row_list.append(word)
                if fen_position[count + 1] == 'w':
                    IsWhiteToPlay = True
                else:
                    IsWhiteToPlay = False
                break
            count += 1
        nb_row = 7
        for row in row_list:
            counter = 0
            for k in range(len(row)):
                if row[k].isdigit():
                    digit = int(row[k])
                    counter += digit
                else:
                    if row[k] == 'r' or row[k] == 'R':
                        new_board[nb_row][counter][1] = Rook(row[k].isupper(), Cell(nb_row, counter))
                    elif row[k] == 'n' or row[k] == 'N':
                        new_board[nb_row][counter][1] = Knight(row[k].isupper(), Cell(nb_row, counter))
                    elif row[k] == 'b' or row[k] == 'B':
                        new_board[nb_row][counter][1] = Bishop(row[k].isupper(), Cell(nb_row, counter))
                    elif row[k] == 'k' or row[k] == 'K':
                        new_board[nb_row][counter][1] = King(row[k].isupper(), Cell(nb_row, counter))
                    elif row[k] == 'q' or row[k] == 'Q':
                        new_board[nb_row][counter][1] = Queen(row[k].isupper(), Cell(nb_row, counter))
                    elif row[k] == 'p' or row[k] == 'P':
                        new_board[nb_row][counter][1] = Pawn(row[k].isupper(), Cell(nb_row, counter))
                    counter += 1
            nb_row -= 1
        return(new_board, IsWhiteToPlay)

    def move(self, current_cell, final_cell):
        piece = self.board[current_cell.row][current_cell.column][1]
        if piece is None:
            print("Il n'y a pas de pièce dans la case indiquée")
            return()
        if (final_cell.row, final_cell.column) not in [(cell.row, cell.column) for cell in piece.possible_moves]:
            print("La pièce ne peut pas aller jusqu'à la case indiquée")
            return()
        self.board[current_cell.row][current_cell.column][1] = None
        if piece.letter == "" and (current_cell.row == 6 and piece.IsWhite):
            if final_cell.promote is None:
                print("Problème : pas de promotion")
                return()
            if final_cell.promote in ["Q", "q"]:
                self.board[final_cell.row][final_cell.column][1] = Queen(piece.IsWhite, final_cell)
            elif final_cell.promote in ["N", "n"]:
                self.board[final_cell.row][final_cell.column][1] = Knight(piece.IsWhite, final_cell)
            elif final_cell.promote in ["B", "b"]:
                self.board[final_cell.row][final_cell.column][1] = Bishop(piece.IsWhite, final_cell)
            elif final_cell.promote in ["R", "r"]:
                self.board[final_cell.row][final_cell.column][1] = Rook(piece.IsWhite, final_cell)

        elif piece.letter == "" and (current_cell.row == 1 and not piece.IsWhite):
            if final_cell.promote is None:
                print("Problème : pas de promotion", piece.letter, current_cell.name, final_cell.name, final_cell.promote)
                return()
            if final_cell.promote in ["Q", "q"]:
                self.board[final_cell.row][final_cell.column][1] = Queen(piece.IsWhite, final_cell)
            elif final_cell.promote in ["N", "n"]:
                self.board[final_cell.row][final_cell.column][1] = Knight(piece.IsWhite, final_cell)
            elif final_cell.promote in ["B", "b"]:
                self.board[final_cell.row][final_cell.column][1] = Bishop(piece.IsWhite, final_cell)
            elif final_cell.promote in ["R", "r"]:
                self.board[final_cell.row][final_cell.column][1] = Rook(piece.IsWhite, final_cell) 
        elif piece.letter in ["K", "k"]:
            self.board[final_cell.row][final_cell.column][1] = King(piece.IsWhite, final_cell)
        elif piece.letter in ["R", "r"]:
            self.board[final_cell.row][final_cell.column][1] = Rook(piece.IsWhite, final_cell)
        elif piece.letter in ["B", "b"]:
            self.board[final_cell.row][final_cell.column][1] = Bishop(piece.IsWhite, final_cell)
        elif piece.letter in ["N", "n"]:
            self.board[final_cell.row][final_cell.column][1] = Knight(piece.IsWhite, final_cell)
        elif piece.letter in ["Q", "q"]:
            self.board[final_cell.row][final_cell.column][1] = Queen(piece.IsWhite, final_cell)
        elif piece.letter in [""]:
            self.board[final_cell.row][final_cell.column][1] = Pawn(piece.IsWhite, final_cell)
        self.update_possible_moves()

    def evaluation(self):
        eval = 0
        if self.IsCheckmate(True):
            return(-1000000)
        elif self.IsCheckmate(False):
            return(1000000)
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    eval += cell[1].value
        return(eval)
    
    def CanBeCaptured(self, piece):
        captured_by = []
        opponent_moves = [[cell[0], cell[1]] for cell in self.get_all_possible_moves2(not piece.IsWhite)]
        for k in range(len(opponent_moves)):
            for i in range(len(opponent_moves[k][1])):
                current_cell = opponent_moves[k][1][i]
                if piece.current_cell.name == current_cell.name:
                    captured_by.append(opponent_moves[k][0])
                    break
        if len(captured_by) == 0:
            return(False, captured_by)
        else:
            return(True, captured_by)

    def IsCheck(self, IsWhiteToPlay):
        value = 1000 if IsWhiteToPlay else -1000
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    piece = cell[1]
                    if piece.value == value:
                        return(self.CanBeCaptured(piece)[0])

    def IsCheckmate(self, IsWhiteToPlay):
        initial_board = copy.deepcopy(self.board)
        count = 0
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    piece2 = copy.deepcopy(cell[1])
                    # print(piece2.letter, piece2.current_cell.name)
                    if (piece2.value == 1000 or piece2.value == -1000) and (piece2.IsWhite == IsWhiteToPlay):
                        list_captured = copy.deepcopy(self.CanBeCaptured(piece2)[1])
                        if self.CanBeCaptured(piece2)[0]: #Vérifie si le roi est en échec
                            current_row = piece2.current_cell.row
                            current_column = piece2.current_cell.column
                            current_cell = Cell(current_row,current_column)
                            for move in piece2.possible_moves:
                                self.move(current_cell, move)
                                new_piece = self.board[move.row][move.column][1]
                                can_be_captured = self.CanBeCaptured(new_piece)[0]
                                # print(new_piece.current_cell.name, [cell.name for cell in self.CanBeCaptured(new_piece)[1]])
                                if can_be_captured:
                                    count += 1
                                self.board = copy.deepcopy(initial_board)
                                self.update_possible_moves()
                            if count != len(piece2.possible_moves): #Vérifie si le roi peut s'échapper ou pas
                                return(False)
                            else: #Le roi ne peut pas s'échapper
                                if len(list_captured) == 1: #Une pièce met en échec
                                    cell = list_captured[0]
                                    piece_opponent = self.board[cell.row][cell.column][1]
                                    (can_be_captured2, list_captured2) = self.CanBeCaptured(piece_opponent)
                                    if can_be_captured2 and (len(list_captured2) > 1 or self.board[list_captured2[0].row][list_captured2[0].column][1].letter not in ["k", "K"]): #La pièce peut être prise par une pièce autre que le roi
                                        index = None
                                        for m in range(len(list_captured2)):
                                            if self.board[list_captured2[m].row][list_captured2[m].column][1].letter in ["K", "k"]:
                                                index = m
                                                break
                                        if index != None:
                                            list_captured2.pop(index)
                                        c = 0
                                        for cell_opponent in list_captured2:
                                            c += 1
                                            self.move(cell_opponent, piece_opponent.current_cell)
                                            if not self.IsCheck(IsWhiteToPlay): # Au moins une pièce peut prendre la pièce qui met en échec
                                                self.board = copy.deepcopy(initial_board)
                                                return(False)
                                            self.board = copy.deepcopy(initial_board)
                                        return(True)
                                    else: #La pièce ne peut pas être prise par une pièce autre que le roi
                                        cells_inbetween = []
                                        piece_opponent = self.board[list_captured[0].row][list_captured[0].column][1]
                                        row_king = piece2.current_cell.row
                                        column_king = piece2.current_cell.column
                                        if piece_opponent.letter in ["R", "r", "q", "Q"]:
                                            if piece_opponent.current_cell.column == column_king and piece_opponent.current_cell.row > row_king: #la Tour est au-dessus du roi
                                                current_column = piece_opponent.current_cell.column
                                                current_row = piece_opponent.current_cell.row - 1
                                                while current_row != row_king and current_row >= 0:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row -= 1
                                            elif piece_opponent.current_cell.column == column_king and piece_opponent.current_cell.row < row_king: #la Tour est en dessous du roi
                                                current_column = piece_opponent.current_cell.column
                                                current_row = piece_opponent.current_cell.row + 1
                                                while current_row != row_king and current_row <= 7:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row += 1
                                            elif piece_opponent.current_cell.row == row_king and piece_opponent.current_cell.column > column_king: #la Tour est à droite du roi
                                                current_column = piece_opponent.current_cell.column - 1
                                                current_row = piece_opponent.current_cell.row
                                                while current_column != column_king and current_column >= 0:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_column -= 1
                                            elif piece_opponent.current_cell.row == row_king and piece_opponent.current_cell.column < column_king: #la Tour est à gauche du roi
                                                current_column = piece_opponent.current_cell.column + 1
                                                current_row = piece_opponent.current_cell.row
                                                while current_column != column_king and current_column <= 7:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_column += 1
                                        if piece_opponent.letter in ["B", "b", "Q", "q"]:
                                            if piece_opponent.current_cell.column > column_king and piece_opponent.current_cell.row > row_king: #le Fou est en haut à droite du roi
                                                current_column = piece_opponent.current_cell.column - 1
                                                current_row = piece_opponent.current_cell.row - 1
                                                while current_row != row_king and current_column >= 0 and current_row >= 0:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row -= 1
                                                    current_column -= 1
                                            elif piece_opponent.current_cell.column < column_king and piece_opponent.current_cell.row < row_king: #le Fou est en bas à gauche du roi
                                                current_column = piece_opponent.current_cell.column + 1
                                                current_row = piece_opponent.current_cell.row + 1
                                                while current_row != row_king and current_row <= 7 and current_column <= 7:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row += 1
                                                    current_column += 1
                                            elif piece_opponent.current_cell.column > column_king and piece_opponent.current_cell.row < row_king: #le Fou est en bas à droite du roi
                                                current_column = piece_opponent.current_cell.column - 1
                                                current_row = piece_opponent.current_cell.row + 1
                                                while current_row != row_king and current_row <= 7 and current_column >= 0:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row += 1
                                                    current_column -= 1
                                            elif piece_opponent.current_cell.column < column_king and piece_opponent.current_cell.row > row_king: #le Fou est en haut à gauche du roi
                                                current_column = piece_opponent.current_cell.column + 1
                                                current_row = piece_opponent.current_cell.row - 1
                                                while current_row != row_king and current_row >= 0 and current_column <= 7:
                                                    cells_inbetween.append(self.board[current_row][current_column][0])
                                                    current_row -= 1
                                                    current_column += 1
                                        if piece_opponent.letter not in ["R", "r", "B", "b", "Q", "q"]: #La pièce qui met en échec n'est ni un fou, ni une tour, ni une Dame
                                            return(True)
                                        cells_inbetween = [cell.name for cell in cells_inbetween]
                                        all_possible_moves = copy.deepcopy(self.get_all_possible_moves(IsWhiteToPlay))
                                        ending_cells = []
                                        for n in range(len(all_possible_moves)):
                                            current_cell = all_possible_moves[n][0]
                                            if self.board[current_cell.row][current_cell.column][1].letter not in ['k', 'K']:
                                                ending_cells += all_possible_moves[n][1]
                                        ending_cells = [cell.name for cell in ending_cells]
                                        for cell in ending_cells:
                                            if cell in cells_inbetween:
                                                return(False)
                                        return(True)
                                else: #2 pièces ou plus mettent en échec
                                    return(True)
                        else:
                            return(False)
        return("test")

    def get_all_possible_moves2(self, IsWhiteToPlay):
        all_possible_moves = []
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    if cell[1].IsWhite == IsWhiteToPlay:
                        all_possible_moves.append([cell[1].current_cell, cell[1].possible_moves])
        return(all_possible_moves)
    
    def get_all_possible_moves(self, IsWhiteToPlay):
        all_possible_moves = []
        initial_board = copy.deepcopy(self.board[:])
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    self.board = copy.deepcopy(initial_board[:])
                    piece = copy.deepcopy(cell[1])
                    if piece.IsWhite == IsWhiteToPlay:
                        current_moves = []
                        index = -1
                        # killer_moves = []
                        for move in piece.possible_moves:
                            piece_opponent = copy.deepcopy(self.board[move.row][move.column][1])
                            self.move(piece.current_cell, move)
                            if not self.IsCheck(IsWhiteToPlay):
                                if self.IsCheck(not IsWhiteToPlay):
                                    current_moves = [move] + current_moves
                                elif piece_opponent != None and ((piece_opponent.IsWhite) ^ (piece.IsWhite)):
                                    current_moves = [move] + current_moves
                                elif piece.letter not in [""] and index != -1:
                                    current_moves = current_moves[:index] + [move] + current_moves[index:]
                                else:
                                    current_moves.append(move)
                                self.board = copy.deepcopy(initial_board[:])
                                index += 1
                            else:
                                self.board = copy.deepcopy(initial_board[:])
                        # current_moves = killer_moves + current_moves
                        all_possible_moves.append([piece.current_cell, current_moves])
        return(all_possible_moves)

    def update_possible_moves(self):
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    cell[1].get_possible_moves(self.board)

    def solve(self, fen_position, IsWhiteToPlay, depth):
        self.c = 0 
        self.tot = 0
        self.best_moves = [None for i in range(depth)]
        variations = []
        (self.board, IsWhiteToPlay) = self.get_position_from_fen(fen_position)
        self.update_possible_moves()
        time_begin = time.time()
        result = self.solve_assist(IsWhiteToPlay, -9999999999, 9999999999, depth)
        time_final = time.time()
        tot_time = round(time_final - time_begin, 1)
        tot_min = int((tot_time // 60) % 60)
        tot_hours = int(tot_time // 3600)
        tot_sec = round(tot_time % 60,1)
        print(f"Durée de l'exécution: {tot_hours} heures, {tot_min} minutes et {tot_sec} secondes")
        return(result)

    def solve_assist(self, IsWhiteToPlay, alpha, beta, depth):
        # print(depth, self.IsCheckmate(True))
        self.c += 1
        print(f"{self.c}/{self.tot}", self.evaluation())
        if depth == 0 or self.IsCheckmate(True) or self.IsCheckmate(False):
            return(self.evaluation(), self.best_moves)
        if IsWhiteToPlay:
            best = -99999999999
            all_possible_moves = self.get_all_possible_moves(IsWhiteToPlay)
            flag = False
            IsStalemate = True
            for k in range(len(all_possible_moves)):
                self.tot += len(all_possible_moves[k][1])
            for move in all_possible_moves:
                for i in range(len(move[1])):
                    initial_board = copy.deepcopy(self.board[:])
                    initial_best_moves = copy.deepcopy(self.best_moves[:])
                    self.move(move[0], move[1][i])
                    IsStalemate = False
                    val = self.solve_assist(not IsWhiteToPlay, alpha, beta, depth - 1)[0]
                    self.board = copy.deepcopy(initial_board[:])
                    if val > best:
                        best = val
                        next_move = ""
                        if move[1][i].promote != None:
                            if self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + "x" + f"{move[1][i].name}" + "=" + f"{move[1][i].promote}"
                            else:
                                next_move = f"{move[1][i].name}" + "=" + f"{move[1][i].promote}"
                        else:
                            if self.board[move[0].row][move[0].column][1].letter == "" and self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + next_move
                            if self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{self.board[move[0].row][move[0].column][1].letter}" + "x" + f"{move[1][i].name}"
                            else:
                                next_move = f"{self.board[move[0].row][move[0].column][1].letter}" + f"{move[1][i].name}"
                            if self.board[move[0].row][move[0].column][1].letter == "" and self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + next_move
                        self.move(move[0], move[1][i])
                        if self.IsCheckmate(not IsWhiteToPlay):
                            next_move = next_move + "#"
                        elif self.IsCheck(not IsWhiteToPlay):
                            next_move = next_move + "+"
                        self.board = copy.deepcopy(initial_board[:])
                        self.best_moves[-depth] = next_move
                    else:
                        self.best_moves = copy.deepcopy(initial_best_moves)
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        flag = True
                        break
                if flag:
                    break
            if IsStalemate:
                return(0, self.best_moves)
        else:
            best = 9999999999
            all_possible_moves = self.get_all_possible_moves(IsWhiteToPlay)
            flag = False
            IsStalemate = True
            for k in range(len(all_possible_moves)):
                self.tot += len(all_possible_moves[k][1])
            for move in all_possible_moves:
                for i in range(len(move[1])):
                    initial_board = copy.deepcopy(self.board[:])
                    initial_best_moves = copy.deepcopy(self.best_moves[:])
                    self.move(move[0], move[1][i])
                    IsStalemate = False
                    val = self.solve_assist(not IsWhiteToPlay, alpha, beta, depth - 1)[0]
                    self.board = copy.deepcopy(initial_board[:])
                    if val < best:
                        best = val
                        next_move = ""
                        if move[1][i].promote != None:
                            if self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + "x" + f"{move[1][i].name}" + "=" + f"{move[1][i].promote}"
                            else:
                                next_move = f"{move[1][i].name}" + "=" + f"{move[1][i].promote}"
                        else:
                            if self.board[move[0].row][move[0].column][1].letter == "" and self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + next_move
                            if self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{self.board[move[0].row][move[0].column][1].letter}" + "x" + f"{move[1][i].name}"
                            else:
                                next_move = f"{self.board[move[0].row][move[0].column][1].letter}" + f"{move[1][i].name}"
                            if self.board[move[0].row][move[0].column][1].letter == "" and self.board[move[1][i].row][move[1][i].column][1] != None:
                                next_move = f"{chr(move[0].column + 97)}" + next_move
                        self.move(move[0], move[1][i])
                        if self.IsCheckmate(not IsWhiteToPlay):
                            next_move = next_move + "#"
                        elif self.IsCheck(not IsWhiteToPlay):
                            next_move = next_move + "+"
                        self.board = copy.deepcopy(initial_board[:])
                        self.best_moves[-depth] = next_move
                    else:
                        self.best_moves = copy.deepcopy(initial_best_moves)
                    beta = min(beta, val)
                    if beta <= alpha:
                        flag = True
                        break
                if flag:
                    break
            if IsStalemate:
                return(0, self.best_moves)
        return(best, self.best_moves)
    
    def solve2(self, fen_position, IsWhiteToPlay, depth):
        self.c = 0 
        (self.board, IsWhiteToPlay) = self.get_position_from_fen(fen_position)
        self.update_possible_moves()
        return(self.solve_assist2(IsWhiteToPlay, [None for i in range(depth)], depth, IsWhiteToPlay))
    
    def solve_assist2(self, IsWhiteToPlay, depth):
        # print(depth, self.IsCheckmate(True))
        self.c += 1
        print(self.c, self.IsCheckmate(False), self.evaluation())
        if depth == 0 or self.IsCheckmate(True) or self.IsCheckmate(False):
            return(self.evaluation())
        flag = False
        if IsWhiteToPlay:
            best_moves = []
            best = - 99999999
            all_possible_moves = self.get_all_possible_moves(IsWhiteToPlay)
            for move in all_possible_moves:
                for i in range(len(move[1])):
                    initial_board = copy.deepcopy(self.board[:])
                    self.move(move[0], move[1][i])
                    if not self.IsCheck(IsWhiteToPlay):
                        val = self.solve_assist2(not IsWhiteToPlay, best_moves, depth - 1)[0]
                        if val > best:
                            self.board = copy.deepcopy(initial_board[:])
                            best_moves = [f"{self.board[move[0].row][move[0].column][1].letter}" + f"{move[1][i].name}"]
                        self.board = copy.deepcopy(initial_board[:])
                    else:
                        self.board = copy.deepcopy(initial_board[:])
                if flag:
                    break
        # else:
        #     all_possible_moves = self.get_all_possible_moves(IsWhiteToPlay)
        #     flag = False
        #     for move in all_possible_moves:
        #         for i in range(len(move[1])):
        #             initial_board = copy.deepcopy(self.board[:])
        #             self.move(move[0], move[1][i])
        #             if not self.IsCheck(IsWhiteToPlay):
        #                 end = self.solve_assist2(not IsWhiteToPlay, best_moves, depth - 1)
        #                 if end:
        #                     best_moves[depth - 1] = f"{self.board[move[0].row][move[0].column][1].letter}" + f"{move[1][i].name}"
        #                 self.board = copy.deepcopy(initial_board[:])
        #             else:
        #                 self.board = copy.deepcopy(initial_board[:])
