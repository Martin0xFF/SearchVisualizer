import pygame as sdl
import sys
from random import randint

class BFS():
    def __init__(self, grid, width=100, height=100, goal=(0,0), start=(0,0)):
        self.grid = grid
        self.goal = goal
        self.width = width
        self.height = height
        self.frontier = [start]
        self.explored = set()

    def successor(self, node):

        if node[0] != 0:
            if (node[0]-1, node[1]) not in self.explored:
                if self.grid[node[0]-1][node[1]] == 2:
                    self.explored.add((node[0]-1, node[1]))
                    self.frontier.append((node[0]-1, node[1]))
        if node[0] != self.width-1:
            if self.grid[node[0]+1][node[1]] == 2:
                if (node[0]+1, node[1]) not in self.explored:
                    self.explored.add((node[0]+1, node[1]))
                    self.frontier.append((node[0]+1, node[1]))
        if node[1] != 0:
            if self.grid[node[0]][node[1]-1] == 2:
                if (node[0], node[1]-1) not in self.explored:
                    self.explored.add((node[0], node[1]-1))
                    self.frontier.append((node[0], node[1]-1))
        if node[1] != self.height-1:
            if self.grid[node[0]][node[1]+1] == 2:
                if (node[0], node[1]+1) not in self.explored:
                    self.explored.add((node[0], node[1]+1))
                    self.frontier.append((node[0], node[1]+1))

    def is_goal(self,node):
        if node == self.goal:
            return True

    def step(self):
        if len(self.frontier) == 0:
            return False

        node = self.frontier.pop(0)
        self.grid[node[0]][node[1]] = 1
        if self.is_goal(node):
            return True

        self.successor(node)





sdl.init()
size = width, height = 400, 400
speed= [1, 1]
black = 0, 0, 0

screen = sdl.display.set_mode(size)
rect  = sdl.Rect(0,0,64,64)
cmap = {1:(0xff,0xff,0xff), 2: (0,0,0xff), 3:(0,0xff,0)}
grid = []

def init_grid(grid, px_width=8):
    for i in range(width//px_width):
        temp = []
        for j in range(height//px_width):
            val = 2
            temp.append(val)
        grid.append(temp[:])


def draw_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect  = sdl.Rect(i*8,j*8,7,7)
            sdl.draw.rect(screen, cmap[grid[i][j]], rect)

def spread(grid):
    temp = grid[:][:]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i != 0:
                    if grid[i-1][j] != 1:
                        temp[i-1][j] = 1

                if i != len(grid)-1:
                    if grid[i+1][j] != 1:
                        temp[i+1][j] = 1

                if j != 0:
                    if grid[i][j-1] != 1:
                        temp[i][j-1] = 1

                if j != len(grid[0])-1:
                    if grid[i][j+1] != 1:
                        temp[i][j+1] = 1
    [print(row) for row in temp]
    [print(row) for row in grid]
    return temp


def update_grid(grid, rule):
    grid = rule(grid)
clock = sdl.time.Clock()


init_grid(grid)
for j in range(len(grid)-3):
    if True:
        grid[j][20] = 3


bfs = BFS(grid=grid, width=width//8, height=height//8, start=(15,35))

while True:
    for event in sdl.event.get():
        if event.type == sdl.QUIT: sys.exit()

    screen.fill(black)
    bfs.step()
    draw_grid(grid)
    sdl.display.flip()
    clock.tick(60)


