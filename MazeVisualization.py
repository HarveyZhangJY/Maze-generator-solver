import maze
from PIL import Image
import numpy as np
print(1)
width = 100
height = 100
print(1)
image = Image.new(mode="RGB", size=(2*width+1, 2*height+1))
print(1)
map = maze.maze(width, height)
print(1)
m = map
stack = []
maze.maze_path(stack, m, 1,1,2*width-1, 2*height-1)
for k in stack:
    map[k[0]][k[1]] = 3
print(map)
width, height = image.size
for i in range(width):
    for j in range(height):
        if m[i][j] != 3:
            image.putpixel((i, j), (int(map[i][j])*255, int(map[i][j])*255, int(map[i][j])*255))
        if m[i][j] == 3:
            image.putpixel((i, j), (255, 0, 0))
        print(image.getpixel((i, j)))
image.show()
image.save("maze.png")