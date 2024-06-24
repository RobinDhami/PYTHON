# person = {"name":"rabin","age":32}
# salary = {"hr":"10k","labour":"20k"}
# for word in zip(person,salary):
#     print(word)

def anagram(s1,s2):
    a1= sorted(s1)
    a2=sorted(s2)

    if a1==a2:
        return True
def main():
    anagram("silent","listen")  
    if(anagram):
        print("Its a angram ")  
    else:
        print("not")    

if __name__ == "__main__":
    main()