from atexit import register
from time import ctime, sleep
from threading import Thread, Lock, BoundedSemaphore
from random import randrange

lock = Lock()
MAX = 5                             #信号量大小
candytray = BoundedSemaphore(MAX)


def refull():
    with lock:
        print('refulling...')
        try:
            candytray.release()
        except ValueError:
            print('Is Full!')
        else:
            print('OK')

def buy():
    with lock:
        print('buying...')
        if candytray.acquire(False):    #加入False参数，如果信号量为空，则不阻塞，而是返回错误，
            print('OK')
        else:
            print('empty')

def consumer(loops):
    for i in range(loops):
        refull()
        sleep(randrange(3))             #睡眠时间尽量长于creater的概率尽量大，


def creater(loops):
    for i in range(loops):
        buy()
        sleep(randrange(5))


def main():
    print('starting...')
    n = randrange(2,6)
    print('the candy mechine full with {0}'.format(MAX))
    Thread(target=creater,args=(randrange(n,n+MAX+2),)).start()
    Thread(target=consumer, args=(randrange(n,n+MAX+2),)).start()


@register
def atexitt():
    print('The end!')


if __name__ == '__main__':
    main()




