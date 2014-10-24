__author__ = 'bryan'
from Deque import Deque


class Palindrome(object):
    def __init__(self,string):
        self.string = string
        self.deque = Deque()
        self.converToDeque()

    def converToDeque(self):
        for char in self.string:
            self.deque.append(char.lower())

    def check(self):
        isPalindrome = True
        while self.deque.length() > 1:
            first = self.deque.popBeginning()
            last = self.deque.popEnd()
            if first != last:

                isPalindrome = False
                break
        return isPalindrome
tests = {'Palindrome': False, 'madam': True, 'solos': True, 'peeweep': True, 'Racecar': True, 'level': True, 'minim': True, 'testset': True, 'aibohphobia': True, 'stats': True, 'Malayalam': True, 'devoved': True, 'Radar': True, 'Monty': False, 'racecar': True, 'rotator': True, 'Hannah': True, 'repaper': True, 'reviver': True, 'alula': True, 'lemel': True, 'terret': True, 'rotavator': True, 'tenet': True, 'cammac': True, 'refer': True, 'deleveled': True, 'civic': True, 'retder': False, 'kayak': True, 'reifier': True, 'deified': True, 'sexes': True, 'evitative': True, 'dewed': True, 'sagas': True, 'radar': True, 'Civic': True, 'rotor': True, 'detartrated': True, 'kinnikinnik': True, 'murdrum': True}
"""tests = {   "monty" : False,
                "radar" : True,
                "racecar" : True,
                "palindrome" : False,
                "civic" : True }"""
#strs = ["Radar", "Palindrome", "Racecar", "Monty", "Civic", "aibohphobia", "alula", "cammac", "civic", "deified", "deleveled", "detartrated", "devoved", "dewed", "evitative", "Hannah", "kayak", "kinnikinnik", "lemel", "level", "madam", "Malayalam", "minim", "murdrum", "peeweep", "racecar", "radar", "retder", "refer", "reifier", "repaper", "reviver", "rotator", "rotavator", "rotor", "sagas", "solos", "sexes", "stats", "tenet", "terret", "testset"]
for string in tests.keys():
    pal = Palindrome(string)
    correct = tests[string] == pal.check()
    print("Is Correct: " + str(correct))
