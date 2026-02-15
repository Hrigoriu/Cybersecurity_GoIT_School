"""
    ! Global Interpreter Lock (GIL) !
Це коли Python має механізм, який примусово блокує виконання коду різними потоками одного Python процесу в один і той самий час.
*Тільки один потік всередині процесу Python виконується, всі інші (якщо такі є) знаходяться в режимі 'Sleep'.
*Операції, пов'язані з введенням/виведенням (системні виклики) не блокуються GIL, але не їх послідовність.
"""
#==============================================================================================

from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        sleep(2)
        logging.debug('Wake up!')
        logging.debug(f"args: {self.args}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(5):
        thread = MyThread(args=(f"Count thread - {i}",))
        thread.start()
    print('Usefull message')

"""
Usefull message
Thread-1 Wake up!
Thread-1 args: ('Count thread - 0',)
Thread-2 Wake up!
Thread-2 args: ('Count thread - 1',)
Thread-3 Wake up!
Thread-4 Wake up!
Thread-4 args: ('Count thread - 3',)
Thread-5 Wake up!
Thread-5 args: ('Count thread - 4',)
Thread-3 args: ('Count thread - 2',)
"""
#==============================================================================================
    #! Потік як функтор
# Через  метод __call__
#==============================================================================================
from threading import Thread
from time import sleep
import logging


class UsefulClass():
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(2)
    thread = Thread(target=t2)
    thread.start()
    print('Some stuff')
"""
Some stuff
Thread-1 Wake up!
"""
#==============================================================================================
    #! Потік у функції !
#==============================================================================================
from threading import Thread
from time import sleep
import logging


def example_work(delay):
    sleep(delay)
    logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
    print('Usefull message')
"""
Thread-1 (example_work) Wake up!
Usefull message
Thread-2 (example_work) Wake up!
Thread-3 (example_work) Wake up!
Thread-4 (example_work) Wake up!
Thread-5 (example_work) Wake up!
"""
#==============================================================================================
    #! Очікування виконання потоку !
#==============================================================================================
from threading import Thread
import logging
from time import sleep


def example_work(params):
    sleep(params)
    logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.debug('Start program')
    threads = []
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    logging.debug('End program')
"""
MainThread Start program
Thread-1 (example_work) Wake up!
Thread-2 (example_work) Wake up!
Thread-3 (example_work) Wake up!
Thread-4 (example_work) Wake up!
Thread-5 (example_work) Wake up!
MainThread End program
"""
#==============================================================================================
from threading import Thread
from time import sleep
import logging


class UsefulClass:
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(2)
    thread = Thread(target=t2)
    thread_locking = Thread(target=t2)

    thread.start()
    print(thread.is_alive(), thread_locking.is_alive())
    thread_locking.start()
    thread.join()
    thread_locking.join()
    print(thread.is_alive(), thread_locking.is_alive())
    print('After all...')
"""
True False
Thread-1 Wake up!
Thread-2 Wake up!
False False
After all...
"""
#==============================================================================================
    #! Потоки Timer !
#==============================================================================================
from threading import Timer
import logging
from time import sleep


def example_work():
    logging.debug('Start!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    first = Timer(0.5, example_work)
    first.name = 'First thread'
    second = Timer(0.7, example_work)
    second.name = 'Second thread'
    logging.debug('Start timers')
    first.start()
    second.start()
    sleep(0.6)
    second.cancel()

    logging.debug('End program')
"""
MainThread Start timers
First thread Start!
MainThread End program
"""
#==============================================================================================
