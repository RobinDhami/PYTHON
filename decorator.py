# Define the decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is being called")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Function {func.__name__} has been called")
        return result
    return wrapper

# Apply the decorator to a function
@log_decorator
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Alice")
