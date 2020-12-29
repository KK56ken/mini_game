
import os
import tkinter as tk
from tkinter import messagebox

# マップの広さ
HEIGHT = 8
WIDTH = 8
# 先行、後攻のターン
FIRST = 0
SECOND = 1


class Chess():
    def __init__(self, app):
        self.app = app
        self.cells = None
        self.height = HEIGHT
        self.width = WIDTH

        self.turn = FIRST

        self.init_cells()

        self.placement_chara()

        # debug呼び出し
        # cellsの中身の確認
        self.test_cells()

    #　cellsの初期化
    def init_cells(self):
        self.cells = [["" for i in range(self.height)]
                      for j in range(self.width)]

    #　キャラクターの配置
    def placement_chara(self):
        for i in range(self.height):
            for j in range(self.width):
                if (i == 1 or i == 6):
                    self.cells[i][j] = "PAWN"
                elif (i == 0 and j == 0) or (i == 0 and j == 7) or (i == 7 and j == 0) or (i == 7 and j == 7):
                    self.cells[i][j] = "ROOK"
                elif (i == 0 and j == 1) or (i == 0 and j == 6) or (i == 7 and j == 1) or (i == 7 and j == 6):
                    self.cells[i][j] = "KNIGHT"
                elif (i == 0 and j == 2) or (i == 0 and j == 5) or (i == 7 and j == 2) or (i == 7 and j == 5):
                    self.cells[i][j] = "BISHOP"
                elif (i == 0 and j == 3) or (i == 7 and j == 3):
                    self.cells[i][j] = "KING"
                elif (i == 0 and j == 4) or (i == 7 and j == 4):
                    self.cells[i][j] = "QUEEN"

    #　動けるか確認する関数
    # i,jが古い座標、x、yが新しい座標（動きたい座標）
    def is_move(self, name, i, j, y, x):
        if name == "PAWN":
            if j >= 0 and i >= 0 and j < self.height and i < self.width:
                if self.cells[y][x] == "":
                    self.pown_move(i, j, y, x)
                else:
                    self.not_move_alert()

    # ポーンの動き
    def pown_move(self, i, j, y, x):
        self.cells[y][x] = self.cells[i][j]
        self.cells[i][j] = ""

    #

    #

    #
    def not_move_alert(self):
        messagebox.showinfo(
            "そこに動くことはできません。"
        )

    ################################################################################

    ###################
    ## debug_methods ##
    ##################
    # cellsの中身を確認する
    def test_cells(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.cells[i][j], end=' ')
                print()


# プログラムの開始
app = tk.Tk()
game = Chess(app)
app.mainloop()
