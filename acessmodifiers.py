class Apple:
    def __init__(self) -> None:
        self.__name = "Rabin"  # By default, this is a public variable

a = Apple()
print(a._Apple__name)  # This will print: Rabin

print(dir(a))  # This will print the list of attributes and methods of the object `a`
