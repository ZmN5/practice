class leak(object):
    def __init__(self):
        print("object with {0} was born".format(id(self)))

while(True):
    A = leak()
    B = leak()
    A.b = B
    B.a = A
    A = None
    B = None