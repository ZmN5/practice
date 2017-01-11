memo={}
def maxVal(w, v, i, ws):
    try:
        return memo[(i,ws)]
    except KeyError:
        if i == 0:
            if w[i] <= ws:
                memo[(i, ws)] = v[i]
                return v[i]
            else:
                memo[(i, ws)] = 0
                return 0
        without_i = maxVal(w, v, i-1, ws)
        if w[i] > ws:
            memo[(i, ws)] = without_i
            return without_i
        else:
            with_i = maxVal(w, v, i-1, ws-w[i]) + v[i]
        res = max(without_i, with_i)
        memo[(i, ws)] = res
        return res

w = [5, 3, 2]
v = [9, 7, 8]
val = maxVal(w, v, 2, 5)
print(val)