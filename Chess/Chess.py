
import os
import tkinter as tk
from tkinter import messagebox

# マップの広さ
HEIGHT = 8
WIDTH = 8
# 先行、後攻のターン
FIRST = 0
SECOND = 1

CPU = 0
USER = 1


class Chess():
    # コンストラクタ
    def __init__(self, app):
        self.app = app
        # 今、コマのいる位置を保存しておくリスト
        self.cells = None
        # 移動できるところを保存しておくリスト
        self.move_cells = None
        # 一つ前に押したところを保存しておく連想配列
        self.save_cell = None

        self.height = HEIGHT
        self.width = WIDTH
        # プレイヤー
        self.player = None

        self.user_name = None
        self.cpu_name = None

        self.turn = None
        self.now_turn = FIRST

        self.labels = None

        self.init_cells()

        self.init_move_cells()

        self.placement_piece()

        # ↓GUIの作成
        self.create_widgets()

        self.set_events()
        # debug呼び出し
        # cellsの中身の確認
        self.test_cells()

        self.test_move_cells()

        self.test_player_cells()

    # cellsの初期化
    def init_cells(self):
        self.cells = [[dict() for i in range(self.width)]
                      for j in range(self.height)]
    # 移動できる場所を保持する配列の初期化

    def init_move_cells(self):
        self.move_cells = [[bool() for i in range(self.width)]
                           for j in range(self.height)]

    # 先行後攻選択
    def select_turn(self):
        # 先行を押した時の処理
        if self.turn == FIRST:
            self.player = CPU
        # 後攻を押した時の処理
        elif self.turn == SECOND:
            self.player = USER

    # コマの配置

    def placement_piece(self):
        null_dict = {
            "player": "",
            "chess_piece": ""
        }
        cpu_pawn_dict = {
            "player": "CPU",
            "chess_piece": "PAWN"
        }
        cpu_rook_dict = {
            "player": "CPU",
            "chess_piece": "ROOK"
        }
        cpu_knight_dict = {
            "player": "CPU",
            "chess_piece": "KNIGHT"
        }
        cpu_bishop_dict = {
            "player": "CPU",
            "chess_piece": "BISHOP"
        }
        cpu_king_dict = {
            "player": "CPU",
            "chess_piece": "KING"
        }
        cpu_queen_dict = {
            "player": "CPU",
            "chess_piece": "QUEEN"
        }
        user_pawn_dict = {
            "player": "USER",
            "chess_piece": "PAWN"
        }
        user_rook_dict = {
            "player": "USER",
            "chess_piece": "ROOK"
        }
        user_knight_dict = {
            "player": "USER",
            "chess_piece": "KNIGHT"
        }
        user_bishop_dict = {
            "player": "USER",
            "chess_piece": "BISHOP"
        }
        user_king_dict = {
            "player": "USER",
            "chess_piece": "KING"
        }
        user_queen_dict = {
            "player": "USER",
            "chess_piece": "QUEEN"
        }

        for i in range(self.height):
            for j in range(self.height):
                # CPUのコマ配置
                if (i == 1):
                    self.cells[i][j] = cpu_pawn_dict.copy()
                elif (i == 0 and j == 0) or (i == 0 and j == 7):
                    self.cells[i][j] = cpu_rook_dict.copy()
                elif (i == 0 and j == 1) or (i == 0 and j == 6):
                    self.cells[i][j] = cpu_knight_dict.copy()
                elif (i == 0 and j == 2) or (i == 0 and j == 5):
                    self.cells[i][j] = cpu_bishop_dict.copy()
                elif (i == 0 and j == 3):
                    self.cells[i][j] = cpu_king_dict.copy()
                elif (i == 0 and j == 4):
                    self.cells[i][j] = cpu_queen_dict.copy()
                # USERのコマ配置
                elif (i == 6):
                    self.cells[i][j] = user_pawn_dict.copy()
                elif (i == 7 and j == 0) or (i == 7 and j == 7):
                    self.cells[i][j] = user_rook_dict.copy()
                elif (i == 7 and j == 1) or (i == 7 and j == 6):
                    self.cells[i][j] = user_knight_dict.copy()
                elif (i == 7 and j == 2) or (i == 7 and j == 5):
                    self.cells[i][j] = user_bishop_dict.copy()
                elif (i == 7 and j == 3):
                    self.cells[i][j] = user_king_dict.copy()
                elif (i == 7 and j == 4):
                    self.cells[i][j] = user_queen_dict.copy()
                else:
                    self.cells[i][j] = null_dict.copy()

    def is_pawn_move(self, player, x, y):
        if player == "CPU":
            reverse_player = "USER"
            one = 1
            two = 2
            row = 1

        elif player == "USER":
            reverse_player = "CPU"
            one = -1
            two = -2
            row = 6

        if (x + one) >= 0 and (x + one) < self.height and not self.cells[x + one][y]["player"] == reverse_player:
            if x == row and not self.cells[x + two][y]["player"] == reverse_player and not self.cells[x + two][y]["player"] == player:
                self.move_cells[y][x + one] = True
                self.move_cells[y][x + two] = True
            elif not self.cells[x + one][y]["player"] == player:
                self.move_cells[y][x + one] = True

        if (x + one) >= 0 and (y - 1) >= 0 and (x + one) < self.height and (y - 1) < self.width:
            if self.cells[x + one][y - 1]["player"] == reverse_player:
                self.move_cells[y - 1][x + one] = True

        if (x + one) >= 0 and (y + 1) >= 0 and (x + one) < self.height and (y + 1) < self.width:
            if self.cells[x + one][y + 1]["player"] == reverse_player:
                self.move_cells[y + 1][x + one] = True

    def is_rook_move(self, player, x, y):

        if player == "CPU":
            reverse_player = "USER"
        elif player == "USER":
            reverse_player = "CPU"

        for i in range(4):
            for j in range(8):
                if i == 0 and not j == 0 and (y - j) >= 0 and (y - j) < self.height:
                    if self.cells[x][y - j]["player"] == player:
                        break
                    elif self.cells[x][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x] = True
                        break
                    elif not (y - j == y) and not self.cells[x][y - j]["player"] == player:
                        self.move_cells[y - j][x] = True
                elif i == 1 and not j == 0 and (y + j) >= 0 and (y + j) < self.height:
                    if self.cells[x][y + j]["player"] == player:
                        break
                    elif self.cells[x][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x] = True
                        break
                    elif not (y + j == y) and not self.cells[x][y + j]["player"] == player:
                        self.move_cells[y + j][x] = True
                elif i == 2 and not j == 0 and (x - j) >= 0 and (x - j) < self.height:
                    if self.cells[x - j][y]["player"] == player:
                        break
                    elif self.cells[x - j][y]["player"] == reverse_player:
                        self.move_cells[y][x - j] = True
                        break
                    elif not (x - j == x) and not self.cells[x - j][y]["player"] == player:
                        self.move_cells[y][x - j] = True
                elif i == 3 and not j == 0 and (x + j) >= 0 and (x + j) < self.height:
                    if self.cells[x + j][y]["player"] == player:
                        break
                    elif self.cells[x + j][y]["player"] == reverse_player:
                        self.move_cells[y][x + j] = True
                        break
                    elif not (x + j == x) and not self.cells[x + j][y]["player"] == player:
                        self.move_cells[y][x + j] = True
                else:
                    continue

    def is_knight_move(self, player, x, y):
        if y - 2 >= 0 and x - 1 >= 0 and y - 2 < self.height and x - 1 < self.width:
            if not self.cells[x-1][y-2]["player"] == player:
                self.move_cells[y - 2][x - 1] = True

        if y - 1 >= 0 and x - 2 >= 0 and y - 1 < self.height and x - 2 < self.width:
            if not self.cells[x-2][y-1]["player"] == player:
                self.move_cells[y - 1][x - 2] = True

        if y - 2 >= 0 and x + 1 >= 0 and y - 2 < self.height and x + 1 < self.width:
            if not self.cells[x+1][y-2]["player"] == player:
                self.move_cells[y - 2][x + 1] = True

        if y - 1 >= 0 and x + 2 >= 0 and y - 1 < self.height and x + 2 < self.width:
            if not self.cells[x+2][y-1]["player"] == player:
                self.move_cells[y - 1][x + 2] = True

        if y + 1 >= 0 and x - 2 >= 0 and y + 1 < self.height and x - 2 < self.width:
            if not self.cells[x-2][y+1]["player"] == player:
                self.move_cells[y + 1][x - 2] = True

        if y + 2 >= 0 and x - 1 >= 0 and y + 2 < self.height and x - 1 < self.width:
            if not self.cells[x-1][y+2]["player"] == player:
                self.move_cells[y + 2][x - 1] = True

        if y + 2 >= 0 and x + 1 >= 0 and y + 2 < self.height and x + 1 < self.width:
            if not self.cells[x+1][y+2]["player"] == player:
                self.move_cells[y + 2][x + 1] = True

        if y + 1 >= 0 and x + 2 >= 0 and y + 1 < self.height and x + 2 < self.width:
            if not self.cells[x+2][y+1]["player"] == player:
                self.move_cells[y + 1][x + 2] = True

    def is_bishop_move(self, player, x, y):
        if player == "CPU":
            reverse_player = "USER"
        elif player == "USER":
            reverse_player = "CPU"

        for i in range(4):
            for j in range(8):
                if i == 0 and not j == 0 and y - j >= 0 and x - j >= 0 and y - j < self.height and x - j < self.width:
                    if self.cells[x - j][y - j]["player"] == player:
                        break
                    elif self.cells[x - j][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x - j] = True
                        break
                    elif not (y - j == y and x - j == x) and not self.cells[x - j][y - j]["player"] == player:
                        self.move_cells[y - j][x - j] = True
                elif i == 1 and not j == 0 and y - j >= 0 and x + j >= 0 and y - j < self.height and x + j < self.width:
                    if self.cells[x + j][y - j]["player"] == player:
                        break
                    elif self.cells[x + j][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x + j] = True
                        break
                    elif not (y - j == y and x + j == x) and not self.cells[x + j][y - j]["player"] == player:
                        self.move_cells[y - j][x + j] = True

                elif i == 2 and not j == 0 and y + j >= 0 and x - j >= 0 and y + j < self.height and x - j < self.width:
                    if self.cells[x - j][y + j]["player"] == player:
                        break
                    elif self.cells[x - j][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x - j] = True
                        break
                    elif not (y + j == y and x - j == x) and not self.cells[x - j][y + j]["player"] == player:
                        self.move_cells[y + j][x - j] = True

                elif i == 3 and not j == 0 and y + j >= 0 and x + j >= 0 and y + j < self.height and x + j < self.width:
                    if self.cells[x + j][y + j]["player"] == player:
                        break
                    elif self.cells[x + j][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x + j] = True
                        break
                    elif not (y + j == y and x + j == x) and not self.cells[x + j][y + j]["player"] == player:
                        self.move_cells[y + j][x + j] = True
                else:
                    continue

    def is_king_move(self, player, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if y + i >= 0 and x + j >= 0 and y + i < self.height and x + j < self.width and not (i == 0 and j == 0):
                    if not self.cells[x+j][y+i]["player"] == player:
                        self.move_cells[y + i][x + j] = True

    def is_queen_move(self, player, x, y):
        if player == "CPU":
            reverse_player = "USER"

        elif player == "USER":
            reverse_player = "CPU"

        for i in range(8):
            for j in range(8):
                if i == 0 and not j == 0 and y - j >= 0 and x - j >= 0 and y - j < self.height and x - j < self.width:
                    if self.cells[x - j][y - j]["player"] == player:
                        break
                    elif self.cells[x - j][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x - j] = True
                        break
                    elif not (y - j == y and x - j == x) and not self.cells[x - j][y - j]["player"] == player:
                        self.move_cells[y - j][x - j] = True
                elif i == 1 and not j == 0 and y - j >= 0 and x + j >= 0 and y - j < self.height and x + j < self.width:
                    if self.cells[x + j][y - j]["player"] == player:
                        break
                    elif self.cells[x + j][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x + j] = True
                        break
                    elif not (y - j == y and x + j == x) and not self.cells[x + j][y - j]["player"] == player:
                        self.move_cells[y - j][x + j] = True
                elif i == 2 and not j == 0 and y + j >= 0 and x - j >= 0 and y + j < self.height and x - j < self.width:
                    if self.cells[x - j][y + j]["player"] == player:
                        break
                    elif self.cells[x - j][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x - j] = True
                        break
                    elif not (y + j == y and x - j == x) and not self.cells[x - j][y + j]["player"] == player:
                        self.move_cells[y + j][x - j] = True
                elif i == 3 and not j == 0 and y + j >= 0 and x + j >= 0 and y + j < self.height and x + j < self.width:
                    if self.cells[x + j][y + j]["player"] == player:
                        break
                    elif self.cells[x + j][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x + j] = True
                        break
                    elif not (y + j == y and x + j == x) and not self.cells[x + j][y + j]["player"] == player:
                        self.move_cells[y + j][x + j] = True
                elif i == 4 and not j == 0 and (y - j) >= 0 and (y - j) < self.height:
                    if self.cells[x][y - j]["player"] == player:
                        break
                    elif self.cells[x][y - j]["player"] == reverse_player:
                        self.move_cells[y - j][x] = True
                        break
                    elif not (y - j == y) and not self.cells[x][y - j]["player"] == player:
                        self.move_cells[y - j][x] = True
                elif i == 5 and not j == 0 and (y + j) >= 0 and (y + j) < self.height:
                    if self.cells[x][y + j]["player"] == player:
                        break
                    elif self.cells[x][y + j]["player"] == reverse_player:
                        self.move_cells[y + j][x] = True
                        break
                    elif not (y + j == y) and not self.cells[x][y + j]["player"] == player:
                        self.move_cells[y + j][x] = True
                elif i == 6 and not j == 0 and (x - j) >= 0 and (x - j) < self.width:
                    if self.cells[x - j][y]["player"] == player:
                        break
                    elif self.cells[x - j][y]["player"] == reverse_player:
                        self.move_cells[y][x - j] = True
                        break
                    elif not (x - j == x) and not self.cells[x - j][y]["player"] == player:
                        self.move_cells[y][x - j] = True
                elif i == 7 and not j == 0 and (x + j) >= 0 and (x + j) < self.width:
                    if self.cells[x + j][y]["player"] == player:
                        break
                    elif self.cells[x + j][y]["player"] == reverse_player:
                        self.move_cells[y][x + j] = True
                        break
                    elif not (x + j == x) and not self.cells[x + j][y]["player"] == player:
                        self.move_cells[y][x + j] = True
                else:
                    continue

    def is_move(self, event, arg):

        y = arg["y"]
        x = arg["x"]

        player = self.cells[x][y]["player"]

        if any(self.cells[x][y]):
            name = self.cells[x][y]["chess_piece"]
        else:
            name = None

        if self.move_cells[y][x]:
            name = self.cells[self.save_cell["x"]
                              ][self.save_cell["y"]]["chess_piece"]
            self.move(name, y, x)

        else:
            self.init_move_cells()

            if name == "PAWN":
                self.is_pawn_move(player, x, y)

            elif name == "ROOK":
                self.is_rook_move(player, x, y)

            elif name == "KNIGHT":
                self.is_knight_move(player, x, y)

            elif name == "BISHOP":
                self.is_bishop_move(player, x, y)

            elif name == "KING":
                self.is_king_move(player, x, y)

            elif name == "QUEEN":
                self.is_queen_move(player, x, y)

            for i in range(self.height):
                for j in range(self.width):
                    if self.move_cells[i][j]:
                        label = self.labels[j][i]
                        label.config(
                            bg="red"
                        )
                    else:
                        label = self.labels[j][i]
                        label.config(
                            bg="white"
                        )
            self.save_cell = {
                "y": y,
                "x": x
            }

            self.test_cells()
            self.test_move_cells()
            self.test_player_cells()

    def move(self, name, y, x):

        label = self.labels[x][y]
        piece_name = self.cells[self.save_cell["x"]
                                ][self.save_cell["y"]]["chess_piece"]
        player = self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"]

        if name == "PAWN":
            if self.is_game_end(piece_name, player, x, y):
                self.game_end()
            else:
                self.pawn_move(player, y, x)

        elif name == "ROOK":
            self.rook_move(player, y, x)

        elif name == "KNIGHT":
            self.knight_move(player, y, x)

        elif name == "BISHOP":
            self.bishop_move(player, y, x)

        elif name == "KING":
            self.king_move(player, y, x)

        elif name == "QUEEN":
            self.queen_move(player, y, x)

        self.init_move_cells()

        for i in range(self.height):
            for j in range(self.width):
                if self.move_cells[i][j]:
                    label = self.labels[j][i]
                    label.config(
                        bg="red"
                    )
                else:
                    label = self.labels[j][i]
                    label.config(
                        bg="white"
                    )

    def pawn_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "PAWN"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="PAWN"
        )

    def rook_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "ROOK"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="ROOK"
        )

    def knight_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "KNIGHT"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="KNIGHT"
        )

    def bishop_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "BISHOP"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="BISHOP"
        )

    def king_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "KING"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="KING"
        )

    def queen_move(self, player, y, x):
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["chess_piece"] = ""
        self.cells[self.save_cell["x"]
                   ][self.save_cell["y"]]["player"] = ""
        self.cells[x][y]["player"] = player
        self.cells[x][y]["chess_piece"] = "QUEEN"
        self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
            text=""
        )
        self.labels[x][y].config(
            text="QUEEN"
        )

    def cant_move_alert(self):
        messagebox.showinfo(
            "そこに動くことはできません。"
        )

    # ウィジェットを作成

    def create_widgets(self):
        # ラベルウィジェット管理用のリストを作成
        self.labels = [[None] * self.width for j in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):

                if (i == 1):
                    label = tk.Label(
                        self.app,
                        text='PAWN',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 0 and j == 0) or (i == 0 and j == 7):
                    label = tk.Label(
                        self.app,
                        text='ROOK',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 0 and j == 1) or (i == 0 and j == 6):
                    label = tk.Label(
                        self.app,
                        text='KNIGHT',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 0 and j == 2) or (i == 0 and j == 5):
                    label = tk.Label(
                        self.app,
                        text='BISHOP',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 0 and j == 3):
                    label = tk.Label(
                        self.app,
                        text='KING',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 0 and j == 4):
                    label = tk.Label(
                        self.app,
                        text='QUEEN',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                # USERのコマ配置
                elif (i == 6):
                    label = tk.Label(
                        self.app,
                        text='PAWN',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 7 and j == 0) or (i == 7 and j == 7):
                    label = tk.Label(
                        self.app,
                        text='ROOK',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 7 and j == 1) or (i == 7 and j == 6):
                    label = tk.Label(
                        self.app,
                        text='KNIGHT',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 7 and j == 2) or (i == 7 and j == 5):
                    label = tk.Label(
                        self.app,
                        text='BISHOP',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 7 and j == 3):
                    label = tk.Label(
                        self.app,
                        text='KING',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                elif (i == 7 and j == 4):
                    label = tk.Label(
                        self.app,
                        text='QUEEN',
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                else:
                    # まずはテキストなしでラベルを作成
                    label = tk.Label(
                        self.app,
                        width=10,
                        height=6,
                        relief=tk.RAISED
                    )
                # ラベルを配置
                label.grid(column=j, row=i)

                # その座標のラベルのインスタンスを覚えておく
                self.labels[i][j] = label

    def set_events(self):

        # 全ラベルに対してイベントを設定
        for i in range(self.height):
            for j in range(self.width):

                label = self.labels[j][i]
                data = {"y": i, "x": j}

                # 左クリック時のイベント設定
                label.bind("<ButtonPress-1>", lambda event,
                           arg=data: self.is_move(event, arg))

                # 右クリック時のイベント設定
                # label.bind("<ButtonPress-2>", self.raise_flag)

    def is_game_end(self, piece, player, x, y):
        if piece == "KING" and not player == self.cells[x][y]["player"]:
            return True
        return False

    def game_end(self):
        messagebox.showinfo(
            "あなたの勝ちです"
        )
        self.result()

    def result(self):
        print("a")

    ################################################################################

    ###################
    ## debug_methods ##
    ##################
    # cellsの中身を確認する

    def test_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                if any(self.cells[i][j]):
                    print(self.cells[i][j]["chess_piece"], end=' ')
                else:
                    print("", end=' ')
            print()

    def test_move_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.move_cells[i][j], end=' ')
            print()

    def test_player_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                if any(self.cells[i][j]):
                    print(self.cells[i][j]["player"], end=' ')
                else:
                    print("", end=' ')
            print()


# プログラムの開始
app = tk.Tk()
app.title("Chess")
game = Chess(app)
app.mainloop()
