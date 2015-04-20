__author__ = 'Babalooey04'
import pickle
import os


def load(data):
    if os.path.isfile(data):
        return pickle.load(open(data,"rb"))
    else:
        return None

def dump(Tree, data):
    if not os.path.isfile(data):
        open(data, "a").close()
    pickle.dump(Tree , open(data,"wb"))