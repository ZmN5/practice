class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesTwo:
    def __init__(self):
        self.value *= 2


class PlusFive:
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self,value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class AnotherWay(MyBaseClass,  PlusFive, TimesTwo):
    def __init__(self,value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print('OneWay (5*2)+5=', foo.value)
foo = AnotherWay(5)
print('AnotherWay:', foo.value)