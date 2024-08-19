a = "Hello my name is rabin Dhami.I am a boy"

if "rabin"  in a:
    print("Rabin present")

#Check for Palindrome    

word = "..........Damad,"
word = word.lower().replace(" ","").replace(",","").replace(".","")
palin = word[::-1]

if(word==palin):
    print("It is a palindrome")

