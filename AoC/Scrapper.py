import os

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")


symbols = set('*$+#-/%&=@')


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
            neighbors.append(matrix[new_row][new_col])

    return neighbors

def isValid(matrix, number, x, y):
    n = len(number)
    for i in range(n):
        neig = get_neighbors(matrix, x, y-i)

        for sym in symbols:
            if sym in neig:
                print(number)
                return int(number)

    return 0

def extract():

    count = 0
    num = ""

    with open(inputPath, "r") as file:
        data = file.readlines()

    for (x, line) in enumerate(data):
        for (y, car) in enumerate(line):
            try:
                n = int(car)
                num += car
            except:
                if num != "":
                    count += isValid(data, num, x, y-1)
                    num = ""

    return count