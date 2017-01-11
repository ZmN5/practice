def quicksort(array):
    smaller=[];larger=[]
    if len(array)<1:
        return array
    pv=array.pop()
    for num in array:
        if num>pv:
            larger.append(num)
        else:
            smaller.append(num)
    return quicksort(smaller)+[pv]+quicksort(larger)

if __name__=='__main__':
    numarray=[5,4,3,6,7,2,9,1,2,9]
    numarray=quicksort(numarray)
    sarray=['hahahahah','heheheheh','abc','every dog has its lucky day']
    sarray=quicksort(sarray)
    print(numarray,'\n',sarray)