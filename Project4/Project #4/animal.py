#!/bin/python3.4
from binaryTree import BinaryTree
import dataLogic

class Animal(object):
    def __init__(self, file_path):
        self.root = dataLogic.load(file_path)
        self.file_path = file_path
        self.current_tree = self.root

    def make_new_question(self):
        animal = input("I am stumped. What animal were you thinking of?")
        question = input("What question should I have asked?")
        return [animal,question]

    def ask_question(self):
        return input(self.current_tree.key).lower()

    def guess_animal(self):
        return input("Is " + self.current_tree.key + " the animal you are thinking of?").lower()

def main():

        animal = Animal("data")
        if animal.root == None:
            if input("Would you like to play the animal game?").lower()[0] == "y":
                animal_answer,question = animal.make_new_question()
                animal.root = BinaryTree(question)
                animal.root.leftChild = BinaryTree(animal_answer)
                animal.root.righChild = BinaryTree(None)
                animal.current_tree = animal.root
                dataLogic.dump(animal.root,animal.file_path)
            else:
                return
        while True:
            animal.current_tree = animal.root
            contine_game = True
            play = input("Would you like to play the animal game?").lower()[0]
            if not play == "y":
                break
            while animal.current_tree.leftChild != None:
                answer = animal.ask_question()
                if answer[0] == "y":
                    animal.current_tree = animal.current_tree.leftChild
                else:
                    if animal.current_tree.rightChild == None:
                        new_animal,new_question = animal.make_new_question()
                        animal.current_tree.rightChild = BinaryTree(new_question)
                        animal.current_tree.rightChild.leftChild = BinaryTree(new_animal)
                        dataLogic.dump(animal.root,animal.file_path)
                        contine_game = False
                        break
                    else:
                        animal.current_tree = animal.current_tree.rightChild

            if contine_game:
                answer = animal.guess_animal()
                if answer[0] == "y":
                    print ("I am soooo smart!")
                else:
                    old_animal = animal.current_tree.key
                    new_animal, new_question = animal.make_new_question()
                    animal.current_tree.key = new_question
                    animal.current_tree.leftChild = BinaryTree(new_animal)
                    animal.current_tree.rightChild = BinaryTree(old_animal)
                    dataLogic.dump(animal.root,animal.file_path)
main()






