import pygame
from sys import exit

class TicTacToe():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.background_color = "White"
        self.screen.fill(self.background_color)
        pygame.display.set_caption("Morpion")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 33)
        self.morpion_surface = pygame.image.load('Plateau morpion.png')
        self.title_surface = self.font.render('Jeu du morpion', False, "Black")
        self.text_rect = self.title_surface.get_rect(center = (400, 30))
        self.board = [[None for j in range(3)] for i in range(3)]
        self.playing = True

    def game(self):
        self.is_player_one_to_play = True
        self.display_who_to_play(True)
        self.count = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player_click()
            # self.screen.blit(self.morpion_surface, (160, 30))
            self.draw_board()
            pygame.display.update()
            self.clock.tick(60)

    def draw_board(self):
        board_rect = pygame.Rect(200, 50, 400, 400)
        pygame.draw.rect(self.screen, "Black", board_rect, 4)
        pygame.draw.line(self.screen, "Black", (333.333333, 50),(333.333333, 450), 4)
        pygame.draw.line(self.screen, "Black", (466.666666, 50),(466.666666, 450), 4)
        pygame.draw.line(self.screen, "Black", (200, 183.3333),(600, 183.333), 4)
        pygame.draw.line(self.screen, "Black", (200, 316.6663),(600, 316.6663), 4)
        button_restart = pygame.Rect(620, 230, 160, 40)
        pygame.draw.rect(self.screen, "Gray", button_restart)
        text_restart = self.font.render("Recommencer", False, "Black")
        self.screen.blit(text_restart, (623,237))
        

    def display_winner(self, is_player_one_winner):
        self.remove_text()
        if is_player_one_winner:
            text_player_one_wins = self.font.render("Le joueur 1 a gagné !", False, "Blue")
            text_rect = text_player_one_wins.get_rect(center = (400, 30))
            self.screen.blit(text_player_one_wins, text_rect)
        else:
            text_player_one_wins = self.font.render("Le joueur 2 a gagné !", False, "Red")
            text_rect = text_player_one_wins.get_rect(center = (400, 30))
            self.screen.blit(text_player_one_wins, text_rect)
        self.playing = False

    def display_draw(self):
        self.remove_text()
        text_draw = self.font.render("Égalité !", False, "Black")
        text_rect = text_draw.get_rect(center = (400, 30))
        self.screen.blit(text_draw, text_rect)

    def remove_text(self):
        white_rect = pygame.Rect(0, 0, 700, 50)
        pygame.draw.rect(self.screen, self.background_color, white_rect)
        

    def display_who_to_play(self, is_player_one_to_play):
        self.remove_text()
        if is_player_one_to_play:
            text_player_one_to_play = self.font.render("Au tour du joueur 1", False, "Blue")
            text_rect = text_player_one_to_play.get_rect(center = (400, 30))
            self.screen.blit(text_player_one_to_play, text_rect)
        else:
            text_player_one_to_play = self.font.render("Au tour du joueur 2", False, "Red")
            text_rect = text_player_one_to_play.get_rect(center = (400, 30))
            self.screen.blit(text_player_one_to_play, text_rect)

    def check(self):
        if (self.board[0][0] != None and self.board[0][0]) and (self.board[1][1] != None and self.board[1][1]) and (self.board[2][2] != None and self.board[2][2]):
            self.display_winner(True)
        elif (self.board[0][0] != None and not self.board[0][0]) and (self.board[1][1] != None and not self.board[1][1]) and (self.board[2][2] != None and not self.board[2][2]):
            self.display_winner(False)
        elif (self.board[0][0] != None and self.board[0][0]) and (self.board[0][1] != None and self.board[0][1]) and (self.board[0][2] != None and self.board[0][2]):
            self.display_winner(True)
        elif (self.board[0][0] != None and not self.board[0][0]) and (self.board[0][1] != None and not self.board[0][1]) and (self.board[0][2] != None and not self.board[0][2]):
            self.display_winner(False)
        elif (self.board[0][0] != None and self.board[0][0]) and (self.board[1][0] != None and self.board[1][0]) and (self.board[2][0] != None and self.board[2][0]):
            self.display_winner(True)
        elif (self.board[0][0] != None and not self.board[0][0]) and (self.board[1][0] != None and not self.board[1][0]) and (self.board[2][0] != None and not self.board[2][0]):
            self.display_winner(False)
        elif (self.board[1][0] != None and self.board[1][0]) and (self.board[1][1] != None and self.board[1][1]) and (self.board[1][2] != None and self.board[1][2]):
            self.display_winner(True)
        elif (self.board[1][0] != None and not self.board[1][0]) and (self.board[1][1] != None and not self.board[1][1]) and (self.board[1][2] != None and not self.board[1][2]):
            self.display_winner(False)
        elif (self.board[0][1] != None and self.board[0][1]) and (self.board[1][1] != None and self.board[1][1]) and (self.board[2][1] != None and self.board[2][1]):
            self.display_winner(True)
        elif (self.board[0][1] != None and not self.board[0][1]) and (self.board[1][1] != None and not self.board[1][1]) and (self.board[2][1] != None and not self.board[2][1]):
            self.display_winner(False)
        elif (self.board[2][0] != None and self.board[2][0]) and (self.board[2][1] != None and self.board[2][1]) and (self.board[2][2] != None and self.board[2][2]):
            self.display_winner(True)
        elif (self.board[2][0] != None and not self.board[2][0]) and (self.board[2][1] != None and not self.board[2][1]) and (self.board[2][2] != None and not self.board[2][2]):
            self.display_winner(False)
        elif (self.board[0][2] != None and self.board[0][2]) and (self.board[1][2] != None and self.board[1][2]) and (self.board[2][2] != None and self.board[2][2]):
            self.display_winner(True)
        elif (self.board[0][2] != None and not self.board[0][2]) and (self.board[1][2] != None and not self.board[1][2]) and (self.board[2][2] != None and not self.board[2][2]):
            self.display_winner(False)
        elif (self.board[2][0] != None and self.board[2][0]) and (self.board[1][1] != None and self.board[1][1]) and (self.board[0][2] != None and self.board[0][2]):
            self.display_winner(True)
        elif (self.board[2][0] != None and not self.board[2][0]) and (self.board[1][1] != None and not self.board[1][1]) and (self.board[0][2] != None and not self.board[0][2]):
            self.display_winner(False)
        elif self.count == 9:
            self.display_draw()

    def play(self, spot):
        if self.is_player_one_to_play:
            if spot == 1:
                pygame.draw.circle(self.screen, "Blue", (266.66, 116.65), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 2:
                pygame.draw.circle(self.screen, "Blue", (400, 116.65), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 3:
                pygame.draw.circle(self.screen, "Blue", (533.33, 116.65), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 4:
                pygame.draw.circle(self.screen, "Blue", (266.66, 250), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 5:
                pygame.draw.circle(self.screen, "Blue", (400, 250), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 6:
                pygame.draw.circle(self.screen, "Blue", (533.33, 250), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 7:
                pygame.draw.circle(self.screen, "Blue", (266.66, 383.3), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 8:
                pygame.draw.circle(self.screen, "Blue", (400, 383.3), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 9:
                pygame.draw.circle(self.screen, "Blue", (533.33, 383.3), 50, 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
        else:
            if spot == 1:
                pygame.draw.line(self.screen, "Red", (216.66, 66.65), (316.66, 166.65), 4)
                pygame.draw.line(self.screen, "Red", (216.66, 166.65), (316.66, 66.65), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 2:
                pygame.draw.line(self.screen, "Red", (350, 66.65), (450, 166.65), 4)
                pygame.draw.line(self.screen, "Red", (350, 166.65), (450, 66.65), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 3:
                pygame.draw.line(self.screen, "Red", (483.33, 66.65), (583.33, 166.65), 4)
                pygame.draw.line(self.screen, "Red", (483.33, 166.65), (583.33, 66.65), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 4:
                pygame.draw.line(self.screen, "Red", (216.66, 200), (316.66, 300), 4)
                pygame.draw.line(self.screen, "Red", (216.66, 300), (316.66, 200), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 5:
                pygame.draw.line(self.screen, "Red", (350, 200), (450, 300), 4)
                pygame.draw.line(self.screen, "Red", (350, 300), (450, 200), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 6:
                pygame.draw.line(self.screen, "Red", (483.33, 200), (583.33, 300), 4)
                pygame.draw.line(self.screen, "Red", (483.33, 300), (583.33, 200), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 7:
                pygame.draw.line(self.screen, "Red", (216.66, 333.33), (316.66, 433.33), 4)
                pygame.draw.line(self.screen, "Red", (216.66, 433.33), (316.66, 333.33), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 8:
                pygame.draw.line(self.screen, "Red", (350, 333.33), (450, 433.33), 4)
                pygame.draw.line(self.screen, "Red", (350, 433.33), (450, 333.33), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
            if spot == 9:
                pygame.draw.line(self.screen, "Red", (483.33, 333.33), (583.33, 433.33), 4)
                pygame.draw.line(self.screen, "Red", (483.33, 433.33), (583.33, 333.33), 4)
                self.is_player_one_to_play = not self.is_player_one_to_play
        self.display_who_to_play(self.is_player_one_to_play)

    def restart(self):
        self.screen.fill(self.background_color)
        self.draw_board()
        self.is_player_one_to_play = True
        self.playing = True
        self.display_who_to_play(self.is_player_one_to_play)
        self.board = [[None for j in range(3)] for i in range(3)]
        self.count = 0

    def player_click(self):
        pos = pygame.mouse.get_pos()
        if pos[0] in range(620, 780) and pos[1] in range(230, 270):
            self.restart()
        if self.playing:
            if pos[0] in range(200, 333) and pos[1] in range(50, 183) and self.board[0][0] == None:
                self.board[0][0] = self.is_player_one_to_play
                self.play(1)
                self.count += 1
            if pos[0] in range(334, 466) and pos[1] in range(50, 183) and self.board[1][0] == None:
                self.board[1][0] = self.is_player_one_to_play
                self.play(2)
                self.count += 1
            if pos[0] in range(467, 600) and pos[1] in range(50, 183) and self.board[2][0] == None:
                self.board[2][0] = self.is_player_one_to_play
                self.play(3)
                self.count += 1
            if pos[0] in range(200, 333) and pos[1] in range(183, 316) and self.board[0][1] == None:
                self.board[0][1] = self.is_player_one_to_play
                self.play(4)
                self.count += 1
            if pos[0] in range(334, 466) and pos[1] in range(183, 316) and self.board[1][1] == None:
                self.board[1][1] = self.is_player_one_to_play
                self.play(5)
                self.count += 1
            if pos[0] in range(467, 600) and pos[1] in range(183, 316) and self.board[2][1] == None:
                self.board[2][1] = self.is_player_one_to_play
                self.play(6)
                self.count += 1
            if pos[0] in range(200, 333) and pos[1] in range(317, 450) and self.board[0][2] == None:
                self.board[0][2] = self.is_player_one_to_play
                self.play(7)
                self.count += 1
            if pos[0] in range(334, 466) and pos[1] in range(317, 450) and self.board[1][2] == None:
                self.board[1][2] = self.is_player_one_to_play
                self.play(8)
                self.count += 1
            if pos[0] in range(467, 600) and pos[1] in range(317, 450) and self.board[2][2] == None:
                self.board[2][2] = self.is_player_one_to_play
                self.play(9)
                self.count += 1
            self.check()
