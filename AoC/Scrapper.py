import os
from collections import defaultdict

inputPath = os.path.join(os.getcwd(), r"Input\input_file.txt")


def extract():

    allCardSplit = []
    total = 0

    with open(inputPath, "r") as file:
        cards = file.readlines()

    totalCard = [1 for _ in range(len(cards))]

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

    for (index, card) in enumerate(allCardSplit):
        cardIndex = index + 1
        for el in card[0]:
            if el in card[1]:
                totalCard[cardIndex] += 1*totalCard[index]
                cardIndex += 1


    return int(sum(totalCard))