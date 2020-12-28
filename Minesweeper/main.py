#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk

BOARD_WIDTH = 5
BOARD_HEIGHT = 5
MINE_NUM = 2
MINE_BG_COLOR = "pink"
FLAG_BG_COLOR = "gold"
EMPTY_BG_COLOR = "lightgray"

fg_color = {
    1: "blue",
    2: "green",
    3: "purple",
    4: "olive",
    5: "chocolate",
    6: "magenta",
    7: "darkorange",
    8: "red",
}

MINE = -1


class MineSweeper():
    def __init__(self, app):
        self.app = app
        self.cells = None
        self.labels = None
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.mine_num = MINE_NUM
        self.clear_num = self.width * self.height - self.mine_num
        self.open_num = 0
        self.open_mine = False
        self.play_game = False

        self.init_cells()

        # ウィジェットの作成と配置
        self.create_widgets()

        # イベントの設定
        self.set_events()

        # 最後にゲーム中フラグをTrueに設定
        self.play_game = True

     # ボードの初期化
    def init_cells(self):
        # ボードのサイズ分の２次元リストを作成
        self.cells = [[0] * self.width for _ in range(self.height)]

    def create_widgets(self):
        self.labels = [[None] * self.width for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                label = tk.Label(width=2, height=1, relief=tk.RAISED)
                label.grid(column=i, row=j)

                self.labels[i][j] = label

    def set_events(self):
        for j in range(self.height):
            for i in range(self.width):
                label = self.labels[j][i]

                label.bind("<ButtonPress-1>", self.open_cell)

                label.bind("<ButtonPress-2>", self.raise_flag)

    def open_cell(self, event):
        # ゲーム中でなければ何もしない
        if not self.play_game:
            return
        label = event.widget

        for y in range(self.height):
            for x in range(self.width):
                if self.labels[y][x] == label:
                    j = y
                    i = x
        cell = self.cells[j][i]

        if label.cget("relief") != tk.RAISED:
            return
        text, bg, fg = self.get_text_info(cell)

        # そこに地雷がある場合
        if cell == MINE:
            # ゲームオーバーフラグをTrueに設定
            self.open_mine = True

        # ラベルの設定変更
        label.config(
            text=text,
            bg=bg,
            fg=fg,
            relief=tk.SUNKEN
        )

    def raise_flag(self, event):
        # ゲーム中でなければ何もしない
        if not self.play_game:
            return
        label = event.widget
        if label.cget("relief") != tk.RAISED:
            return

        if label.cget("text") != "F":
            # ラベルの色を設定
            bg = FLAG_BG_COLOR

            # そのラベル上に旗(F)を立てる
            label.config(
                text="F",
                bg=bg
            )
        else:
            # ラベルの色を設定
            bg = EMPTY_BG_COLOR

            # そのラベル上の旗(F)を取り除く
            label.config(
                text="",
                bg=bg

            )

    # テキストと文字と背景色を取得する関数
    def get_text_info(self, num):

        # 指定された数字を表示する色を決定
        if num == MINE:
            text = "X"
            bg = MINE_BG_COLOR
            fg = "darkred"
        elif num == 0:
            text = ""
            bg = EMPTY_BG_COLOR
            fg = "black"
        else:
            text = str(num)
            bg = EMPTY_BG_COLOR
            fg = fg_color[num]

        return (text, bg, fg)


app = tk.Tk()
app.title("Minesweeper")

game = MineSweeper(app)
app.mainloop()
