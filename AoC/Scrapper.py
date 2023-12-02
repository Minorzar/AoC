import os

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")

rMax = 12
gMax = 13
bMax = 14

def find_color(color):
    if color.find("red") != -1:
        color = color.replace("red", '')
        if int(color) > rMax:
            return False
        return True

    if color.find("blue") != -1:
        color = color.replace("blue", '')
        if int(color) > bMax:
            return False
        return True

    if color.find("green") != -1:
        color = color.replace("green", '')
        if int(color) > gMax:
            return False
        return True

def extract():
    games = []
    gameSet = []
    colors = []
    count = 0

    with open(inputPath, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.split(' ')
        line = line[2:]
        games.append(''.join(line))        # get games as a string

    for game in games:
        gameSet.append(game.split(';'))              # get a list of the set of cube

    for (i, game) in enumerate(gameSet):
        colors.append([])
        for gSet in game:
            colors[i].append(gSet.split(','))       # get a list of colors

    for (idGame, game) in enumerate(colors):
        bol = True
        for gSet in game:
            for color in gSet:
                bol = bol and find_color(color)

        if bol:
            count += (idGame + 1)

    return count