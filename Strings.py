#   Note:: All Strings method return new value they dont change the original value
sentence = " I love to watch anime.My favourite anime is Tensura. And i love Diablo "
sentence=sentence.upper().strip()
print(sentence.lower())

#It is not working right now cause we have converted sentence into uppercase and store it into sentence so we need to use uppercase while replaing items
sentence=sentence.replace("Diablo","Benimaru") 
print(sentence)

#concate strings
a= "hello"
b= "world"
sum = a+" "+b
print(sum)

#Use f for string to use with int
n=100
Adress= f"kaalanki {n}"
print(Adress)
