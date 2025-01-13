import fibo

print(fibo.fib(1000))


print(fibo.fib2(100))


print(fibo.__name__)




fib = fibo.fib
print(fib(1000))


#More on Modules


from fibo import fib, fib2
print(fib(500))





from fibo import *
print(fib(500))



from fibo import fib as fibonacci
a = fibonacci(500)
print(a)


# if __name__ == "__main__":
#     import sys
#     print(fib(int(sys.argv[1])))


import fibo  # Import the module

# Call the functions
fibo.fib(50)  # Prints the Fibonacci series up to 50
result = fibo.fib2(50)  # Returns the Fibonacci series up to 50
print(result)




import sys


print("Default sys.ps1:")


print("Default sys.ps2:")


sys.ps1 = 'C> '


print(sys.ps1)


import sys
sys.path.append('/ufs/guido/lib/python')





import fibo, sys
print(dir(fibo))


print(dir(sys))  


a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())


import builtins
print(dir(builtins))


__all__ = ["echo", "surround", "reverse"]

print(__all__)


__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'



print(__all__)

#Intra-package References

#import sound.effects.echo
#import sound.effects.surround
#from sound.effects import *

#from . import echo
#from .. import formats
#from ..filters import equalizer