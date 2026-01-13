import sys
import os

print(sys.modules["os"])

#=========================================================================================
import sys
import os

print(sys.modules.keys())

#=========================================================================================
import sys
import os

print(sys.builtin_module_names)

#=========================================================================================
#echo.py
import sys

for arg in sys.argv:
    print(arg)
# Command to run the script:  python echo.py test - -user - hello some text 
"""
echo.py
test
--user
-hello
some
text

"""
#=========================================================================================
# arg.py
import sys

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])


if __name__ == "__main__":
    main()
# Command to run the script:  # python arg.py 123

#=========================================================================================

