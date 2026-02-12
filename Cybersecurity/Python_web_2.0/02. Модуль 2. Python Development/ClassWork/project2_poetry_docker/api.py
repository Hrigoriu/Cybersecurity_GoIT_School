import os

print(os.getenv("HELLO"))
if os.getenv("WORLD"):
    print("Hello, World!")