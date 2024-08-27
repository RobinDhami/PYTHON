class Generator:
    def prac(self):
        for i in range(5):
            yield i 

gen = Generator()
val=gen.prac()
# Iterate over the generator and print the yielded values
for value in val:
    print(f'Yielded value: {value}')

