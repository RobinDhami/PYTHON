squares = map(lambda n: n**2, range(10))
print(list(squares))

sq1 = list(
    filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10)))
 )

print(sq1)


