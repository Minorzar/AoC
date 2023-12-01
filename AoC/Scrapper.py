import os

cwd = os.getcwd()
inputFile = r"Input\input_file.txt"
num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

inputPath = os.path.join(cwd, inputFile)

def counter():
    count = 0
    with open(inputPath, "r") as file:
        lines = file.readlines()

    for line in lines:
        numbers = []
        for n in num:
            index = line.find(n)
            while index != -1:
                numbers.append((index, num.index(n)))
                index = line.find(n, index + 1)
        for (i, c) in enumerate(line):
            try:
                number = int(c)
                numbers.append((i, number))
            except:
                continue
        numbers = sorted(numbers, key=lambda x: x[0])
        count += numbers[0][1]*10 + numbers[-1][1]

    print("The number is: ", count)