'''Create a Decorator to Log Calls
Create a decorator called log_function_call that prints function name and when it was called.
Apply it to a function like add().
'''
def log_function_calls(func):
    def wrapper (a,b):
        print(f"\nFunction {func.__name__} is called .\n") 
        func(a,b)
    return wrapper

@log_function_calls
def add(a,b):
    print(f"Answer : {a+b}")

a= int(input("first number :    "))
b= int(input("second number :    "))

add(a,b)
        
        