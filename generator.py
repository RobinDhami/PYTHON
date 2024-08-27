def prac():
    for i in range(20):
        yield i
        print(i)  # Print the current value of i

# Create a generator object
gen = prac()

# Iterate over the generator and print the yielded values
for value in gen:
    print(f'Yielded value: {value}')
