from collections import defaultdict
def xor(l):
    tmp = 0
    for item in l:
        tmp ^= item
    return tmp


def odd(arr):
    status = defaultdict(int)
    for i in arr:
        if status[i] == 1:
            del status[i]
        else:
            status[i] = 1
    res = [i for i in status.keys()]
    return res






l = [1,2,3,4,5,4,3,2,1]
t = xor(l)
print(t)
res = odd(l)
print(res)