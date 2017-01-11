def play2(l):
    try:
        for i in l:
            for num in play2(i):
                yield num
    except TypeError:
        yield l


def play(l):
    res = []
    for i in l:
        if isinstance(i, list):
            t=list(play(i))
            for j in t:
                res.append(j)
        else:
            res.append(i)
    return res

def sum(l):
    res = 0
    for i in l:
        if not isinstance(i, list):
            res+=i
        else:
            res+=sum(i)
    return res

def play3(l):
    try:
        try: l+''
        except TypeError: pass
        else: raise TypeError
        for i in l:
            for s in play3(i):
                yield s
    except TypeError:
        yield l

if __name__ == '__main__':
    l = [1,[2,[3,4,[5,6]]]]
    l2=['abs',['de','fg',['hi','jk']]]
    print(sum(l))
    print('play',list(play(l2)))
    print('play2',list(play2(l2)))
    print('play3',list(play3(l2)))