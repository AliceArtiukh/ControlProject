import time
from Tetris import TetrisGame


def main():
  game = TetrisGame()
  last_update_time = time.time()

  while True:
   current_time = time.time()

   if current_time - last_update_time >= 0.4:
      game.update_logic()
      last_update_time = current_time

   game.render()
   time.sleep(0.01)


if __name__ == "__main__":
   main()

