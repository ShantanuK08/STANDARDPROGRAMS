# Open file and print each line
for line in open("myfile.txt"):
    print(line, end="")

# Open file using 'with' statement
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

# Raising and Handling Multiple Unrelated Exceptions (Python 3.11+)

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

# Handling ExceptionGroup
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: {e}')

# Nested ExceptionGroup example
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

# Handling multiple exceptions in a group
try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
except* RecursionError as e:
    print("There were RecursionErrors")


def tests():
    excs = []
    for test in tests:
        
        try:
            test.run()
        except Exception as e:
            excs.append(e)

    if excs:
        raise ExceptionGroup("Test Failures", excs)
    





# Enriching Exceptions with Notes


try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise




