import turtle
from tkinter import messagebox
from Figure import Figure
class TetrisGame:
    def __init__(self):
        self.board_width=10
        self.board_height=20
        self.cell_size=25

        self.score=0

        self.screen=turtle.Screen()
        self.screen.title("Тетріс!")
        self.screen.bgcolor("black")

        window_width=self.board_width*self.cell_size+250
        window_height=self.board_height*self.cell_size+100
        self.screen.setup(window_width, window_height)
        self.screen.tracer(0)

        self.pen=turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")

        self.board=[[0]*self.board_width for _ in range(self.board_height)]

        self.current_figure=None
        self.game_running=True

        self.screen.listen()
        self.screen.onkeypress(self.move_left,"Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.rotate_figure, "Up")

        self.spawn_figure()

    def spawn_figure(self):
        self.current_figure=Figure()

        if not self.can_move(self.current_figure.shape,self.current_figure.x, self.current_figure.y):
            self.game_running=False
            self.screen.update()
            messagebox.showinfo("Гра завершена", f"Game Over!\nВаш рахунок:{self.score}")
            self.reset_game()

    def reset_game(self):
        self.board=[[0]*self.board_width for _ in range(self.board_height)]
        self.score=0
        self.game_running=True
        self.spawn_figure()

    def update_logic(self):
        if not self.game_running:
            return

        if self.can_move(self.current_figure.shape, self.current_figure.x, self.current_figure.y+1):
            self.current_figure.move_down()
        else:
            self.merge_figure_to_board()
            self.clear_lines()
            self.spawn_figure()

    def can_move(self, shape, cx, cy):
        for dx, dy in shape:
            board_x=cx+dx
            board_y=cy+dy

            if board_x<0 or board_x>=self.board_width or board_y>=self.board_height:
                return False
            if board_y>=0 and self.board[board_y][board_x]!=0:
                return False
        return True






















