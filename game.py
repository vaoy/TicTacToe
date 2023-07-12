import tkinter
from tkinter import Frame, Label, Radiobutton, Entry, Button, DISABLED, END, NORMAL, Canvas

MAIN_WIN_WIDTH = 320
MAIN_WIN_HEIGHT = 300
BG_COLOR = "cyan"
ENTRY_COLOR = "white"
HEADER_FONT = "Times"
NAME_LABEL_FONT = "Verdana"
BLANK_FONT = "Arial"
NORMAL_WEIGHT = "normal"
BOLD_WEIGHT = "bold"
UNDERLINE_WEIGHT = "underline"
TITLE = "Tic Tac Toe"
HEADING_WRITING = "Settings"
HEADING_SIZE = 25
RB1_WRITING = "Single Player"
RB2_WRITING = "Multi Player"
RB3_WRITING = "Easy"
RB4_WRITING = "Medium"
RB5_WRITING = "Hard"
LABEL1_WRITING = "P1 NAME"
LABEL2_WRITING = "P2 NAME"
LABEL_SIZE = 7
START_BUTTON = "Start"
BLANK = " "
BLANK1_SIZE = 3
BLANK2_SIZE = 10
CELL_WIDTH = 60
CELL_X_OFFSET = MAIN_WIN_WIDTH/4-10
CELL_Y_OFFSET = MAIN_WIN_HEIGHT/4
NUM_OF_CELLS = 9
SHAPE_X = "x"
SHAPE_O = "o"
SHAPE_OFFSET = CELL_WIDTH/4
SHAPE_WIDTH = 3
GAME_IN_PROGRESS = "Game In Progress"
GAME_OVER = "Game Over"
BLACK_FILL = "black"
GAME_OVER_FONT = "Helvetica 35 bold"
PLAYER_WINS_FONT = "Verdana 20"
X_FOR_MANY_THINGS = 160
GAME_OVER_AND_PLAYERS_Y = 22
PLAYER_WINS_Y = 60
WIN_MSG = " Wins"
TIE_MSG = "Tie Game"
PLAYER_FONT = "Helvetica 20 bold"
ERASING_RECTANGLE_X1_AND_Y1 = 0
ERASING_RECTANGLE_X2 = 320
ERASING_RECTANGLE_Y2 = 60
COMP = "CPU"
VS = " v.s. "
LEFT_CLICK_EVENT = '<Button-1>'
WIN_LINE_COLOR = "yellow"
X_COLOR = "red"
O_COLOR = "blue"
INVALID_NAME_MSG_FONT = "Helvetica, 5"
INVALID_NAME_MSG = "Please enter a name"
DEFAULT_FONT = "Arial, 8"
ERR_COLOR = "red"
NORMAL_COLOR = "black"

