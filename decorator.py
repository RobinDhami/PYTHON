def sum(func):
    def wrapper(*args, **kwargs):
        print(f"This is {func.__name__} function")
        func(*args, **kwargs)  # Call the original function with arguments
    return wrapper

@sum
def hello(name):
    print(f"My first decorator {name}")

# Call the decorated function
hello("ram")
