import os
from collections import defaultdict

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")


def get_neighbors(matrix, row, col):
    neighbors = []

    index = [
        (-1, -1), (-1, 0),  (-1, 1),
        (0,  -1),           (0, 1),
        (1,  -1), (1, 0),   (1, 1)
    ]

    for i, j in index:
        new_row, new_col = row + i, col + j

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            neighbors.append(((new_row, new_col), matrix[new_row][new_col]))

    return neighbors

def getNumber(matrix, x, y, xStar, yStar):
    line = matrix[x]
    number = ""
    numberM = ""
    n = len(line)
    subline = line[y-2:y+3]

    for car in subline:
        if car.isdigit():
            number += car
        else:
            number = ""

        if len(number) > len(numberM):
            numberM = number


    return [(xStar, yStar), int(numberM)]


def extract():

    num = ""
    nearGear = []
    count = 0
    coord_dict = defaultdict(list)
    starCount = 0

    with open(inputPath, "r") as file:
        data = file.readlines()

    for (x, line) in enumerate(data):
        for (y, car) in enumerate(line):

            if car == "*":
                starCount += 1
                nei = get_neighbors(data, x, y)
                for ((xNei, yNey), value) in nei:
                    try:
                        int(value)
                        ngAdd = getNumber(data, xNei, yNey, x, y)
                        if ngAdd not in nearGear:
                            nearGear.append(ngAdd)
                    except:
                        pass

    for (xStar, yStar), num in nearGear:
        coord_dict[(xStar, yStar)].append(num)

    for coord, values in coord_dict.items():
        if len(values) != 1:
            multiplication = 1
            for value in values:
                multiplication *= value
            count += multiplication

    return count