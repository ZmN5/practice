from threading import Thread
from time import ctime, sleep

loops = [4, 2]


class mythread(Thread):
    def __init__(self, func, args, name=''):
        Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.name = name

    def run(self):          #注意不是__call__(self)
        self.func(self.args)


def loop(nloop, nsec):
    print('loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop ', nloop, 'end at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []

    for i in range(len(loops)):
        t = mythread(loop,(i,loops[i]))
        threads.append(t)

    for i in range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print('end at:', ctime())

if __name__ == '__main__':
    main()