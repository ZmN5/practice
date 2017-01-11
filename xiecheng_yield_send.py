def consumer():
    while True:
        line = yield
        print(line.upper())


def productor():
    with open('text.txt') as file:
        for i, line in enumerate(file):
            yield line
            print("{0} lines".format(i))


c = consumer()
c.__next__()
for i in productor():
    c.send(i)