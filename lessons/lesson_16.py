# recurssion lesson! 

# recursion is when a function calls itself 

def f(): 
    print("hello") 
    f() # this is a recursive call


# recursion must have a exit condition so it doesn't go on forever

def f(n):
    if n == 0:
        return
    print("hello")
    f(n-1)



# recursion is a good way to solve problems that can be broken down into smaller problems


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))



def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(40))



def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

print(sum_digits(22222))



# recursion is when a function calls itself 
# recursion must have a exit condition so it doesn't go on forever
# recursion is a good way to solve problems that can be broken down into smaller problems
    
def fq(n):
    if(n == -1):
        return
    fq(n-1)
    print(n)
    
fq(100)