primes = []  # this will contain the primes in the end
upto = 100  # the limit, inclusive
for n in range(2, upto + 1):
   is_prime = True  # flag, new at each iteration of outer for
   for divisor in range(2, n):
      if n % divisor == 0:
         is_prime = False
         break
   if is_prime:  # check on flag
         primes.append(n)
print(primes)



class prime:
   prime=[]
   def prime(n):
      for i in range(2,n+1):
         is_prime=True
         for x in range(2,n):
            if i%x==0:
               is_prime=False
               break
         if is_prime:
            prime.append(i)
   print(prime)                