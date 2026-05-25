import turtle
import time
from Figure import Figure
rows=20
cols=10
screen_width=400
screen_height=600
pedding_x=150
pedding_y=100
cell_size=min((screen_width-pedding_x)/cols, (screen_height-pedding_y)/rows)
class TetrisGame:
    def __init__(self):
        self.screen=turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(screen_width, screen_height)
        self.screen.title("Tetris")
        self.screen.tracer(0)
        self.drawer=turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.text_drawer=turtle.Turtle()
        self.text_drawer.hideturtle()
        self.text_drawer.penup()
        self.text_drawer.color("white")
        self.score=0
        self.game_over=False

        self.grid=[]
        for r in range(rows):
            row=[0]*cols
            self.grid.append(row)

        self.current_figure=Figure(cols)

        self.screen.listen()
        self.screen.onkey(self.press_left, "Left")
        self.screen.onkey(self.press_right, "Right")
        self.screen.onkey(self.press_up, "Up")
        self.screen.onkey(self.press_down, "Down")

        self.last_fall_time=time.time()
        self.fall_speed=0.5

    def screen_coords(self, row,col):
        start_x=-(cols*cell_size)/2
        start_y=(rows*cell_size)/2
        x=start_x+col*cell_size
        y=start_y-row*cell_size
        return x,y

    def draw_cell(self,row,col,color):
        x,y=self.screen_coords(row,col)
        self.drawer.goto(x,y)
        self.drawer.pendown()
        self.drawer.fillcolor(color)
        self.drawer.begin_fill()
        for i in range(4):
            self.drawer.forward(cell_size-1)
            self.drawer.right(90)
        self.drawer.end_fill()
        self.drawer.penup()

    def draw_everything(self):








