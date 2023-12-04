# AoC
This is the repository of my work on the Advent of Code 2023 code

## Day 1:

# Puzzle 1

    The idea is to look for each caracter of the line and check if it's a number. The option I went with is to
    add all result inside an array then add the first number find time ten and the last.

    The code works and I got the star.

# Puzzle 2

    The idea is the same as puzzle 1 but now to also check for instance of number in text. The option I went with
    is to check first for all instances, add them with their index, check for number the sort the array by the
    index and do the same operation.

    The code works and I got the star.

## Day 2

# Puzzle 1

    The idea is to decompose each game into pieces (each set of cube) then to get the value before the color and
    check if it's greater or not than one of the limits.

    The code works and I got the star.

# Puzzle 2

    Same as before but we just modify the maximum value got for each game instead of them being fixed. I also
    change the bol to be a return of the modified maximum values then I put the power of each game in an array.

    The code works and I got the star.

## Day 3

# Puzzle 1
    
    The idea is to look at every number in the file, add them in a string if they are in a row. When the number
    is "over", we check if there is any symbol near it and add it or not to the total.

    The code works and I got the star.

# Puzzle 2

    The idea is to get all occurence of number near a so called gear. After that get the whole number and put it
    in an array. I then use a dictionary to be able to get the multiple number near a gear then multiply them if
    their are more thant 1 number for a gear/

    The code works and I got the star.

## Day 4

# Puzzle 1

    The idea is to decompose the card into two array: one with the number to check and the other with the winning
    numbers. The to check if any of the winning number is in the number to check (or the inverse) and then compute
    the card value.

    The code works and I got the star.

# Puzzle 2

    The idea is to create an array that comport all the number of card we have (set to one by default), then to 
    calculate the number of card we have each time we won (for one card the to multiply by the number of instance
    of the card).

    The code works and I got the star.