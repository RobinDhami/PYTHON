primes = []  # this will contain the primes in the end
upto = 100  # the limit, inclusive
for n in range(2, upto + 1):
   for divisor in range(2, n):
      if n % divisor == 0:
         break
   else: 
      primes.append(n)
print(primes)


class Prime:
   def calc_prime(self,n):
      primes=[]
      for i in range(2,n+1):
         for x in range(2,i):
            if i%x==0:
               break
         else:
            primes.append(i)      
      return primes   

result = Prime()
x=result.calc_prime(100) 
print(x)                

# x = [1, 2, 3] #global 
# def func(x):
#    x[1] = 42  # this changes the caller!
#    x = 'something else'  # this points x to a new string object but is local cant access outside the func
# func(x)
# print(x)