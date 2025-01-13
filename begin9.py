# Errors and Exceptions


#syntax error

# while True print('Hello world'):

#Exceptions

# 10 * (1/0)

# 4 + spam*3

# '2' + 2

  

try:
    raise Exception('spam', 'eggs')  # Raise an exception with two arguments
except Exception as inst:
    print(type(inst))    # Print the exception type
    print(inst.args)     # Print the arguments stored in .args
    print(inst)          # Print the exception instance (__str__ is called)
    
    # Unpack args
    x, y = inst.args
    print('x =', x)
    print('y =', y)





import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise




for arg in sys.argv [1:]:
    try : 
        f = open (arg,'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()




def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)



#Raising Exceptions


# raise NameError('HiThere')

# raise value error



try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# Exception Chaining


