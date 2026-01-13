import math

sin_pi = math.sin(math.pi)
#=========================================================================================
"""
Для того щоб викликати функцію з імпортованого пакету, потрібно вказати ім'я пакету і через крапку ім'я функції або константи в цьому пакеті. Цей синтаксис дуже схожий на виклик метода, ми робили так зі словниками та списками раніше.
"""
#=========================================================================================
from math import pi, sin

sin_pi = sin(pi)
#=========================================================================================
# mymodule.py
def say_hello(name):
    return f"Hello, {name}!"
#=========================================================================================
# main.py
import mymodule

print(mymodule.say_hello("World"))
#=========================================================================================
# main.py
from mymodule import say_hello

print(say_hello("World"))
#=========================================================================================
# main.py
from mymodule import say_hello as greeting

print(greeting("World"))
#=========================================================================================
#=========================================================================================
# main.py
from mymodule import say_hello as greeting

print(dir())
print(greeting("World"))

"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greeting']
Hello, World!
"""
#=========================================================================================
# mymodule.py
def say_hello(name):
    print(f'Hello, {name}')


print("You imported hello.py")
say_hello('user')

#=========================================================================================
# main.py
from mymodule import say_hello as greeting

print(greeting("World"))
"""
You imported hello.py
Hello user
Hello, World!
"""
#=========================================================================================
# mymodule.py
def say_hello(name):
    print(f'Hello, {name}')

if __name__ == '__main__':
    print("You imported hello.py")
    say_hello('user')

#=========================================================================================
# mymodule.py
def say_hello(name):
    print(f'Hello {name}')

def main():
    print("You imported hello.py")
    say_hello('user')


if __name__ == '__main__':
    main()