class UI:
    def __init__(self):
        self.board = Board()
        '''Main Window'''
        self.main_win = tkinter.Tk()
        self.main_win.geometry(str(MAIN_WIN_WIDTH) + "x" + str(MAIN_WIN_HEIGHT))
        self.main_win.config(bg = BG_COLOR)
        self.main_win.title(TITLE)
        '''Settings Frame'''
        self.settings = Frame(self.main_win, width = MAIN_WIN_WIDTH, height = MAIN_WIN_HEIGHT, bg = BG_COLOR)
        heading = Label(self.settings, text = HEADING_WRITING, font = (ENTRY_COLOR, HEADING_SIZE, BOLD_WEIGHT, UNDERLINE_WEIGHT), bg = BG_COLOR)
        blank1 = Label(self.settings, text = BLANK, font = (BLANK_FONT, BLANK1_SIZE), bg = BG_COLOR)
        self.num_of_players = tkinter.IntVar()
        self.rb1 = Radiobutton(self.settings, text = RB1_WRITING, variable = self.num_of_players, value = 1, bg = BG_COLOR, command = self.player_selection)
        self.rb2 = Radiobutton(self.settings, text = RB2_WRITING, variable = self.num_of_players, value = 2, bg = BG_COLOR, command = self.player_selection)
        name1_label = Label(self.settings, text = LABEL1_WRITING, font = (NAME_LABEL_FONT, LABEL_SIZE, NORMAL_WEIGHT), bg = BG_COLOR)
        name2_label = Label(self.settings, text = LABEL2_WRITING, font = (NAME_LABEL_FONT, LABEL_SIZE, NORMAL_WEIGHT), bg = BG_COLOR)
        self.name1 = Entry(self.settings, bg = ENTRY_COLOR)
        self.name2 = Entry(self.settings, bg = ENTRY_COLOR)
        self.cpu_level = tkinter.IntVar()
        self.rb3 = Radiobutton(self.settings, text = RB3_WRITING, variable = self.cpu_level, value = 1, bg = BG_COLOR)
        self.rb4 = Radiobutton(self.settings, text = RB4_WRITING, variable = self.cpu_level, value = 2, bg = BG_COLOR)
        self.rb5 = Radiobutton(self.settings, text = RB5_WRITING, variable = self.cpu_level, value = 3, bg = BG_COLOR)
        blank2 = Label(self.settings, text = BLANK, font = (BLANK_FONT, BLANK2_SIZE), bg = BG_COLOR)
        self.start_button = Button(self.settings, text = START_BUTTON, bg = BG_COLOR, command = self.run_game)
        heading.pack()
        blank1.pack()
        self.rb1.pack()
        self.rb2.pack()
        name1_label.pack()
        self.name1.pack()
        name2_label.pack()
        self.name2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        blank2.pack()
        self.start_button.pack()
        self.settings.pack()
        '''Game Frame'''
        self.game = Frame(self.main_win, width = MAIN_WIN_WIDTH, height = MAIN_WIN_HEIGHT, bg = BG_COLOR)
        self.game_canvas = Canvas(self.game, width = MAIN_WIN_WIDTH, height = MAIN_WIN_HEIGHT, bg = BG_COLOR)
        self.game_canvas.bind(LEFT_CLICK_EVENT,self.on_press)

        self.curr_player_index = 0 
        self.cell_list = []
        x = 0
        y = 0
        for i in range(NUM_OF_CELLS):
            if i % 3 == 0 and i != 0:
                x = 0
                y = y + 1
            p1 = Point(int(x*CELL_WIDTH+CELL_X_OFFSET), int(y*CELL_WIDTH+CELL_Y_OFFSET))
            p2 = Point(int((x+1)*CELL_WIDTH+CELL_X_OFFSET), int((y+1)*CELL_WIDTH+CELL_Y_OFFSET))
            cell = Cell(p1, p2)
            self.cell_list.append(cell)
            x = x + 1
        self.game_state = GAME_IN_PROGRESS
        self.draw_board()

    def on_press(self, event):
        if self.game_state != GAME_OVER and not (isinstance(self.players[self.curr_player_index], CPU_Easy) or isinstance(self.players[self.curr_player_index], CPU_Medium) or isinstance(self.players[self.curr_player_index], CPU_Hard)):
            for j in range(9):
                if event.x < self.cell_list[j].point_bottomright.x and event.x > self.cell_list[j].point_topleft.x and event.y < self.cell_list[j].point_bottomright.y and event.y > self.cell_list[j].point_topleft.y and self.board.get(j)==None:
                    self.board.insert(j, self.players[self.curr_player_index].shape)
                    self.curr_player_index = 1 - self.curr_player_index
            self.draw_board()
            self.check_win()
        if self.game_state != GAME_OVER and (isinstance(self.players[self.curr_player_index], CPU_Easy) or isinstance(self.players[self.curr_player_index], CPU_Medium) or isinstance(self.players[self.curr_player_index], CPU_Hard)):
            self.players[self.curr_player_index].move(self.board)
            self.curr_player_index = 1 - self.curr_player_index
            self.draw_board()
            self.check_win()
            
    def check_win(self):
        for i in range(3):
            if self.board.get(i*3) != None and self.board.get(i*3) == self.board.get(i*3+1) and self.board.get(i*3) == self.board.get(i*3+2):
                self.draw_win_line(self.cell_list[i*3].point_topleft.x, (self.cell_list[i*3].point_topleft.y + self.cell_list[i*3].point_bottomright.y)/2, self.cell_list[i*3+2].point_bottomright.x, (self.cell_list[i*3+2].point_topleft.y + self.cell_list[i*3+2].point_bottomright.y)/2)
                self.game_state = GAME_OVER
        for i in range(3):
            if self.board.get(i) != None and self.board.get(i) == self.board.get(i+3) and self.board.get(i) == self.board.get(i+6):
                self.draw_win_line((self.cell_list[i].point_topleft.x + self.cell_list[i].point_bottomright.x)/2, self.cell_list[i].point_topleft.y, (self.cell_list[i+6].point_topleft.x + self.cell_list[i+6].point_bottomright.x)/2, self.cell_list[i+6].point_bottomright.y)
                self.game_state = GAME_OVER
        if self.board.get(0) != None and self.board.get(0) == self.board.get(4) and self.board.get(0) == self.board.get(8):
            self.draw_win_line(self.cell_list[0].point_topleft.x, self.cell_list[0].point_topleft.y, self.cell_list[8].point_bottomright.x, self.cell_list[8].point_bottomright.y)
            self.game_state = GAME_OVER
        if self.board.get(2) != None and self.board.get(2) == self.board.get(4) and self.board.get(2) == self.board.get(6):
            self.draw_win_line(self.cell_list[2].point_bottomright.x, self.cell_list[2].point_topleft.y, self.cell_list[6].point_topleft.x, self.cell_list[6].point_bottomright.y)
            self.game_state = GAME_OVER
        if self.game_state == GAME_OVER:
            self.game_canvas.create_rectangle(ERASING_RECTANGLE_X1_AND_Y1, ERASING_RECTANGLE_X1_AND_Y1, ERASING_RECTANGLE_X2, ERASING_RECTANGLE_Y2, fill = BG_COLOR, outline = BG_COLOR)
            self.game_canvas.create_text(X_FOR_MANY_THINGS, GAME_OVER_AND_PLAYERS_Y, text = GAME_OVER, fill = BLACK_FILL, font = (GAME_OVER_FONT))
            if self.curr_player_index == 0:
                mesg = self.name2.get() + WIN_MSG
            elif self.curr_player_index == 1:
                mesg = self.name1.get() + WIN_MSG
            self.game_canvas.create_text(X_FOR_MANY_THINGS, PLAYER_WINS_Y, text = mesg, fill = BLACK_FILL, font = (PLAYER_WINS_FONT))
        elif self.board.is_board_full() == True:
            mesg = TIE_MSG
            self.game_state = GAME_OVER
            self.game_canvas.create_rectangle(ERASING_RECTANGLE_X1_AND_Y1, ERASING_RECTANGLE_X1_AND_Y1, ERASING_RECTANGLE_X2, ERASING_RECTANGLE_Y2, fill = BG_COLOR, outline = BG_COLOR)
            self.game_canvas.create_text(X_FOR_MANY_THINGS, GAME_OVER_AND_PLAYERS_Y, text = GAME_OVER, fill = BLACK_FILL, font = (GAME_OVER_FONT))
            self.game_canvas.create_text(X_FOR_MANY_THINGS, PLAYER_WINS_Y, text = mesg, fill = BLACK_FILL, font = (PLAYER_WINS_FONT))

    def draw_win_line(self, x1, y1, x2, y2):
        self.game_canvas.create_line(x1, y1, x2, y2, fill = WIN_LINE_COLOR, width = 3)

    def draw_board(self):
        self.game_canvas.create_line(self.cell_list[1].point_topleft.x, self.cell_list[1].point_topleft.y, self.cell_list[6].point_bottomright.x, self.cell_list[6].point_bottomright.y)
        self.game_canvas.create_line(self.cell_list[2].point_topleft.x, self.cell_list[2].point_topleft.y, self.cell_list[7].point_bottomright.x, self.cell_list[7].point_bottomright.y)
        self.game_canvas.create_line(self.cell_list[3].point_topleft.x, self.cell_list[3].point_topleft.y, self.cell_list[2].point_bottomright.x, self.cell_list[2].point_bottomright.y)
        self.game_canvas.create_line(self.cell_list[6].point_topleft.x, self.cell_list[6].point_topleft.y, self.cell_list[5].point_bottomright.x, self.cell_list[5].point_bottomright.y)
        for i in range(NUM_OF_CELLS):
            if self.board.get(i) == SHAPE_X:
                self.draw_x(self.cell_list[i])
            elif self.board.get(i) == SHAPE_O:
                self.draw_o(self.cell_list[i])
            else:
                pass
    
    def draw_x(self, cell):
        self.game_canvas.create_line(cell.point_topleft.x+SHAPE_OFFSET, cell.point_topleft.y+SHAPE_OFFSET, cell.point_bottomright.x-SHAPE_OFFSET, cell.point_bottomright.y-SHAPE_OFFSET, width = SHAPE_WIDTH, fill = X_COLOR)
        self.game_canvas.create_line(cell.point_topleft.x+SHAPE_OFFSET, cell.point_bottomright.y-SHAPE_OFFSET, cell.point_bottomright.x-SHAPE_OFFSET, cell.point_topleft.y+SHAPE_OFFSET, width = SHAPE_WIDTH, fill = X_COLOR)
    
    def draw_o(self, cell):
        self.game_canvas.create_oval(cell.point_topleft.x+SHAPE_OFFSET, cell.point_topleft.y+SHAPE_OFFSET, cell.point_bottomright.x-SHAPE_OFFSET, cell.point_bottomright.y-SHAPE_OFFSET, width = SHAPE_WIDTH, outline = O_COLOR)
    
    def run(self):
        self.rb1.select()
        self.rb4.select()
        self.player_selection()
        self.main_win.mainloop()
    
    def player_selection(self):
        if self.num_of_players.get() == 1:
            self.name2.delete(0, END)
            self.name2.insert(0, COMP)
            self.name2.config(state = DISABLED)
            self.start_button.forget()
            self.rb3.pack()
            self.rb4.pack()
            self.rb5.pack()
            self.start_button.pack()
        else:
            self.name2.config(state = NORMAL)
            self.name2.delete(0, END)
            self.rb3.forget()
            self.rb4.forget()
            self.rb5.forget()

    def run_game(self):
        skip = False
        if self.name1.get() == "" or self.name1.get() == INVALID_NAME_MSG:
            self.name1.delete(0, END)
            self.name1.config(font = (INVALID_NAME_MSG_FONT))
            self.name1.insert(0, INVALID_NAME_MSG)
            self.name1.config(font = (DEFAULT_FONT))
            skip = True
        if self.name2.get() == "" or self.name2.get() == INVALID_NAME_MSG:
            self.name2.delete(0, END)
            self.name2.config(font = (INVALID_NAME_MSG_FONT))
            self.name2.insert(0, INVALID_NAME_MSG)
            self.name2.config(font = (DEFAULT_FONT))
            skip = True
        if skip == True:
            return
        PLAYERS_TXT = self.name1.get() + VS + self.name2.get()
        self.settings.forget()
        self.game_canvas.pack()
        self.game.pack()
        if self.num_of_players.get() == 2:
            self.players = [Human(SHAPE_X), Human(SHAPE_O)]
        else:
            if self.cpu_level.get() == 1:
                self.players = [Human(SHAPE_X), CPU_Easy(SHAPE_O)]
            elif self.cpu_level.get() == 2:
                self.players = [Human(SHAPE_X), CPU_Medium(SHAPE_O)]
            elif self.cpu_level.get() == 3:
                self.players = [Human(SHAPE_X), CPU_Hard(SHAPE_O)]
        self.game_canvas.create_text(X_FOR_MANY_THINGS, GAME_OVER_AND_PLAYERS_Y, text = PLAYERS_TXT, fill = BLACK_FILL, font = (PLAYER_FONT))

    def check_names(self):
        name1 = self.name1.get()
        name2 = self.name2.get()
        if len(name1) > 0 and len(name2) > 0:
            self.start_button.config(state = NORMAL)


