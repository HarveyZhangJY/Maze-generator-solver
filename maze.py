#coding=gbk
import numpy as np
from random import randint, choice
def setMap(map, x, y, value):
    map[x][y] = value
def isVisited(map, x, y):
    return map[x][y] != 0

def checkAdjacentPos(map, x, y, width, height, checklist):
    directions = []
    if x > 0:
        if not isVisited(map, 2 * (x - 1) + 1, 2 * y + 1):
            directions.append(0)
    if y > 0:
        if not isVisited(map, 2 * x + 1, 2 * (y - 1) + 1):
            directions.append(1)
    if x < width - 1:
        if not isVisited(map, 2 * (x + 1) + 1, 2 * y + 1):
            directions.append(2)
    if y < height - 1:
        if not isVisited(map, 2 * x + 1, 2 * (y + 1) + 1):
            directions.append(3)

    if len(directions):
        direction = choice(directions)

        if direction == 0:
            setMap(map, 2 * (x - 1) + 1, 2 * y + 1, 1)
            setMap(map, 2 * x, 2 * y + 1, 1)
            checklist.append((x - 1, y))
        elif direction == 1:
            setMap(map, 2 * x + 1, 2 * (y - 1) + 1, 1)
            setMap(map, 2 * x + 1, 2 * y, 1)
            checklist.append((x, y - 1))
        elif direction == 2:
            setMap(map, 2 * (x + 1) + 1, 2 * y + 1, 1)
            setMap(map, 2 * x + 2, 2 * y + 1, 1)
            checklist.append((x + 1, y))
        elif direction == 3:
            setMap(map, 2 * x + 1, 2 * (y + 1) + 1, 1)
            setMap(map, 2 * x + 1, 2 * y + 2, 1)
            checklist.append((x, y + 1))
        return True
    else:
        return False


def maze(width, height):
    map = np.zeros((2 * width + 1, 2 * height + 1))
    map[1, 1] = 1
    checklist = [(0, 0)]
    while len(checklist):
        entry = choice(checklist)
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            checklist.remove(entry)
    return map

dirs = [
    lambda x,y:(x+1,y),#下
    lambda x,y:(x-1,y),#上
    lambda x,y:(x,y-1),#左
    lambda x,y:(x,y+1),#右
]
def maze_path(stack, maze, x1,y1,x2,y2):
    maze[1][1] = 3
    stack.append((x1,y1))
    while(len(stack)>0):
        curNode = stack[-1] # 当前的节点
        if curNode[0]==x2 and curNode[1]==y2:
            # 走到终点了
            print(stack)
            return True
        # x,y 四个方向：上 x-1,y, 右 x,y+1, 下 x+1,y, 左 x,y-1
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 1:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            stack.pop()
    else:
        print('没有路 No solution')
        return False
if __name__ == "__main__":
    # while 1:
    width = int(input("width:"))
    height = int(input("height:"))
    m = maze(width, height)
    stack = []
    maze_path(stack, m, 1,1,2*width-1, 2*height-1)
    for k in stack:
        m[k[0]][k[1]] = 3
    with open('maze.txt', 'w') as f:
        for i in m:
            for j in i:
                if j == 0:
                    f.write('#')
                    print("#", end=" ")
                elif j == 1 or j == 2:
                    f.write(' ')
                    print(" ", end=" ")
                elif j == 3:
                    f.write(' ')
                    print(" ", end=" ")
            print()
            f.write('\n')
    with open('maze_answer.txt', 'w') as f:
        for i in m:
            for j in i:
                if j == 0:
                    f.write('#')
                    print("#", end=" ")
                elif j == 1 or j == 2:
                    f.write(' ')
                    print(" ", end=" ")
                elif j == 3:
                    f.write('o')
                    print("o", end=" ")
            print()
            f.write('\n')
    f.close()