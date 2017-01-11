from atexit import register
from time import sleep, ctime
from threading import currentThread, Thread, Lock
from random import randrange


class cleanOutput(list):
    def __str__(self):
        return ','.join(self)

loops = [randrange(2, 5) for x in range(randrange(3, 7))]
remaining = cleanOutput()
lock = Lock()


def loop(nsec):
    myname = currentThread().name
    with lock:
        remaining.append(myname)
        print('{0} starting at {1}'.format(myname, ctime()))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('{0} end at {1}'.format(myname, ctime()))
        print('remaining {0}'.format(remaining))


def main():
    for i in loops:
        Thread(target=loop, args=(i,)).start()


@register
def _atexit():
    print("end!")


if __name__ == '__main__':
    main()

