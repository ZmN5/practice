def isconflict(state, nx):
    """
    验证下一个要放置的皇后是否与之前的皇后冲突
    """
    ny = len(state)
    for i in range(ny):
        if abs(state[i]-nx) in (0, ny-i):
            return True
    return False


def queens(num=8, state=[]):
    """
    主处理函数
    """
    for p in range(num):
        if not isconflict(state, p):
            if len(state) == num-1:
                yield p
            else:
                for result in queens(num, state+[p]):
                    yield [result, p]


def play3(l):
    """
    把返回的结果列表中的子列表裂解开
    """
    try:
        try: l+''
        except TypeError: pass
        else: raise TypeError
        for i in l:
            for s in play3(i):
                yield s
    except TypeError:
        yield l

def printqueens(l):
    """
    打印输出结果
    """
    l = play3(l)
    l = list(l)
    n = len(l)
    for i in range(n):
        for j in range(n):
            if j != l[i]:
                print('.', end=' ')
            else:
                print('q', end=' ')
        print(' ')

if __name__ == '__main__':
    l = list(queens(5))
    print(l)
    n = len(l)
    print('有 {0} 种放置方法：'.format(n))
    for i in range(n):
        print('--------------------')
        printqueens(l[i])
        print('--------------------')
