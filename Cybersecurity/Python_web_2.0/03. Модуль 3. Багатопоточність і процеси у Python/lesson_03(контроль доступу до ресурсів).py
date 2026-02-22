#! Блокування Lock та RLock !
# ==============================================================================================
"""
Lock це коли у кожного потоку один і той самий ключ і будь-який потік може відкрити замок, хто б його не закрив із потоків.
З RLock ситуація трохи інша, у кожного потоку свій ключ і свій замок.
"""
# ==============================================================================================
from threading import Thread, RLock
import logging
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    locker.acquire()
    sleep(delay)
    locker.release()
    logging.debug(f"Done {time() - timer}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))
    t1.start()
    t2.start()
    logging.debug("Started")
    t1.join()
    t2.join()
    logging.debug("End")

"""
MainThread Started
Thread-1 (func) Done 2.000440835952759
Thread-2 (func) Done 3.9962124824523926
MainThread End
"""
# ==============================================================================================
from threading import Thread, RLock
import logging
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    with locker:
        sleep(delay)
    logging.debug(f"Done {time() - timer}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))
    t1.start()
    t2.start()
    logging.debug("Started")
    t1.join()
    t2.join()
    logging.debug("End")

"""
MainThread Started
Thread-1 (func) Done 2.001513957977295
Thread-2 (func) Done 4.008785247802734
MainThread End
"""
# ==============================================================================================
#! Семафор !
# блокує кількість потоків, до кількості, що вказано
# ==============================================================================================
from threading import Semaphore, Thread
import logging
from time import sleep


def worker(condition):
    with condition:
        logging.debug(f"Got semaphore")
        sleep(1)
        logging.debug(f"finished")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    pool = Semaphore(2)
    for num in range(10):
        thread = Thread(name=f"Th-{num}", target=worker, args=(pool,))
        thread.start()
"""
Th-0 Got semaphore
Th-1 Got semaphore
Th-0 finished
Th-2 Got semaphore
Th-1 finished
Th-3 Got semaphore
Th-2 finished
Th-4 Got semaphore
Th-3 finished
Th-5 Got semaphore
Th-5 finished
Th-4 finished
Th-6 Got semaphore
Th-7 Got semaphore
Th-6 finished
Th-7 finished
Th-8 Got semaphore
Th-9 Got semaphore
Th-8 finished
Th-9 finished
"""
# ==============================================================================================
