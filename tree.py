def sum(t):
    tmp=0
    for k in t:
        if not isinstance(k,list):
            tmp+=k
        else:
            tmp+=sum(k)
    return tmp
if __name__=='__main__':
    x=[1,[2,[3,4,5,[6,7,[8,9]]]]]
    t=sum(x)
    print(t)
