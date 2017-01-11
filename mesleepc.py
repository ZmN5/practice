from threading import Thread
from time import ctime, sleep

loops = [4, 2]


def loop(nloop, nsec):
    print('loops ', nloop, 'starting at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'end at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []

    for i in range(len(loops)):
        t = Thread(target=loop, args=(i,loops[i]))
        threads.append(t)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print('all done at:', ctime())

if __name__ == '__main__':
    main()