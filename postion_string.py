names = ['ajay', 'teja']


def posy(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1


print(posy(names, 'ajay'))
