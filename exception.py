a = input(" Enter a number:")

try:
    for i in range(1,11):
        print(f"{a}*{i}={int(a)*int(i)}")

except Exception as e:
    print("Invalid Input")        

l=[1,2,3,4,5]

def func():
    try:
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except Exception as e:
        print(e)    
        return 0
    finally:   
        print("I am always executed")

func()

#Custom Error
a = input("Enter the value butween 5 and 9: ")

if (a == "quit"):
  print("ohk")
elif (int(a) < 5 or int(a) > 9):
  raise ValueError("The num should be between 5 and 9")

# Exception Type	Description
# SyntaxError	Raised when there is incorrect syntax in the code.
# IndentationError	A subclass of SyntaxError, raised for incorrect indentation.
# NameError	Raised when a local or global name is not found.
# TypeError	Raised when an operation or function is applied to an object of inappropriate type.
# ValueError	Raised when a function receives an argument of the right type but inappropriate value.
# IndexError	Raised when trying to access an element from a list or tuple using an invalid index.
# KeyError	Raised when a dictionary is accessed with a key that doesn’t exist.
# AttributeError	Raised when an attribute reference or assignment fails.
# ZeroDivisionError	Raised when a division or modulo operation is performed with zero as the divisor.
# FileNotFoundError	Raised when a file or directory is requested but doesn’t exist.
# IOError	Raised for I/O operation failures. Often replaced by OSError in Python 3.
# OSError	Raised for system-related errors, including file operations and resource allocation issues.
# RuntimeError	Raised for errors that don't fall into any of the other categories.
# ImportError	Raised when an imported module or object cannot be found. Often replaced by ModuleNotFoundError.
# ModuleNotFoundError	A subclass of ImportError, raised when a module could not be found.
# MemoryError	Raised when an operation runs out of memory.
# OverflowError	Raised when the result of an arithmetic operation is too large to be expressed within the data type.