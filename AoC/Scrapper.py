import os

cwd = os.getcwd()
inputFile = r"Input\input_file.txt"

inputPath = os.path.join(cwd, inputFile)

def counter():
    count = 0
    with open(inputPath, "r") as file:
        lines = file.readlines()

    for line in lines:
        numbers = []
        for (i, c) in enumerate(line):
            try:
                number = int(c)
                numbers.append(number)
            except:
                continue
        count += numbers[0]*10 + numbers[-1]

    print("The number is: ", count)