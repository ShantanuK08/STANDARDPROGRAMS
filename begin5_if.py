x = int(input("Please enter an integer: ")) # if Statements

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



words = ['cats','window','defenstrate']      #for Statements
for w in words:
    print(w,len(w))

users = {'Hans': 'active', 'lol': 'inactive', 'goat': 'active'} #Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':

# Strategy:  Create a new collection
        active_users = {}
        for user, status in users.items(): 
            if status == 'active':
                active_users[user] = status

                print(status)


for i in range(5):  #iterates over a sequence of no.s ,generates arithmatic progressions.
    print(i)  


print(list(range(5,10)))

print(list(range(0, 10, 3)))

print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i  in range(len(a)) :                #to iterate over the indices of a sequence you can combine range() and len()
    print(i,a[i])


    print(range(10))

    print(sum(range(4)))

 #break and continue Statements
for n  in range (2,10):            
    for x in range(2,n):   
        if n % x==0:                          #break statement breaks out the innermost enclosing for and while loop.
            print(f"{n} equals {x} * {n//x}")

print(range(10))




for num in range(2,10):
    if num % 2 == 0:    #continue statements continues with next iteration of loop
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")



#else Clauses on Loops


for n in range(2,10):
    for x in range (2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'prime minister')


            #in a for loop , the else clause is executed after the loop finishes its final iteration,that is , if no break occured.
            #In a while loop ,it’s executed after the loop’s condition becomes false.




#pass Statements

# while True:
#     pass        #pass statement does nothing , it can be used when a statement is required syntactically but the program requires no action.
#     print(True)


#match Statements

# a match statement takes an expression and compare its value to successive patterns given as one or more case blocks.
point = (100,50)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
  

