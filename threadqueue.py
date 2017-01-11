from random import randint
from threading import Thread
from queue import Queue
from time import sleep


def writeq(queue):
    print('starting put queue...')
    queue.put('hahaha', 1)
    print('size now', queue.qsize())


def readq(queue):
    print('starting get queue...')
    val = queue.get(1)
    print('consume from queu...size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeq(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readq(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]


def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in range(len(funcs)):
        t = Thread(target=funcs[i], args=(q, nloops))
        threads.append(t)

    for i in range(len(funcs)):
        threads[i].start()

    for i in range(len(funcs)):
        threads[i].join()

    print('all done')

if __name__ == '__main__':
    main()