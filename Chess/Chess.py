
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

        self.cells = None
        self.move_cells = None

        self.height = HEIGHT
        self.width = WIDTH

        self.player = None

        self.user_name = None
        self.cpu_name = None

        self.turn = None
        self.now_turn = FIRST

        self.init_cells()

        self.placement_piece()

        # debug呼び出し
        # cellsの中身の確認
        self.test_cells()

    # cellsの初期化
    def init_cells(self):
        self.cells = [[dict() for i in range(self.width)]
                      for j in range(self.height)]
    # 移動できる場所を保持する配列の初期化

    def init_move_cells(self):
        self.move_cells = [[False for i in range(self.width)]
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
                if (i == 6):
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

    def is_move(self, name, y, x):
        self.init_move_cells()
        if name == "PAWN":
            if self.cells[y][x] == "CPU_PAWN":
                if (y + 1) >= 0 and (y + 1) < self.height:
                    # 今の状態だと移動先に何があっても移動できる
                    self.move_cells[y + 1][x] = True

            elif self.cells[y][x] == "USER_PAWN":
                if (y - 1) >= 0 and (y - 1) < self.height:
                    self.move_cells[y - 1][x] = True

        elif name == "ROOK":
            for i in range(4):
                for j in range(8):
                    if i == 0 and (y-j) >= 0 and (y-j) < self.height:
                        self.move_cells[y - j][x] = True
                    elif i == 1 and (y+j) >= 0 and (y+j) < self.height:
                        self.move_cells[y + j][x] = True
                    elif i == 2 and (x-j) >= 0 and (x-j) < self.height:
                        self.move_cells[y][x - j] = True
                    elif i == 3 and (x+j) >= 0 and (x+j) < self.height:
                        self.move_cells[y][x - j] = True
                    else:
                        continue

        elif name == "KNIGHT":
            if y - 2 >= 0 and x - 1 >= 0 and y - 2 < self.height and x - 1 < self.width:
                self.move_cells[y - 2][x - 1] = True

            if y - 1 >= 0 and x - 2 >= 0 and y - 1 < self.height and x - 2 < self.width:
                self.move_cells[y - 1][x - 2] = True

            if y - 2 >= 0 and x + 1 >= 0 and y - 2 < self.height and x + 1 < self.width:
                self.move_cells[y - 2][x + 1] = True

            if y - 1 >= 0 and x + 2 >= 0 and y - 1 < self.height and x + 2 < self.width:
                self.move_cells[y - 1][x + 2] = True

            if y + 1 >= 0 and x - 2 >= 0 and y + 1 < self.height and x - 2 < self.width:
                self.move_cells[y + 1][x - 2] = True

            if y + 2 >= 0 and x - 1 >= 0 and y + 2 < self.height and x - 1 < self.width:
                self.move_cells[y + 2][x - 1] = True

            if y + 1 >= 0 and x + 2 >= 0 and y + 1 < self.height and x + 2 < self.width:
                self.move_cells[y + 1][x + 2] = True

            if y + 2 >= 0 and x + 1 >= 0 and y + 2 < self.height and x + 1 < self.width:
                self.move_cells[y + 2][x + 1] = True

        elif name == "BISHOP":
            for i in range(4):
                for j in range(8):
                    if i == 0 and y-j >= 0 and x-j >= 0 and y-j < self.height and x-j < self.width:
                        self.move_cells[y - j][x - j] = True
                    elif i == 1 and y-j >= 0 and x+j >= 0 and y-j < self.height and x+j < self.width:
                        self.move_cells[y - j][x + j] = True
                    elif i == 2 and y+j >= 0 and x-j >= 0 and y+j < self.height and x-j < self.width:
                        self.move_cells[y + j][x - j] = True
                    elif i == 3 and y+j >= 0 and x+j >= 0 and y+j < self.height and x+j < self.width:
                        self.move_cells[y + j][x + j] = True
                    else:
                        continue

        elif name == "KING":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if y+i >= 0 and x+j >= 0 and y+i < self.height and x+j < self.width and not(i == 0 and j == 0):
                        self.move_cells[y+i][x+j] = True

        elif name == "QUEEN":
            for i in range(8):
                for j in range(8):
                    if i == 0 and y-j >= 0 and x-j >= 0 and y-j < self.height and x-j < self.width:
                        self.move_cells[y - j][x - j] = True
                    elif i == 1 and y-j >= 0 and x+j >= 0 and y-j < self.height and x+j < self.width:
                        self.move_cells[y - j][x + j] = True
                    elif i == 2 and y+j >= 0 and x-j >= 0 and y+j < self.height and x-j < self.width:
                        self.move_cells[y + j][x - j] = True
                    elif i == 3 and y+j >= 0 and x+j >= 0 and y+j < self.height and x+j < self.width:
                        self.move_cells[y + j][x + j] = True
                    elif i == 4 and (y-j) >= 0 and (y-j) < self.height:
                        self.move_cells[y - j][x] = True
                    elif i == 5 and (y+j) >= 0 and (y+j) < self.height:
                        self.move_cells[y + j][x] = True
                    elif i == 6 and (x-j) >= 0 and (x-j) < self.width:
                        self.move_cells[y][x - j] = True
                    elif i == 7 and (x+j) >= 0 and (x+j) < self.width:
                        self.move_cells[y][x - j] = True
                    else:
                        continue


    def pown_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_PAWN":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_PAWN":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()

    # ルークの動き
    def rook_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_ROOK":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_ROOK":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
    # ナイトの動き

    def knight_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_KNIGHT":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_NIGHT":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()

    # ビショップの動き

    def bishop_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_BISHOP":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_BISHOP":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()

    # キングの動き
    def king_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_KING":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_KING":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()

    # クイーンの動き

    def queen_move(self, cell, y, x):
        if self.player == CPU:
            if self.cells[y][x] == "" or self.cells[y][x] == "USER_KING":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()
        elif self.player == USER:
            if self.cells[y][x] == "" or self.cells[y][x] == "CPU_KING":
                self.cells[y][x] = cell
            else:
                self.cant_move_alert()

    def cant_move_alert(self):
        messagebox.showinfo(
            "そこに動くことはできません。"
        )

    ################################################################################

    ###################
    ## debug_methods ##
    ##################
    # cellsの中身を確認する
    def test_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                if any(self.cells[i][j]):
                    print(self.cells[i][j]["player"], end=' ')
                else:
                    print("NONE", end=' ')
            print()


# プログラムの開始
app = tk.Tk()
game = Chess(app)
app.mainloop()
