
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

        self.save_cell = None

        self.height = HEIGHT
        self.width = WIDTH

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

    def is_move(self, event, arg):

        y = arg["y"]
        x = arg["x"]
        print(y, x)
        print(self.move_cells[y][x])

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
                if self.cells[x][y]["player"] == "CPU":
                    if (x + 1) >= 0 and (x + 1) < self.height:
                        if x == 1:
                            self.move_cells[y][x + 1] = True
                            self.move_cells[y][x + 2] = True
                        else:
                            self.move_cells[y][x + 1] = True

                elif self.cells[x][y]["player"] == "USER":
                    if (x - 1) >= 0 and (x - 1) < self.height:
                        if x == 6:
                            self.move_cells[y][x - 1] = True
                            self.move_cells[y][x - 2] = True
                        else:
                            self.move_cells[y][x - 1] = True

            elif name == "ROOK":
                for i in range(4):
                    for j in range(8):
                        if i == 0 and (y - j) >= 0 and (y - j) < self.height:
                            if not (y - j == y):
                                self.move_cells[y - j][x] = True
                        elif i == 1 and (y + j) >= 0 and (y + j) < self.height:
                            if not (y + j == y):
                                self.move_cells[y + j][x] = True
                        elif i == 2 and (x - j) >= 0 and (x - j) < self.height:
                            if not (x - j == x):
                                self.move_cells[y][x - j] = True
                        elif i == 3 and (x + j) >= 0 and (x + j) < self.height:
                            if not (x + j == x):
                                self.move_cells[y][x + j] = True
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
                        if i == 0 and y - j >= 0 and x - j >= 0 and y - j < self.height and x - j < self.width:
                            if not (y - j == y and x - j == x):
                                self.move_cells[y - j][x - j] = True
                        elif i == 1 and y - j >= 0 and x + j >= 0 and y - j < self.height and x + j < self.width:
                            if not (y - j == y and x + j == x):
                                self.move_cells[y - j][x + j] = True
                        elif i == 2 and y + j >= 0 and x - j >= 0 and y + j < self.height and x - j < self.width:
                            if not (y + j == y and x - j == x):
                                self.move_cells[y + j][x - j] = True
                        elif i == 3 and y + j >= 0 and x + j >= 0 and y + j < self.height and x + j < self.width:
                            if not (y + j == y and x + j == x):
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
                        if i == 0 and y - j >= 0 and x - j >= 0 and y - j < self.height and x - j < self.width:
                            if not (y - j == y and x - j == x):
                                self.move_cells[y - j][x - j] = True
                        elif i == 1 and y - j >= 0 and x + j >= 0 and y - j < self.height and x + j < self.width:
                            if not (y - j == y and x + j == x):
                                self.move_cells[y - j][x + j] = True
                        elif i == 2 and y + j >= 0 and x - j >= 0 and y + j < self.height and x - j < self.width:
                            if not (y + j == y and x - j == x):
                                self.move_cells[y + j][x - j] = True
                        elif i == 3 and y + j >= 0 and x + j >= 0 and y + j < self.height and x + j < self.width:
                            if not (y + j == y and x + j == x):
                                self.move_cells[y + j][x + j] = True
                        elif i == 4 and (y - j) >= 0 and (y - j) < self.height:
                            if not (y - j == y):
                                self.move_cells[y - j][x] = True
                        elif i == 5 and (y + j) >= 0 and (y + j) < self.height:
                            if not (y + j == y):
                                self.move_cells[y + j][x] = True
                        elif i == 6 and (x - j) >= 0 and (x - j) < self.width:
                            if not (x - j == x):
                                self.move_cells[y][x - j] = True
                        elif i == 7 and (x + j) >= 0 and (x + j) < self.width:
                            if not (x + j == x):
                                self.move_cells[y][x + j] = True
                        else:
                            continue

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

            # if self.save_cell["y"] == y and self.save_cell["x"] == x:
            #     label = self.labels[j][i]
            #     label.config(
            #         bg="white"
            #     )
            self.test_cells()
            self.test_move_cells()

    def move(self, name, y, x):

        label = self.labels[x][y]

        print(name)

        if name == "PAWN":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "PAWN"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="PAWN"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "PAWN"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="PAWN"
                )
        elif name == "ROOK":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "ROOK"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="ROOK"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "ROOK"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="ROOK"
                )
        elif name == "KNIGHT":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "KNIGHT"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="KNIGHT"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "KNIGHT"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="KNIGHT"
                )
        elif name == "BISHOP":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "BISHOP"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="BISHOP"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "BISHOP"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="BISHOP"
                )

        elif name == "KING":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "KING"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="KING"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "KING"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="KING"
                )
        elif name == "QUEEN":
            print("1")
            if self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "CPU":
                print("2")
                # if not any(self.cells[y][x]) or self.cells[x][y]["player"] == "USER":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "CPU"
                self.cells[x][y]["chess_piece"] = "QUEEN"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="QUEEN"
                )

            elif self.cells[self.save_cell["x"]][self.save_cell["y"]]["player"] == "USER":
                print("3")
                # if not any(self.cells[y][x]) or self.cells[y][x]["player"] == "CPU":
                self.cells[self.save_cell["x"]
                           ][self.save_cell["y"]]["chess_piece"] = "NONE"
                self.cells[x][y]["player"] = "USER"
                self.cells[x][y]["chess_piece"] = "QUEEN"
                self.labels[self.save_cell["x"]][self.save_cell["y"]].config(
                    text=""
                )
                label.config(
                    text="QUEEN"
                )

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
                    print("NONE", end=' ')
            print()

    def test_move_cells(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.move_cells[i][j], end=' ')
            print()


# プログラムの開始
app = tk.Tk()
game = Chess(app)
app.mainloop()
