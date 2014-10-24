__author__ = 'bryan'
import random
from Baseball import Baseball
from Stack import Stack

def createSpeed():
    return random.randrange(70, 100)

def choosePitchType(pitchTypes):
    return pitchTypes[random.randint(len(pitchTypes) - 1)]

def isStrike():
    return bool(random.randint(0, 1))

def generateBaseball():
    return Baseball(isStrike(), createSpeed())

def createStack():
    stack = Stack()
    for num in range(20):
        stack.push(generateBaseball())
    return stack



def main():
    strikes = 0
    pitches = 0
    hits = []
    stack = createStack()
    while strikes < 9:
        ball = stack.pop()
        pitches += 1
        didSwing = input("Swing or Pass: ")
        if didSwing.lower() == "swing":
            if ball.isStrike:
                print("Hit!\n" + str(ball))
                hits.append(ball)
            else:
                print("Strike!\n" + str(ball))
                strikes += 1
        elif didSwing.lower() == "pass":
            if ball.isStrike:
                print("Strike!\n" + str(ball))
                strikes += 1
            else:
                print("Ball!\n" + str(ball))

    print("\nInning over!\nNumber of Pitches: " + str(pitches) + "\nNumber of hits: " + str(len(hits)) + "\nHere is a list of all the balls hit:")
    for ball in hits:
        print(str(ball))

if __name__ == "__main__":
    main()

