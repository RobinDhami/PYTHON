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

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_marks(self):
        marks_input = input("Enter your marks obtained in English, Nepali, Science, Computer (separated by commas): ")
        self.marks = list(map(int, marks_input.split(",")))
    
    def calculate_average(self):
        if len(self.marks) > 0:
            average = sum(self.marks) / len(self.marks)
            return average
        else:
            return 0
    
    def display_info(self):
        average = self.calculate_average()
        print(f"Welcome Mr./Miss {self.name} from Grade {self.grade}")
        print(f"Your average marks are: {average:.2f}")

if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    student_grade = input("Enter the student's grade: ")
    
    student = Student(student_name, student_grade)
    
    # Get marks and display information
    student.get_marks()
    student.display_info()



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_marks(self):
        marks_input = input("Enter your marks obtained in English, Nepali, Science, Computer (separated by commas): ")
        self.marks = list(map(int, marks_input.split(",")))
    
    def calculate_average(self):
        if len(self.marks) > 0:
            average = sum(self.marks) / len(self.marks)
            return average
        else:
            return 0
    
    def display_info(self):
        average = self.calculate_average()
        print(f"Welcome Mr./Miss {self.name} from Grade {self.grade}")
        print(f"Your average marks are: {average:.2f}")

if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    student_grade = input("Enter the student's grade: ")
    
    student = Student(student_name, student_grade)
    
    # Get marks and display information
    student.get_marks()
    student.display_info()
