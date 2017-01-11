import sys
def solution(array):
    second = -10000000
    st = []
    for num in array[::-1]:
        if num<second:
            return True
        elif st and num>st[-1]:
            second=st.pop()
        st.append(num)
    return False

if __name__=='__main__':
    s=[3,1,4,2]
    print(solution(s))