class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y


class Cell:
    def __init__ (self, p1, p2):
        self.point_topleft = p1
        self.point_bottomright = p2


class Board:
    def __init__ (self):
        self.tiles = []
        for i in range(NUM_OF_CELLS):
            self.tiles.append(None)

    def insert(self, tiles_number, shape):
        self.tiles[tiles_number] = shape

    def get(self, tiles_number):
        return self.tiles[tiles_number]

    def is_board_full(self):
        for i in range(NUM_OF_CELLS):
            if self.tiles[i] == None:
                return False
        return True


class Player:
    def __init__ (self, shape):
        self.shape = shape
  

class Human(Player):
    def __init__ (self, shape):
        Player.__init__(self, shape)


class CPU_Easy(Player):
    def __init__ (self, shape):
        Player.__init__(self, shape)
    
    def move(self, board):
        for i in range(9):
            if board.tiles[i] == None:
                board.tiles[i] = SHAPE_O
                return


class CPU_Medium(Player):
    def __init__ (self, shape):
        Player.__init__(self, shape)
    
    def move(self, board):
        empty_spot = self.next_move_win(board)
        if empty_spot != -1:
            board.tiles[empty_spot] = SHAPE_O
        elif board.tiles[4] == None:
            board.tiles[4] = SHAPE_O
        elif (board.tiles[0] == SHAPE_X and board.tiles[8] == SHAPE_X) or (board.tiles[2] == SHAPE_X and board.tiles[6] == SHAPE_X):
            for i in range(1, 9, 2):
                if board.tiles[i] == None:
                    board.tiles[i] = SHAPE_O
                    return
        else:
            for i in range(1, 9, 2):
                if board.tiles[i] == None:
                    board.tiles[i] = SHAPE_O
                    return

    def next_move_win(self, board):
        for i in range(3):
            if board.tiles[i*3] == SHAPE_X and board.tiles[i*3+1] == SHAPE_X and board.tiles[i*3+2] == None:
                return i*3+2
            if board.tiles[i*3+1] == SHAPE_X and board.tiles[i*3+2] == SHAPE_X and board.tiles[i*3] == None:
                return i*3
            if board.tiles[i*3] == SHAPE_X and board.tiles[i*3+2] == SHAPE_X and board.tiles[i*3+1] == None:
                return i*3+1
        for i in range(3):
            if board.tiles[i] == SHAPE_X and board.tiles[i+3] == SHAPE_X and board.tiles[i+3*2] == None:
                return i+3*2
            if board.tiles[i+3] == SHAPE_X and board.tiles[i+3*2] == SHAPE_X and board.tiles[i] == None:
                return i
            if board.tiles[i] == SHAPE_X and board.tiles[i+3*2] == SHAPE_X and board.tiles[i+3] == None:
                return i+3
        if board.tiles[0] == SHAPE_X and board.tiles[4] == SHAPE_X and board.tiles[8] == None:
            return 8
        if board.tiles[4] == SHAPE_X and board.tiles[8] == SHAPE_X and board.tiles[0] == None:
            return 0
        if board.tiles[0] == SHAPE_X and board.tiles[8] == SHAPE_X and board.tiles[4] == None:
            return 4
        if board.tiles[2] == SHAPE_X and board.tiles[4] == SHAPE_X and board.tiles[6] == None:
            return 6
        if board.tiles[4] == SHAPE_X and board.tiles[6] == SHAPE_X and board.tiles[2] == None:
            return 2
        if board.tiles[2] == SHAPE_X and board.tiles[6] == SHAPE_X and board.tiles[4] == None:
            return 4
        return -1


