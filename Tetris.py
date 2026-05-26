import turtle
from tkinter import messagebox
from Figure import Figure
class TetrisGame:
    def __init__(self):
    def spawn_figure(self):
        self.current_figure = Figure()

        if not self.can_move(self.current_figure.shape,self.current_figure.x, self.current_figure.y):
            self.game_running = False
            self.screen.update()
            messagebox.showinfo("Гра завершена", f"Game Over!\nВаш рахунок:{self.score}")
            self.reset_game()

    def reset_game(self):
        self.board = [[0]* self.board_width for _ in range(self.board_height)]
        self.score = 0
        self.game_running = True
        self.spawn_figure()

    def update_logic(self):
        if not self.game_running:
            return

        if self.can_move(self.current_figure.shape, self.current_figure.x, self.current_figure.y + 1):
            self.current_figure.move_down()
        else:
            self.merge_figure_to_board()
            self.clear_lines()
            self.spawn_figure()

    def can_mave(self, shape, cx, cy):
      for dx, dy in shape:
        board_x = cx + dx
        board_y = cy + dy

        if board_x < 0 or board_x >= self.board_width or board_y >= self.board_height:
            return False
        if board_y >=0 and self>board[board_y][board_x]! =0:
            return False
        return True























