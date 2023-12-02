import os

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")


def find_color(color, rMax, gMax, bMax):
    if color.find("red") != -1:
        color = color.replace("red", '')
        if int(color) > rMax:
            return int(color), gMax, bMax
        return rMax, gMax, bMax

    if color.find("blue") != -1:
        color = color.replace("blue", '')
        if int(color) > bMax:
            return rMax, gMax, int(color)
        return rMax, gMax, bMax

    if color.find("green") != -1:
        color = color.replace("green", '')
        if int(color) > gMax:
            return rMax, int(color), bMax
        return rMax, gMax, bMax

def extract():
    games = []
    gameSet = []
    colors = []
    power = []

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
        rMax = 0
        gMax = 0
        bMax = 0
        for gSet in game:
            for color in gSet:
                (rMax, gMax, bMax) = find_color(color, rMax, gMax, bMax)

        power.append(rMax*gMax*bMax)

    return sum(power)