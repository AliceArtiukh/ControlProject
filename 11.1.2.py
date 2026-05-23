import random
import turtle
import time
rows=20
cols=10
screen_width=400
screen_height=600
pedding_x=150
pedding_y=100
cell_size=min((screen_width-pedding_x)/cols, (screen_height-pedding_y)/rows)
colors=['red','green','blue','yellow','magenta','cyan', 'orange']
shapes=[(0,-1),(0,0),(0,1),(0,2)]
print(cell_size)