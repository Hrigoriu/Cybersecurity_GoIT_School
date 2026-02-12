"""
    ! Логування застосунку !
Щоб виправити помилки, потрібно знати, що саме відбувалося в застосунку і які дії призвели до виникнення помилок. 
Для цього потрібно записувати, зберігати стан застосунку в деякий журнал. 
Такий журнал для простоти називають log та механізм журналювання подій — логуванням (logging).
"""
#====================================================================================================
import logging

# print a log message to the console.
logging.warning('This is a warning!')
#WARNING:root:This is a warning!
#====================================================================================================
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ])
logging.warning('An example message.')
logging.warning('Another message')
"""
WARNING:root:An example message.
WARNING:root:Another message
And the same messages are also written to the file program.log.
"""
#====================================================================================================
import logging

# створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# створюємо форматтер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# додаємо зазначений форматтер до handler ch
ch.setFormatter(formatter)

# додаємо handler ch до логера
logger.addHandler(ch)

# Створюємо файловий handler для логера:
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)

# додаємо файловий handler fh до логера
logger.addHandler(fh)

# приклад виконання коду
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
"""
2026-02-06 22:08:30,850 - simple_example - DEBUG - debug message
2026-02-06 22:08:30,850 - simple_example - INFO - info message
2026-02-06 22:08:30,850 - simple_example - WARNING - warn message
2026-02-06 22:08:30,850 - simple_example - ERROR - error message
2026-02-06 22:08:30,850 - simple_example - CRITICAL - critical message

And the following messages are also written to the file app.log:
2026-02-06 22:08:30,850 - simple_example - ERROR - error message
2026-02-06 22:08:30,850 - simple_example - CRITICAL - critical message
"""
#====================================================================================================
