import random


myDeck = []
for f in range(1973):
    myDeck = list(range(1, 79))


def coupeDeck(deck):
    n = random.randint(3, 77)
    print(n-1)
    part1 = deck[:n-1]
    m = 79 - n
    part2 = deck[-m:]
    result = part2 + part1
    return result


print"==============================="
print(myDeck)
newDeck = coupeDeck(myDeck)
print(newDeck)
