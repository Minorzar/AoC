import os
from collections import defaultdict

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")


def extract():

    allCardSplit = []
    total = 0

    with open(inputPath, "r") as file:
        cards = file.readlines()

    for card in cards:
        cardValue = []
        cardWinning = []
        change = 0

        card = card.split()

        for el in card:
            if el == '|':
                change = 1
            if change == 0:
                cardValue.append(el)
            else:
                cardWinning.append(el)
        cardWinning.pop(0)  # remove |
        cardValue.pop(0)
        cardValue.pop(0)    # remove Card n:
        allCardSplit.append((cardValue, cardWinning))

    for card in allCardSplit:
        matching = 0
        for el in card[0]:
            if el in card[1]:
                matching += 1

        total += 2**(matching-1)*(matching != 0)

    return int(total)