import pygame
from chess_code import Cell, Piece, Pawn, Rook, Knight, Queen, Bishop, King, Chessboard
from sys import exit
import copy
import math
import asyncio

class Chess_game(Chessboard):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.set_starting_board()
        self.screen = pygame.display.set_mode((900, 550))
        self.chessboard_surface = pygame.image.load('chessboard.png')
        self.size = 480
        self.cell_size = self.size // 8
        self.chessboard_surface = pygame.transform.scale(self.chessboard_surface, (self.size, self.size))
        self.delta_x = 150
        self.delta_y = 30
        self.background_color = "White"
        self.screen.fill(self.background_color)
        self.font = pygame.font.Font(None, 30)
        pygame.display.set_caption("Jeu d'échecs")
        self.clock = pygame.time.Clock()
        self.black_rook_surface = pygame.image.load('Chess_pieces_png/black_rook.png')
        self.black_rook_surface = pygame.transform.scale(self.black_rook_surface, (self.cell_size, self.cell_size))
        self.black_knight_surface = pygame.image.load('Chess_pieces_png/black_knight.png')
        self.black_knight_surface = pygame.transform.scale(self.black_knight_surface, (self.cell_size, self.cell_size))
        self.black_bishop_surface = pygame.image.load('Chess_pieces_png/black_bishop.png')
        self.black_bishop_surface = pygame.transform.scale(self.black_bishop_surface, (self.cell_size, self.cell_size))
        self.black_king_surface = pygame.image.load('Chess_pieces_png/black_king.png')
        self.black_king_surface = pygame.transform.scale(self.black_king_surface, (self.cell_size, self.cell_size))
        self.black_queen_surface = pygame.image.load('Chess_pieces_png/black_queen.png')
        self.black_queen_surface = pygame.transform.scale(self.black_queen_surface, (self.cell_size, self.cell_size))
        self.black_pawn_surface = pygame.image.load('Chess_pieces_png/black_pawn.png')
        self.black_pawn_surface = pygame.transform.scale(self.black_pawn_surface, (self.cell_size, self.cell_size))

        self.white_rook_surface = pygame.image.load('Chess_pieces_png/white_rook.png')
        self.white_rook_surface = pygame.transform.scale(self.white_rook_surface, (self.cell_size, self.cell_size))
        self.white_knight_surface = pygame.image.load('Chess_pieces_png/white_knight.png')
        self.white_knight_surface = pygame.transform.scale(self.white_knight_surface, (self.cell_size, self.cell_size))
        self.white_bishop_surface = pygame.image.load('Chess_pieces_png/white_bishop.png')
        self.white_bishop_surface = pygame.transform.scale(self.white_bishop_surface, (self.cell_size, self.cell_size))
        self.white_king_surface = pygame.image.load('Chess_pieces_png/white_king.png')
        self.white_king_surface = pygame.transform.scale(self.white_king_surface, (self.cell_size, self.cell_size))
        self.white_queen_surface = pygame.image.load('Chess_pieces_png/white_queen.png')
        self.white_queen_surface = pygame.transform.scale(self.white_queen_surface, (self.cell_size, self.cell_size))
        self.white_pawn_surface = pygame.image.load('Chess_pieces_png/white_pawn.png')
        self.white_pawn_surface = pygame.transform.scale(self.white_pawn_surface, (self.cell_size, self.cell_size))
        
        self.state = "piece_not_selected"
        self.coord_piece_selected = None
        self.cells_selected = []
        self.IsWhiteToPlay = True

        self.scrolled = False
        self.move_list = []
        self.move_count = 1
        self.scroll_count = 0
        self.font_moves_size = 27
        self.limit = 18
        self.font_moves = pygame.font.Font(None, self.font_moves_size)

        self.en_passant_cell = None

        self.pieces_taken_by_white = []
        self.pieces_taken_by_black = []
        self.pieces_taken_size = 25
        self.black_rook_surface2 = pygame.image.load('Chess_pieces_png/black_rook.png')
        self.black_rook_surface2 = pygame.transform.scale(self.black_rook_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.black_knight_surface2 = pygame.image.load('Chess_pieces_png/black_knight.png')
        self.black_knight_surface2 = pygame.transform.scale(self.black_knight_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.black_bishop_surface2 = pygame.image.load('Chess_pieces_png/black_bishop.png')
        self.black_bishop_surface2  = pygame.transform.scale(self.black_bishop_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.black_king_surface2 = pygame.image.load('Chess_pieces_png/black_king.png')
        self.black_king_surface2 = pygame.transform.scale(self.black_king_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.black_queen_surface2 = pygame.image.load('Chess_pieces_png/black_queen.png')
        self.black_queen_surface2 = pygame.transform.scale(self.black_queen_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.black_pawn_surface2 = pygame.image.load('Chess_pieces_png/black_pawn.png')
        self.black_pawn_surface2 = pygame.transform.scale(self.black_pawn_surface2, (self.pieces_taken_size, self.pieces_taken_size))

        self.white_rook_surface2 = pygame.image.load('Chess_pieces_png/white_rook.png')
        self.white_rook_surface2 = pygame.transform.scale(self.white_rook_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.white_knight_surface2 = pygame.image.load('Chess_pieces_png/white_knight.png')
        self.white_knight_surface2 = pygame.transform.scale(self.white_knight_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.white_bishop_surface2 = pygame.image.load('Chess_pieces_png/white_bishop.png')
        self.white_bishop_surface2 = pygame.transform.scale(self.white_bishop_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.white_king_surface2 = pygame.image.load('Chess_pieces_png/white_king.png')
        self.white_king_surface2 = pygame.transform.scale(self.white_king_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.white_queen_surface2 = pygame.image.load('Chess_pieces_png/white_queen.png')
        self.white_queen_surface2 = pygame.transform.scale(self.white_queen_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.white_pawn_surface2 = pygame.image.load('Chess_pieces_png/white_pawn.png')
        self.white_pawn_surface2 = pygame.transform.scale(self.white_pawn_surface2, (self.pieces_taken_size, self.pieces_taken_size))
        self.font_pieces_taken = pygame.font.Font(None, 25)


        self.move_sound = pygame.mixer.Sound('Sounds/move.ogg')
        self.capture_sound = pygame.mixer.Sound('Sounds/capture.ogg')
        self.check_sound = pygame.mixer.Sound('Sounds/check.ogg')
        self.castle_sound = pygame.mixer.Sound('Sounds/castle.ogg')

    async def run(self):
        while True:
            self.screen.fill(self.background_color)
            if self.state == "solve_puzzle":
                pass
            else:
                if (-1 * self.scroll_count * 2) > math.ceil(len(self.move_list)/2) * 2 - self.limit * 2 :
                    self.scroll_count = -(math.ceil(len(self.move_list)/2) * 2 - self.limit * 2) // 2
                elif self.scroll_count >= 0:
                    self.scroll_count = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.player_click()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        self.scrolled = True
                        self.scroll_count -= 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        self.scrolled = True
                        self.scroll_count += 1
                    if event.type == pygame.MOUSEWHEEL:
                        self.scrolled = True
                        self.scroll_count += event.y
                self.screen.blit(self.chessboard_surface, (self.delta_x, self.delta_y))
                self.display_position()
                self.display_moves()
                self.display_pieces_taken()
                self.display_restart_button()
                self.display_solve_puzzle_button()
                if self.state != "game_finished":
                    self.display_who_to_play()
                else:
                    self.display_winner(not self.IsWhiteToPlay)
                self.update_possible_moves()
            pygame.display.update()
            await asyncio.sleep(0)
            self.clock.tick(60)

    def remove_text(self):
        white_rect = pygame.Rect(0, 0, self.size + self.delta_x, self.delta_y)
        pygame.draw.rect(self.screen, self.background_color, white_rect)

    def display_who_to_play(self):
        self.remove_text()
        if self.IsWhiteToPlay:
            text_white_to_play = self.font.render("Au tour des Blancs", False, "Black")
            text_rect = text_white_to_play.get_rect(center = (self.size//2 + self.delta_x, self.delta_y//2))
            self.screen.blit(text_white_to_play, text_rect)
        else:
            text_black_to_play = self.font.render("Au tour des Noirs", False, "Black")
            text_rect = text_black_to_play.get_rect(center = (self.size//2 + self.delta_x, self.delta_y//2))
            self.screen.blit(text_black_to_play, text_rect)

    def remove_moves(self):
        coord_x = self.delta_x + self.size
        coord_y = self.delta_y
        white_rect = pygame.Rect(coord_x, coord_y, 700, 700)
        pygame.draw.rect(self.screen, self.background_color, white_rect)

    def display_moves(self):
        self.remove_moves()
        delta_move_x = 100
        delta_move_y = 10
        if len(self.move_list) > self.limit * 2:
            max_scroll_count = math.ceil(len(self.move_list)/2) * 2 - self.limit * 2
            if (-1 * self.scroll_count * 2) == max_scroll_count or not self.scrolled:
                list_move_to_display = self.move_list[max_scroll_count:]
                if len(list_move_to_display) % 2 == 1:
                    list_move_to_display.append(["", ""])
            else:
                index_start = - self.scroll_count * 2
                index_end = index_start + self.limit * 2
                list_move_to_display = self.move_list[index_start:index_end]
        else:
            list_move_to_display = self.move_list[:]
            self.scroll_count = 0
        for k in range(len(list_move_to_display)):
            coord_y = self.delta_y + (k // 2) * self.font_moves_size + delta_move_y
            if k % 2 == 0:
                coord_x = self.delta_x + self.size + delta_move_x
                text_move = self.font_moves.render(list_move_to_display[k][1], False, "Black")
                text_rect = text_move.get_rect(center = (coord_x, coord_y))
                self.screen.blit(text_move, text_rect)

                coord_x2 = self.delta_x + self.size + delta_move_x - 50
                text_move2 = self.font_moves.render(str(list_move_to_display[k][0]) + ".", False, "Black")
                text_rect2 = text_move2.get_rect(center = (coord_x2, coord_y))
                self.screen.blit(text_move2, text_rect2)
            if k % 2 == 1:
                coord_x = self.delta_x + self.size + delta_move_x + 70
                text_move = self.font_moves.render(list_move_to_display[k][1], False, "Black")
                text_rect = text_move.get_rect(center = (coord_x, coord_y))
                self.screen.blit(text_move, text_rect)

    def display_winner(self, is_white_winner):
        self.remove_text()
        if is_white_winner:
            text_white_winner = self.font.render("Les Blancs ont gagné !", False, "Black")
            text_rect = text_white_winner.get_rect(center = (self.size//2 + self.delta_x, self.delta_y//2))
            self.screen.blit(text_white_winner, text_rect)
        if not is_white_winner:
            text_black_winner = self.font.render("Les Noirs ont gagné !", False, "Black")
            text_rect = text_black_winner.get_rect(center = (self.size//2 + self.delta_x, self.delta_y//2))
            self.screen.blit(text_black_winner, text_rect)

    def display_pieces_taken(self):
        white_rect = pygame.Rect(0, 0, self.delta_x, self.delta_y + self.size)
        pygame.draw.rect(self.screen, self.background_color, white_rect)
        score = self.evaluation()

        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 1.5*self.cell_size
        black_pawn_rect = self.black_pawn_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.black_pawn_surface2, black_pawn_rect)
        text_black_pawn_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_white.count('')}", False, "Black")
        text_rect = text_black_pawn_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_black_pawn_taken, text_rect)

        coord_x += 55
        black_knight_rect = self.black_knight_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.black_knight_surface2, black_knight_rect)
        text_black_knight_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_white.count('n')}", False, "Black")
        text_rect = text_black_knight_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_black_knight_taken, text_rect)

        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 1*self.cell_size
        black_bishop_rect = self.black_bishop_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.black_bishop_surface2, black_bishop_rect)
        text_black_bishop_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_white.count('b')}", False, "Black")
        text_rect = text_black_bishop_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_black_bishop_taken, text_rect)

        coord_x += 55
        black_rook_rect = self.black_rook_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.black_rook_surface2, black_rook_rect)
        text_black_rook_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_white.count('r')}", False, "Black")
        text_rect = text_black_rook_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_black_rook_taken, text_rect)

        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 0.5*self.cell_size
        black_queen_rect = self.black_queen_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.black_queen_surface2, black_queen_rect)
        text_black_queen_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_white.count('q')}", False, "Black")
        text_rect = text_black_queen_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_black_queen_taken, text_rect)
        
        if score == 1000000 or score == -1000000:
            coord_x += 45
            text_score = self.font_pieces_taken.render("#", False, "Black")
            text_rect = text_score.get_rect(midtop = (coord_x + 23, coord_y + 5))
            self.screen.blit(text_score, text_rect)
        elif score > 0:
            coord_x += 45
            text_score = self.font_pieces_taken.render(f"+{score}", False, "Black")
            text_rect = text_score.get_rect(midtop = (coord_x + 23, coord_y + 5))
            self.screen.blit(text_score, text_rect)


        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 8*self.cell_size
        white_pawn_rect = self.white_pawn_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.white_pawn_surface2, white_pawn_rect)
        text_white_pawn_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_black.count('')}", False, "Black")
        text_rect = text_white_pawn_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_white_pawn_taken, text_rect)

        coord_x += 55
        white_knight_rect = self.white_knight_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.white_knight_surface2, white_knight_rect)
        text_white_knight_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_black.count('N')}", False, "Black")
        text_rect = text_white_knight_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_white_knight_taken, text_rect)

        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 7.5*self.cell_size
        white_bishop_rect = self.white_bishop_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.white_bishop_surface2, white_bishop_rect)
        text_white_bishop_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_black.count('B')}", False, "Black")
        text_rect = text_white_bishop_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_white_bishop_taken, text_rect)

        coord_x += 55
        white_rook_rect = self.white_rook_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.white_rook_surface2, white_rook_rect)
        text_white_rook_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_black.count('R')}", False, "Black")
        text_rect = text_white_rook_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_white_rook_taken, text_rect)

        coord_x = self.delta_x - 100
        coord_y = self.delta_y + self.size - 7*self.cell_size
        white_queen_rect = self.white_queen_surface2.get_rect(midtop = (coord_x, coord_y))
        self.screen.blit(self.white_queen_surface2, white_queen_rect)
        text_white_queen_taken = self.font_pieces_taken.render(f"x{self.pieces_taken_by_black.count('Q')}", False, "Black")
        text_rect = text_white_queen_taken.get_rect(midtop = (coord_x + 23, coord_y + 5))
        self.screen.blit(text_white_queen_taken, text_rect)


        if score == 1000000 or score == -1000000:
            coord_x += 45
            text_score = self.font_pieces_taken.render("#", False, "Black")
            text_rect = text_score.get_rect(midtop = (coord_x + 23, coord_y + 5))
            self.screen.blit(text_score, text_rect)
        elif score < 0:
            coord_x += 45
            text_score = self.font_pieces_taken.render(f"+{-score}", False, "Black")
            text_rect = text_score.get_rect(midtop = (coord_x + 23, coord_y + 5))
            self.screen.blit(text_score, text_rect)

    def display_restart_button(self):
        font_restart = pygame.font.Font(None, 27)
        coord_x = self.delta_x - 75
        coord_y = self.delta_y + self.size//2 - 20
        text_restart = font_restart.render("Recommencer", False, "Black")
        text_rect = text_restart.get_rect(center = (coord_x, coord_y))
        rect_restart = pygame.Rect(self.delta_x - 143, coord_y - 15, 135, 30)
        pygame.draw.rect(self.screen, "Gray", rect_restart)
        self.screen.blit(text_restart, text_rect)

    def player_click(self):
        pos = pygame.mouse.get_pos()
        if pos[0] in range(self.delta_x - 143, self.delta_x - 143 + 135) and pos[1] in range(self.delta_y + self.size//2 - 20 - 15, self.delta_y + self.size//2 - 20 - 15 + 30):
            self.restart()
        elif pos[0] in range(self.delta_x - 143, self.delta_x - 143 + 135) and pos[1] in range(self.delta_y + self.size//2 + 20 - 15, self.delta_y + self.size//2 + 20 - 15 + 30):
            # self.state = "solve_puzzle"
            print("coucou")
        elif self.get_row_column() != None:
            if self.state == "piece_not_selected":
                nb_row, nb_column = self.get_row_column()        
                piece = self.board[nb_row][nb_column][1]
                if piece != None and piece.IsWhite == self.IsWhiteToPlay:# and piece.possible_moves != []:
                    self.state = "piece_selected"
                    self.update_cells_selected(piece)
                    self.coord_piece_selected = (nb_row, nb_column)
            elif self.state == "piece_selected":
                nb_row, nb_column = self.get_row_column()
                cell_clicked = self.board[nb_row][nb_column][0]
                piece_clicked = self.board[nb_row][nb_column][1]
                final_cell = None
                for cell in self.cells_selected[1]:
                    if cell_clicked.name == cell.name:
                        final_cell = cell
                        break
                if final_cell != None:
                    self.move_piece(cell_clicked, final_cell)
                elif piece_clicked != None and piece_clicked.IsWhite == self.IsWhiteToPlay and piece_clicked.possible_moves != []:
                    self.state = "piece_selected"
                    self.update_cells_selected(piece_clicked)
                    self.coord_piece_selected = (nb_row, nb_column)
                else:
                    self.state = "piece_not_selected"
                    self.cells_selected = []
        else:
            self.state = "piece_not_selected"
            self.cells_selected = []
        if self.IsCheckmate(self.IsWhiteToPlay):
            self.state = "game_finished"

    def restart(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j] = [Cell(i, j), None]
        self.set_starting_board()
        self.pieces_taken_by_black = []
        self.pieces_taken_by_white = []
        self.state = "piece_not_selected"
        self.coord_piece_selected = None
        self.cells_selected = []
        self.IsWhiteToPlay = True
        self.scrolled = False
        self.move_list = []
        self.move_count = 1
        self.scroll_count = 0

    def move_piece(self, cell_clicked, final_cell):
        piece = self.board[final_cell.row][final_cell.column][1]
        capture = False
        en_passant = False
        if piece != None and self.IsWhiteToPlay:
            self.pieces_taken_by_white.append(piece.letter)
            capture = True
        if piece != None and not self.IsWhiteToPlay:
            self.pieces_taken_by_black.append(piece.letter)
            capture = True
        move_name = self.get_move_name(self.cells_selected[0], final_cell)
        self.move_list.append([self.move_count, move_name])
        if not self.IsWhiteToPlay:
            self.move_count += 1
        original_piece = self.board[self.cells_selected[0].row][self.cells_selected[0].column][1]
        if self.en_passant_cell != None and cell_clicked.name == self.en_passant_cell.name and original_piece.letter == "" and original_piece.IsWhite == self.IsWhiteToPlay:
            self.move_en_passant(self.cells_selected[0], final_cell)
            en_passant = True
        else:
            self.move(self.cells_selected[0], final_cell)
        if original_piece.letter == "" and original_piece.IsWhite and final_cell.row == 3 and self.cells_selected[0].row == 1:
            self.en_passant_cell = Cell(final_cell.row - 1, final_cell.column)
        elif original_piece.letter == "" and not original_piece.IsWhite and final_cell.row == 4 and self.cells_selected[0].row == 6:
            self.en_passant_cell = Cell(final_cell.row + 1, final_cell.column)
        else:
            self.en_passant_cell = None
        if self.IsCheck(not self.IsWhiteToPlay):
            self.check_sound.play()
        elif capture or en_passant:
            self.capture_sound.play()
        elif final_cell.short_castle or final_cell.long_castle:
            self.castle_sound.play()
        else:
            self.move_sound.play()

        self.IsWhiteToPlay = not self.IsWhiteToPlay
        self.state = "piece_not_selected"
        self.cells_selected = []
        self.scrolled = False
        self.scroll_count = -(math.ceil(len(self.move_list)/2) * 2 - self.limit * 2) // 2

    def move_en_passant(self, initial_cell, final_cell):
        if self.IsWhiteToPlay:
            delta = -1
        else:
            delta = 1
        self.board[final_cell.row + delta][final_cell.column][1] = None
        self.board[initial_cell.row][initial_cell.column][1] = None
        self.board[final_cell.row][final_cell.column][1] = Pawn(self.IsWhiteToPlay, Cell(final_cell.row, final_cell.column))
        if self.IsWhiteToPlay:
            self.pieces_taken_by_white.append("")
        else:
            self.pieces_taken_by_black.append("")

    def update_cells_selected(self, piece):
        valid_moves = []
        current_cell = copy.deepcopy(piece.current_cell)
        initial_board = copy.deepcopy(self.board[:])
        if self.en_passant_cell != None and piece.letter == "":
            adjacent_column1 = self.en_passant_cell.column - 1
            adjacent_column2 = self.en_passant_cell.column + 1
            if piece.current_cell.column in [adjacent_column1, adjacent_column2]:
                if piece.current_cell.row + 1 == self.en_passant_cell.row and piece.IsWhite:
                    piece.en_passant = self.en_passant_cell
                    piece.possible_moves.append(self.en_passant_cell)
                    valid_moves.append(self.en_passant_cell)
                elif piece.current_cell.row - 1 == self.en_passant_cell.row and not piece.IsWhite:
                    piece.en_passant = self.en_passant_cell
                    piece.possible_moves.append(self.en_passant_cell)
                    valid_moves.append(self.en_passant_cell)
        for cell in piece.possible_moves:
            if cell.short_castle:
                if self.IsWhiteToPlay:
                    row = 0
                else:
                    row = 7
                if not self.IsCheck(self.IsWhiteToPlay):
                    self.move(current_cell, Cell(row, 5))
                    if not self.IsCheck(self.IsWhiteToPlay):
                        self.board = copy.deepcopy(initial_board)
                        self.move(current_cell, Cell(row, 6))
                        if not self.IsCheck(self.IsWhiteToPlay):
                            valid_moves.append(copy.deepcopy(cell))
                            self.board = copy.deepcopy(initial_board)
                        else:
                            self.board = copy.deepcopy(initial_board)
                    else:
                        self.board = copy.deepcopy(initial_board)
            elif cell.long_castle:
                if self.IsWhiteToPlay:
                    row = 0
                else:
                    row = 7
                if not self.IsCheck(self.IsWhiteToPlay):
                    self.move(current_cell, Cell(row, 2))
                    if not self.IsCheck(self.IsWhiteToPlay):
                        self.board = copy.deepcopy(initial_board)
                        self.move(current_cell, Cell(row, 3))
                        if not self.IsCheck(self.IsWhiteToPlay):
                            valid_moves.append(copy.deepcopy(cell))
                            self.board = copy.deepcopy(initial_board)
                        else:
                            self.board = copy.deepcopy(initial_board)
                    else:
                        self.board = copy.deepcopy(initial_board)
            else:
                self.move(current_cell, cell)
                if not self.IsCheck(self.IsWhiteToPlay):
                    valid_moves.append(copy.deepcopy(cell))
                self.board = copy.deepcopy(initial_board)
        self.cells_selected = [piece.current_cell, copy.deepcopy(valid_moves)]

    def draw_rect(self, nb_row, nb_column, color):
        coord_x = self.delta_x + nb_column * self.cell_size
        coord_y = self.delta_y + self.size - (nb_row + 1) * self.cell_size
        rect = pygame.Rect(coord_x + 1, coord_y + 1, self.cell_size - 1 , self.cell_size)
        pygame.draw.rect(self.screen, color, rect)

    def draw_check(self):
        flag = False
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(len(row)):
                cell = row[j]
                if cell[1] != None and cell[1].letter in ["k", "K"] and cell[1].IsWhite == self.IsWhiteToPlay:
                    self.draw_rect(i, j, "Red")
                    flag = True
                    break
            if flag:
                break

    def get_row_column(self):
        pos = pygame.mouse.get_pos()
        pos_x = pos[0] - self.delta_x
        pos_y = pos[1] - self.delta_y
        if (pos_x in range(0, self.size + 1)) and (pos_y in range(0, self.size + 1)):
            nb_row = 7 - (pos_y // self.cell_size)
            nb_column = pos_x // self.cell_size
            return(nb_row, nb_column)
        else:
            return(None)

    def get_coordinates(self, nb_row, nb_column):
        coord_y = self.size - self.cell_size//2 + self.delta_y - self.cell_size * nb_row
        coord_x = self.cell_size//2 + self.delta_x + self.cell_size * nb_column
        return(coord_x, coord_y)

    def display_position(self):
        if self.state == "piece_selected":
            nb_row, nb_column = self.coord_piece_selected
            if self.cells_selected[1] != []:
                self.draw_rect(nb_row, nb_column, "steelblue4")
        if self.cells_selected != []:
            for cell in self.cells_selected[1]:
                self.draw_rect(cell.row, cell.column, "lightblue3")
        if self.IsCheck(self.IsWhiteToPlay):
            self.draw_check()
        for row in self.board:
            for cell in row:
                if cell[1] is not None:
                    piece = cell[1]
                    if piece.IsWhite:
                        coord_x, coord_y = self.get_coordinates(piece.current_cell.row, piece.current_cell.column)
                        if piece.letter == "R":
                            white_rook_rect = self.white_rook_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_rook_surface, white_rook_rect)
                        elif piece.letter == "N":
                            white_knight_rect = self.white_knight_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_knight_surface, white_knight_rect)
                        elif piece.letter == "B":
                            white_bishop_rect = self.white_bishop_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_bishop_surface, white_bishop_rect)
                        elif piece.letter == "Q":
                            white_queen_rect = self.white_queen_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_queen_surface, white_queen_rect)
                        elif piece.letter == "K":
                            white_king_rect = self.white_king_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_king_surface, white_king_rect)
                        elif piece.letter == "":
                            white_pawn_rect = self.white_pawn_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.white_pawn_surface, white_pawn_rect)
                    else:
                        coord_x, coord_y = self.get_coordinates(piece.current_cell.row, piece.current_cell.column)
                        if piece.letter == "r":
                            black_rook_rect = self.black_rook_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_rook_surface, black_rook_rect)
                        elif piece.letter == "n":
                            black_knight_rect = self.black_knight_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_knight_surface, black_knight_rect)
                        elif piece.letter == "b":
                            black_bishop_rect = self.black_bishop_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_bishop_surface, black_bishop_rect)
                        elif piece.letter == "q":
                            black_queen_rect = self.black_queen_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_queen_surface, black_queen_rect)
                        elif piece.letter == "k":
                            black_king_rect = self.black_king_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_king_surface, black_king_rect)
                        elif piece.letter == "":
                            black_pawn_rect = self.black_pawn_surface.get_rect(center = (coord_x, coord_y))
                            self.screen.blit(self.black_pawn_surface, black_pawn_rect)      
    
    def get_move_name(self, initial_cell, final_cell):
        initial_board = copy.deepcopy(self.board[:])
        move_name = ""
        if final_cell.short_castle:
            move_name = "O-O"
            self.move(initial_cell, final_cell)
            if self.IsCheckmate(not self.IsWhiteToPlay):
                move_name += "#"
            elif self.IsCheck(not self.IsWhiteToPlay):
                move_name += "+"
            self.board = copy.deepcopy(initial_board[:])
        elif final_cell.long_castle:
            move_name = "O-O-O"
            self.move(initial_cell, final_cell)
            if self.IsCheckmate(not self.IsWhiteToPlay):
                move_name += "#"
            elif self.IsCheck(not self.IsWhiteToPlay):
                move_name += "+"
            self.board = copy.deepcopy(initial_board[:])
        elif final_cell.promote != None:
            if self.board[final_cell.row][final_cell.column][1] != None:
                move_name = f"{chr(initial_cell.column + 97)}" + "x" + f"{final_cell.name}" + "=" + f"{final_cell.promote.upper()}"
            else:
                move_name = f"{final_cell.name}" + "=" + f"{final_cell.promote}"
        elif self.en_passant_cell != None and final_cell.name == self.en_passant_cell.name:
            move_name = f"{chr(initial_cell.column + 97)}" + "x" + f"{final_cell.name}"
        else:
            if self.board[initial_cell.row][initial_cell.column][1].letter == "" and self.board[final_cell.row][final_cell.column][1] != None:
                move_name = f"{chr(initial_cell.column + 97)}" + move_name
            if self.board[final_cell.row][final_cell.column][1] != None:
                move_name = f"{self.board[initial_cell.row][initial_cell.column][1].letter.upper()}" + "x" + f"{final_cell.name}"
            else:
                move_name = f"{self.board[initial_cell.row][initial_cell.column][1].letter.upper()}" + f"{final_cell.name}"
            if self.board[initial_cell.row][initial_cell.column][1].letter == "" and self.board[final_cell.row][final_cell.column][1] != None:
                move_name = f"{chr(initial_cell.column + 97)}" + move_name
            self.move(initial_cell, final_cell)
            if self.IsCheckmate(not self.IsWhiteToPlay):
                move_name = move_name + "#"
            elif self.IsCheck(not self.IsWhiteToPlay):
                move_name = move_name + "+"
            self.board = copy.deepcopy(initial_board[:])
        return(move_name)

    def set_starting_board(self):
        self.board[0][0][1] = Rook(True, Cell(0, 0))
        self.board[0][1][1] = Knight(True, Cell(0, 1))
        self.board[0][2][1] = Bishop(True, Cell(0, 2))
        self.board[0][3][1] = Queen(True, Cell(0, 3))
        self.board[0][4][1] = King(True, Cell(0, 4))
        self.board[0][5][1] = Bishop(True, Cell(0, 5))
        self.board[0][6][1] = Knight(True, Cell(0, 6))
        self.board[0][7][1] = Rook(True, Cell(0, 7))
        for k in range(8):
            self.board[1][k][1] = Pawn(True, Cell(1, k))
        
        self.board[7][0][1] = Rook(False, Cell(7, 0))
        self.board[7][1][1] = Knight(False, Cell(7, 1))
        self.board[7][2][1] = Bishop(False, Cell(7, 2))
        self.board[7][3][1] = Queen(False, Cell(7, 3))
        self.board[7][4][1] = King(False, Cell(7, 4))
        self.board[7][5][1] = Bishop(False, Cell(7, 5))
        self.board[7][6][1] = Knight(False, Cell(7, 6))
        self.board[7][7][1] = Rook(False, Cell(7, 7))
        for k in range(8):
            self.board[6][k][1] = Pawn(False, Cell(6, k))

    def display_solve_puzzle_button(self):
        font_puzzle = pygame.font.Font(None, 27)
        coord_x = self.delta_x - 75
        coord_y = self.delta_y + self.size//2 + 20
        text_puzzle = font_puzzle.render("Puzzles", False, "Black")
        text_rect = text_puzzle.get_rect(center = (coord_x, coord_y))
        rect_puzzle = pygame.Rect(self.delta_x - 143, coord_y - 15, 135, 30)
        pygame.draw.rect(self.screen, "Gray", rect_puzzle)
        self.screen.blit(text_puzzle, text_rect)

    
# app = Chess_game()
# asyncio.run(app.run())