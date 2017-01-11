def maxVal(w, v, i, ws):
    if i == 0:
        if w[i] <= ws:
            return v[i]
        else:
            return 0
    without_i = maxVal(w, v, i-1, ws)
    if w[i] > ws:
        return without_i
    else:
        with_i = maxVal(w, v, i-1, ws-w[i]) + v[i]
    return max(without_i, with_i)


w = [5, 3, 2]
v = [9, 7, 8]
val = maxVal(w, v, 2, 5)
print(val)