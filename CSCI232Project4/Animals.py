from Tree import Tree
import dataLogic

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == 'y'

def animal():
    # start with a singleton
    root = dataLogic.load("data")
    if root is None:
        root = Tree("bird")

    # loop until the user quits
    while True:
        if not yes("Would you like to play a game? "):
            break


        # walk the tree
        tree = root
        while tree.left != None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print ("I rule!")
            continue

        # get new information
        prompt = "What is the animal's name? "
        animal = input(prompt)
        prompt = "What question would distinguish a %s from a %s? "
        question = input(prompt % (animal, guess))

        # add new information to the tree
        tree.cargo = question
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % animal):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
        dataLogic.dump(Tree, "data")

main = animal()
