import turtle
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






