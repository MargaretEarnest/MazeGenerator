import random

import pygame
from pygame.locals import QUIT, K_RETURN
from cell import Cell
from wall import Wall

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def makeMaze(mazeColumn, mazeRow):
    grid = [[0] * mazeColumn for _ in range(mazeRow)]
    for r in range(0, mazeRow):
        for c in range(0, mazeColumn):
            top, left = Wall(), Wall()
            if r != 0:
                top = grid[r - 1][c].getWalls()[2]
            if c != 0:
                left = grid[r][c - 1].getWalls()[1]
            grid[r][c] = Cell([top, Wall(), Wall(), left])
            for wall in grid[r][c].getWalls():
                wall.addOwner(grid[r][c])
    maze = []
    wallsToDo = []
    random.random()
    randomCell = grid[random.randint(0, mazeRow - 1)][random.randint(0, mazeColumn - 1)]
    maze.append(randomCell)
    for i in range(0, 4):
        wallsToDo.append(randomCell.getWalls()[i])

    while len(maze) < mazeColumn * mazeRow:
        randomWall = random.choice(wallsToDo)
        if len(randomWall.owner) > 1 and (maze.count(randomWall.owner[0]) == 0 or maze.count(randomWall.owner[1]) == 0):
            randomWall.breakWall()
            newOwner = randomWall.owner[0 if maze.count(randomWall.owner[0]) == 0 else 1]
            maze.append(newOwner)
            for i in range(0, 4):
                if newOwner.getWalls()[i].exists:
                    wallsToDo.append(newOwner.getWalls()[i])
        wallsToDo.remove(randomWall)
        if len(wallsToDo) == 0:
            print("GOT STUCK")
            return makeMaze(mazeColumn, mazeRow)
    return grid


# draws the maze
def drawMaze(DISPLAYSURF, grid, mazeColumn, mazeRow, pS):
    DISPLAYSURF.fill(WHITE)
    for r in range(0, mazeRow):
        for c in range(0, mazeColumn):
            if grid[r][c].getWalls()[0] is None or grid[r][c].getWalls()[0].exists:
                # top
                pygame.draw.line(DISPLAYSURF, BLACK, (pS + c * pS, pS + r * pS), (pS + (c + 1) * pS, pS + r * pS))
            if grid[r][c].getWalls()[1] is None or grid[r][c].getWalls()[1].exists:
                # right
                pygame.draw.line(DISPLAYSURF, BLACK, (pS + (c + 1) * pS, pS + r * pS),
                                 (pS + (c + 1) * pS, pS + (r + 1) * pS))
            if grid[r][c].getWalls()[2] is None or grid[r][c].getWalls()[2].exists:
                # down
                pygame.draw.line(DISPLAYSURF, BLACK, (pS + c * pS, pS + (r + 1) * pS),
                                 (pS + (c + 1) * pS, pS + (r + 1) * pS))
            if grid[r][c].getWalls()[3] is None or grid[r][c].getWalls()[3].exists:
                # left
                pygame.draw.line(DISPLAYSURF, BLACK, (pS + c * pS, pS + r * pS), (pS + c * pS, pS + (r + 1) * pS))


def game():
    """
    Maze game
    """

    mazeRow = 10
    mazeColumn = 10
    pS = 70

    grid = makeMaze(mazeColumn, mazeRow)

    pygame.init()
    pygame.display.set_caption("Maze")

    # create the window and color the background
    DISPLAYSURF = pygame.display.set_mode((mazeColumn * pS + pS*2, mazeRow * pS + pS*2))

    drawMaze(DISPLAYSURF, grid, mazeColumn, mazeRow, pS)

    while True:  # main game loop

        for event in pygame.event.get():

            # exit condition
            if event.type == QUIT:
                pygame.quit()

            # press return to restart a new turn
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    print("Return")

        pygame.display.update()


if __name__ == "__main__":
    game()
