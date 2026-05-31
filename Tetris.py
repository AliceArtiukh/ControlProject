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
        self.screen.setup(width=window_width, height=window_height)
        self.screen.tracer(0)

        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)

        self.score_pen=turtle.Turtle()
        self.score_pen.penup()
        self.score_pen.hideturtle()
        self.score_pen.speed(0)
        self.score_pen.pencolor("white")

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
    def merge_figure_to_board(self):
      for dx, dy in self.current_figure.shape:
        board_x=self.current_figure.x+dx
        board_y=self.current_figure.y+dy
        if 0<= board_y<self.board_height and 0<= board_x<self.board_width:
            self.board[board_y][board_x]=self.current_figure.color

    def clear_lines(self):
      new_board=[row for row in self.board if 0 in row]
      lines_cleared = self.board_height-len(new_board)

      if lines_cleared>0:
          self.score+=lines_cleared*100

          self.board=[[0]*self.board_width for _ in range(lines_cleared)]+new_board

    def draw_square(self, x, y, color):
      screen_x=(x-self.board_width/2)*self.cell_size
      screen_y=(self.board_height/2-y)*self.cell_size

      self.pen.goto(screen_x, screen_y)
      self.pen.fillcolor(color)
      self.pen.pencolor("#222222")
      self.pen.begin_fill()
      for _ in range(4):
        self.pen.forward(self.cell_size-1)
        self.pen.right(90)
      self.pen.end_fill()

    def draw_score(self):
      self.score_pen.clear()
      x_pos=(self.board_width / 2) * self.cell_size+30
      y_pos=0
      self.score_pen.goto(x_pos, y_pos)
      self.score_pen.write(f"Рахунок:\n{self.score}", align="left", font=("Arial", 20, "bold"))

    def render(self):
        self.pen.clear()
        self.pen.pencolor("white")
        x_left = (-self.board_width / 2) * self.cell_size
        x_right = (self.board_width / 2) * self.cell_size
        y_top = (self.board_height / 2) * self.cell_size
        y_bottom = (-self.board_height / 2) * self.cell_size

        self.pen.goto(x_left, y_top)
        self.pen.pendown()
        self.pen.goto(x_left, y_bottom)
        self.pen.goto(x_right, y_bottom)
        self.pen.goto(x_right, y_top)
        self.pen.penup()

        for r in range(self.board_height):
            for c in range(self.board_width):
                if self.board[r][c] != 0:
                    self.draw_square(c, r, self.board[r][c])

        if self.current_figure:
            for dx, dy in self.current_figure.shape:
                self.draw_square(self.current_figure.x + dx, self.current_figure.y + dy, self.current_figure.color)

        self.draw_score()
        self.screen.update()

    def move_left(self):
        if self.can_move(self.current_figure.shape, self.current_figure.x - 1, self.current_figure.y):
            self.current_figure.move_side(-1)
            self.render()

    def move_right(self):
        if self.can_move(self.current_figure.shape, self.current_figure.x + 1, self.current_figure.y):
            self.current_figure.move_side(1)
            self.render()

    def move_down(self):
        if self.can_move(self.current_figure.shape, self.current_figure.x, self.current_figure.y + 1):
            self.current_figure.move_down()
            self.render()

    def rotate_figure(self):
        self.current_figure.rotate()
        if not self.can_move(self.current_figure.shape, self.current_figure.x, self.current_figure.y):
            self.current_figure.rotate()
            self.current_figure.rotate()
            self.current_figure.rotate()
        self.render()
























