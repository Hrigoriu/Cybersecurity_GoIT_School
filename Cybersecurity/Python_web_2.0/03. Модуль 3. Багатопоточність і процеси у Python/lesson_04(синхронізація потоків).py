    #! Condition !
#==============================================================================================
from threading import Thread, Condition
import logging
from time import sleep


def worker(condition: Condition):
    logging.debug('Worker ready to work')
    with condition:
        condition.wait()
        logging.debug('The worker can do the work')


def master(condition: Condition):
    logging.debug('Master doing some work')
    sleep(2)
    with condition:
        logging.debug('Informing that workers can do the work')
        condition.notify_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    condition = Condition()
    master = Thread(name='master', target=master, args=(condition,))

    worker_one = Thread(name='worker_one', target=worker, args=(condition, ))
    worker_two = Thread(name='worker_two', target=worker, args=(condition,))
    worker_one.start()
    worker_two.start()
    master.start()

    logging.debug('End program')

"""
worker_one Worker ready to work
worker_two Worker ready to work
master Master doing some work
MainThread End program
master Informing that workers can do the work
worker_one The worker can do the work
worker_two The worker can do the work
"""
#==============================================================================================
    #! Event !
#==============================================================================================
from threading import Thread, Event
import logging
from time import sleep


def worker(event: Event):
    logging.debug('Worker ready to work')
    event.wait()
    logging.debug('The worker can do the work')


def master(event: Event):
    logging.debug('Master doing some work')
    sleep(2)
    logging.debug('Informing that workers can do the work')
    event.set()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    master = Thread(name='master', target=master, args=(event, ))

    worker_one = Thread(name='worker_one', target=worker, args=(event, ))
    worker_two = Thread(name='worker_two', target=worker, args=(event,))
    worker_one.start()
    worker_two.start()
    master.start()

    logging.debug('End program')

"""
worker_one Worker ready to work
worker_two Worker ready to work
master Master doing some work
MainThread End program
master Informing that workers can do the work
worker_two The worker can do the work
worker_one The worker can do the work
"""
#==============================================================================================
from threading import Thread, Event
import logging
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        logging.debug('Run event work')

        if event_for_exit.is_set():
            break


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    thread = Thread(target=example_work, args=(event,))
    thread.start()

    sleep(5)
    event.set()

    logging.debug('End program')
"""
Thread-1 (example_work) Run event work
Thread-1 (example_work) Run event work
Thread-1 (example_work) Run event work
Thread-1 (example_work) Run event work
MainThread End program
Thread-1 (example_work) Run event work
"""
#==============================================================================================
    #! Barrier !
#==============================================================================================
from random import randint
from threading import Thread, Barrier
import logging
from time import sleep, ctime


def worker(barrier: Barrier):
    logging.debug(f'Start thread: {ctime()}')
    sleep(randint(1, 3))  # Simulate some work
    r = barrier.wait()
    logging.debug(f'count: {r}')
    logging.debug(f'Barrier overcome: {ctime()}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    barrier = Barrier(5)

    for num in range(10):
        thread = Thread(name=f'Th-{num}', target=worker, args=(barrier, ))
        thread.start()

"""
Th-0 Start thread: Fri Feb 13 18:07:53 2026
Th-1 Start thread: Fri Feb 13 18:07:53 2026
Th-2 Start thread: Fri Feb 13 18:07:53 2026
Th-3 Start thread: Fri Feb 13 18:07:53 2026
Th-4 Start thread: Fri Feb 13 18:07:53 2026
Th-5 Start thread: Fri Feb 13 18:07:53 2026
Th-6 Start thread: Fri Feb 13 18:07:53 2026
Th-7 Start thread: Fri Feb 13 18:07:53 2026
Th-8 Start thread: Fri Feb 13 18:07:53 2026
Th-9 Start thread: Fri Feb 13 18:07:53 2026
Th-9 count: 4
Th-5 count: 0
Th-2 count: 2
Th-1 count: 3
Th-6 count: 1
Th-9 Barrier overcome: Fri Feb 13 18:07:55 2026
Th-5 Barrier overcome: Fri Feb 13 18:07:55 2026
Th-2 Barrier overcome: Fri Feb 13 18:07:55 2026
Th-1 Barrier overcome: Fri Feb 13 18:07:55 2026
Th-6 Barrier overcome: Fri Feb 13 18:07:55 2026
Th-7 count: 4
Th-7 Barrier overcome: Fri Feb 13 18:07:56 2026
Th-0 count: 0
Th-4 count: 1
Th-4 Barrier overcome: Fri Feb 13 18:07:56 2026
Th-3 count: 2
Th-3 Barrier overcome: Fri Feb 13 18:07:56 2026
Th-8 count: 3
Th-0 Barrier overcome: Fri Feb 13 18:07:56 2026
Th-8 Barrier overcome: Fri Feb 13 18:07:56 2026
"""
#==============================================================================================