class CPU_Hard(Player):
    def __init__ (self, shape):
        Player.__init__(self, shape)
    
    def move(self, board):
        empty_spot = self.next_move_win(board)
        if empty_spot != -1:
            board.tiles[empty_spot] = SHAPE_O
        elif board.tiles[4] == None:
            board.tiles[4] = SHAPE_O
        elif (board.tiles[0] == SHAPE_X and board.tiles[8] == SHAPE_X) or (board.tiles[2] == SHAPE_X and board.tiles[6] == SHAPE_X):
            for i in range(1, 9, 2):
                if board.tiles[i] == None:
                    board.tiles[i] = SHAPE_O
                    return
        else:
            for i in range(0, 8, 2):
                if board.tiles[i] == None:
                    board.tiles[i] = SHAPE_O
                    return

    def next_move_win(self, board):
        for i in range(3):
            if board.tiles[i*3] == SHAPE_X and board.tiles[i*3+1] == SHAPE_X and board.tiles[i*3+2] == None:
                return i*3+2
            if board.tiles[i*3+1] == SHAPE_X and board.tiles[i*3+2] == SHAPE_X and board.tiles[i*3] == None:
                return i*3
            if board.tiles[i*3] == SHAPE_X and board.tiles[i*3+2] == SHAPE_X and board.tiles[i*3+1] == None:
                return i*3+1
        for i in range(3):
            if board.tiles[i] == SHAPE_X and board.tiles[i+3] == SHAPE_X and board.tiles[i+3*2] == None:
                return i+3*2
            if board.tiles[i+3] == SHAPE_X and board.tiles[i+3*2] == SHAPE_X and board.tiles[i] == None:
                return i
            if board.tiles[i] == SHAPE_X and board.tiles[i+3*2] == SHAPE_X and board.tiles[i+3] == None:
                return i+3
        if board.tiles[0] == SHAPE_X and board.tiles[4] == SHAPE_X and board.tiles[8] == None:
            return 8
        if board.tiles[4] == SHAPE_X and board.tiles[8] == SHAPE_X and board.tiles[0] == None:
            return 0
        if board.tiles[0] == SHAPE_X and board.tiles[8] == SHAPE_X and board.tiles[4] == None:
            return 4
        if board.tiles[2] == SHAPE_X and board.tiles[4] == SHAPE_X and board.tiles[6] == None:
            return 6
        if board.tiles[4] == SHAPE_X and board.tiles[6] == SHAPE_X and board.tiles[2] == None:
            return 2
        if board.tiles[2] == SHAPE_X and board.tiles[6] == SHAPE_X and board.tiles[4] == None:
            return 4
        return -1