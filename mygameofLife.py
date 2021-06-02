import numpy as np
import matplotlib.pyplot as plt
import copy


#x = [1, 2, 3, 4, 5]
#y = [2, 3, 1, 6, 7]

figure = plt.figure(figsize=(8,8))
rangex = 100
rangey = 100

ar = np.zeros([rangex,rangey])

# def checknear(array,num):
#     for a in array:
#
#
#
#     return 0
#
def near_num(array, point):
    num = -array[point[0]][point[1]]
    around = [-1, 1, 0]
    for i in around:
        for j in around:
            if array[point[0] + i][point[1] + j] == 1:
                num += 1
    return num


def refresh(game_map):
    copy_map = copy.copy(game_map)
    for x in range(copy_map.shape[0] - 1):
        for y in range(copy_map.shape[1] - 1):
            num = near_num(copy_map, [x, y])
            if num > 3:
                game_map[x][y] = 0
            elif num == 3:
                game_map[x][y] = 1
                xseries.append(x)
                yseries.append(y)
            elif num == 0 or num == 1:
                game_map[x][y] = 0
    return game_map


import random
game_map = np.zeros([rangex,rangey])
xseries=[]
yseries=[]
#init x y
# for i in range(rangex*rangey):
#     x = random.randint(0,rangex-1)
#     y = random.randint(0,rangey-1)
#     xseries.append(x)
#     yseries.append(y)
#     game_map[x][y] = 1
for i in range(rangey):
    game_map[0][i] = 1
    xseries.append(0)
    yseries.append(i)
    game_map[rangex-1][i]=1
    xseries.append(rangex-1)
    yseries.append(i)
for i in range(rangex):
    game_map[i][0] = 1
    xseries.append(i)
    yseries.append(0)
    game_map[i][rangey-1]=1
    xseries.append(i)
    yseries.append(rangey-1)

while True:
    plt.clf()
    alive = 0
    for line in game_map:
        for point in line:
            if point == 1:
                alive += 1
    print(alive)
    plt.scatter(xseries, yseries, color='g', marker='.')
    plt.pause(0.1)
    plt.ioff()
    xseries=[]
    yseries=[]
    game_map = refresh(game_map)