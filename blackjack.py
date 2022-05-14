#!/usr/bin/env python3
import random
valueMap = dict()
deck = []
suits = ["A", "D", "S", "H"]
vals = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def printHands():
    player = []
    for i in playerHand:
        player.append(i.name)
    print(f"Your Hand: {player}")
    print(f"Total: {totalHandValue(playerHand)}")
    print(f"Dealer Hand: {dealerHand[0].name}, ???")
    print()

def totalHandValue(hand):
    output = 0
    for i in hand:
        output += i.value
    return output

def hit(hand):
    hand.append(Card(deck.pop()))
    if (totalHandValue(hand) > 21):
        print("Bust")
    elif (totalHandValue(hand) == 21):
        print("BlackJack!")
    if (totalHandValue(hand) > 21 and containsAce(hand)):
        updateAceValue(hand)


def updateAceValue(hand):
    for i in hand:
        if i.value == 11:
            i.value = 1

def containsAce(hand):
    for i in hand:
        if i.value == 11 or i.value == 1:
            return True

def compareScores():
    print()
    print(f"Your Score: {totalHandValue(playerHand)}")
    print(f"Dealer Score: {totalHandValue(dealerHand)}")
    print()
    if (totalHandValue(playerHand) > totalHandValue(dealerHand)):
        print("You Win")
        print(f"Amount Won: {betAmount * 2}")
        money += int(betAmount) * 2
    elif (totalHandValue(playerHand) < totalHandValue(dealerHand)):
        print("Dealer Win")
        print(f"Amount Lost: {betAmount}")
        money -= betAmount
    else:
        print("Tie")
        print(f"Bet amount returned: {betAmount}")

class Card:
    def __init__(self, cardName):
        self.name = cardName
        self.value = valueMap.get(cardName)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def aceValueModifier(self):
        self.value = 1

money = 500
print("Welcome to blackjack!")
while (True):
    for suit in range(len(suits)):
        for j in range(len(vals)):
            deck.append(f"{vals[j]}{suits[suit]}")
            if (j >= 9):
                valueMap[f"{vals[j]}{suits[suit]}"] = 10
            if (vals[j] == "A"):
                valueMap[f"{vals[j]}{suits[suit]}"] = 11
            else:
                valueMap[f"{vals[j]}{suits[suit]}"] = j + 1

    random.shuffle(deck)
    card1 = Card(deck.pop())
    card2 = Card(deck.pop())
    playerHand = [card1, card2]
    dealerHand = [Card(deck.pop()), Card(deck.pop())]
    while (True):
        print(f"Your Money: {money}")
        print()
        betAmount = input("How much would you like to bet?: ")
        if (totalHandValue(playerHand) > 21):
            updateAceValue(playerHand)
        standing = False
        while (totalHandValue(playerHand) <= 21):
            printHands()
            actionChoice = input("Hit or Stand (H/S): ")
            if (actionChoice == "H"):
                hit(playerHand)
                continue
            break
        while (totalHandValue(dealerHand) <= 21):
            printHands()
            if (totalHandValue(dealerHand) == 21):
                print("Dealer BlackJack!")
            elif (totalHandValue(dealerHand) < 17):
                hit(dealerHand)
                continue
            break
        compareScores()


    break

