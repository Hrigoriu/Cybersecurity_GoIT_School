from multiprocessing import Process, Manager, current_process
from random import randint
from time import sleep
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(delay, val: Manager):
    name = current_process().name
    logger.debug(f'Started: {name}')
    sleep(delay)
    val[name] = current_process().pid
    logger.debug(f'Done: {name}')


if __name__ == '__main__':
    with Manager() as manager:
        m = manager.dict()
        processes = []
        for i in range(5):
            pr = Process(target=worker, args=(randint(1, 3), m))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(m)

"""
Started: Process-6
Started: Process-3
Started: Process-2
Started: Process-4
Started: Process-5
Done: Process-3
Done: Process-2
Done: Process-4
Done: Process-6
Done: Process-5
{'Process-3': 38448, 'Process-2': 18324, 'Process-4': 13368, 'Process-6': 5780, 'Process-5': 33160}
"""
#==============================================================================================
