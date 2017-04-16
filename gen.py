import numpy as np


def filetolist(fname,a):
    with open(fname) as f:
        for line in f:
            a.append(line.rstrip("\n"))
    return a




features=filetolist("features-normal.txt",[])
features=filetolist("features-magical.txt",features)


materials=filetolist("materials-normal.txt",[])
materials=filetolist("materials-special.txt",materials)
weapons=filetolist("weapons-simple.txt",[])
weapons=filetolist("weapons-martial.txt",weapons)
adjectives=filetolist("adjectives.txt",[])

def get_flavour():
    weaponhead="Check out what I found!\nIt's a {} {} {} with {}.".format(np.random.choice(adjectives,1)[0], np.random.choice(materials,1)[0], np.random.choice(weapons,1)[0], np.random.choice(features,1)[0])
    haft=" Its {} handle has {}.".format(np.random.choice(adjectives,1)[0], np.random.choice(features,1)[0])

    return weaponhead+haft



if __name__ == '__main__':
    print(get_flavour())
