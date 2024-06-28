# person = {"name":"rabin","age":32}
# salary = {"hr":"10k","labour":"20k"}
# for word in zip(person,salary):
#     print(word)

# def anagram(s1,s2):
#     a1= sorted(s1)
#     a2=sorted(s2)

#     if a1==a2:
#         return True
# def main():
#     anagram("silent","listen")  
#     if(anagram):
#         print("Its a angram ")  
#     else:
#         print("not")  
#     

# no commit today

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the smallest and only even prime number
    if n % 2 == 0:
        return False  # even numbers greater than 2 are not prime
    
    # Check divisibility from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def main():
    n = int(input("Enter a number: "))
    res = is_prime(n)
    if res:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

if __name__ == "__main__":
    main()
