import pickle
import os

def load(file_name):
    if os.path.isfile(file_name):
        return pickle.load(open(file_name, "rb"))
    else:
        return None

def dump(tree, file_name):
    if not os.path.isfile(file_name):
        open(file_name,"a").close()
    pickle.dump(tree, open(file_name, "wb"))

