
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

        self.height = HEIGHT
        self.width = WIDTH

        self.player = None

        self.user_name = None
        self.cpu_name = None

        self.turn = None
        self.now_turn = FIRST

        self.init_cells()

        self.placement_chara()

        # debug呼び出し
        # cellsの中身の確認
        self.test_cells()

    # cellsの初期化
    def init_cells(self):
        self.cells = [["" for i in range(self.width)]
                      for j in range(self.height)]

    # 先行後攻選択
    def select_turn(self):
        # 先行を押した時の処理
        if self.turn == FIRST:
            self.player = CPU
        # 後攻を押した時の処理
        elif self.turn == SECOND:
            self.player = USER

    # キャラクターの配置

    def placement_chara(self):
        for i in range(self.width):
            for j in range(self.height):
                # CPUのコマ配置
                if (i == 1):
                    self.cells[i][j] = "CPU_PAWN"
                elif (i == 7 and j == 0) or (i == 7 and j == 7):
                    self.cells[i][j] = "CPU_ROOK"
                elif (i == 7 and j == 1) or (i == 7 and j == 6):
                    self.cells[i][j] = "CPU_KNIGHT"
                elif (i == 7 and j == 2) or (i == 7 and j == 5):
                    self.cells[i][j] = "CPU_BISHOP"
                elif (i == 7 and j == 3):
                    self.cells[i][j] = "CPU_KING"
                elif (i == 7 and j == 4):
                    self.cells[i][j] = "CPU_QUEEN"
                # USERのコマ配置
                if (i == 6):
                    self.cells[i][j] = "USER_PAWN"
                elif (i == 0 and j == 0) or (i == 0 and j == 7):
                    self.cells[i][j] = "USER_ROOK"
                elif (i == 0 and j == 1) or (i == 0 and j == 6):
                    self.cells[i][j] = "USER_KNIGHT"
                elif (i == 0 and j == 2) or (i == 0 and j == 5):
                    self.cells[i][j] = "USER_BISHOP"
                elif (i == 0 and j == 3):
                    self.cells[i][j] = "USER_KING"
                elif (i == 0 and j == 4):
                    self.cells[i][j] = "USER_QUEEN"

    #　動けるか確認する関数
    # i,jが古い座標、x、yが新しい座標（動きたい座標）
    def is_move(self, i, j, y, x):
        if y >= 0 and x >= 0 and y < self.height and x < self.width:
            if self.player == CPU:
                if self.cells[y][x] == "" or self.cells[y][x] == "USER_PAWN":
                    self.pown_move(i, j, y, x)
                else:
                    self.cant_move_alert()
            elif self.player == USER:
                if self.cells[y][x] == "" or self.cells[y][x] == "CPU_PAWN":
                    self.pown_move(i, j, y, x)
                else:
                    self.cant_move_alert()
        else:
            self.cant_move_alert()

    # ポーンの動き
    def pown_move(self, i, j, y, x):
        self.cells[y][x] = self.cells[i][j]
        self.cells[i][j] = ""

    #

    #

    #
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
                print(self.cells[i][j], end=' ')
                print()


# プログラムの開始
app = tk.Tk()
game = Chess(app)
app.mainloop()
