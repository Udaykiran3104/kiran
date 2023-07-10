
def add(x,y):
    sum=a+b
    print(f"sum is:",sum)
    return sum

a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
add(a,b)

# def power(x,y):
  
#     result=a**b
#     print(f"power of given number is:",result)

#     return result

# a=int(input("enter the number:"))
# b=int(input("enter the power:"))
# power(a,b)

# n = int(input("Enter a number: "))

# print("Multiplication table for", n)
# for i in range(1, 11):
#     product = n * i
#     print(n, "x", i, "=", product)

# print("hello world")

# def concatenate_strings(a, b):
#     return a + b
# result = concatenate_strings("uday, ", "kiran")
# print(result)  

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"

# num1 =int(input("enter the 1st number:"))
# num2 =int(input("enter the 2st number:"))

# print("Addition:", add(num1, num2))
# print("Subtraction:", subtract(num1, num2))
# print("Multiplication:", multiply(num1, num2))
# print("Division:", divide(num1, num2))

# class Student:
#     srn=0
#     name=""
#     section=""


#     def __init__(self,srn,name,section):
#         self.srn = srn
#         self.name = name
#         self.section = section

# s=Student(20,"uday","c")

# print(s.srn)
# print(s.name)
# print(s.section)

# class Student:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# u=Student("uday",18,"male")
# u.info()

# class Student:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def info(self):
#         print(self.name,self.age,self.gender)
       
# students=[("student1",18,"male"),("student2",19,"male"),("student3",21,"female")]
# stu_list=[]
# for stu,age,gender in students:
#     student=Student(stu,age,gender)
#     stu_list.append(student)
# for student in stu_list:
#     student.info()

# class Student:
#     college_name="reva"
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
# # instance 
#     def info(self):
#        marks=[1,2,3,4,5]
#        self.college()
#        print(f"name:{self.name} | age:{self.age} | gender:{self.gender}")
#        self.total_marks(marks)

# # class
#     @classmethod
#     def college(cls):
#         print(f"college:{cls.college_name}")

# # static
#     @staticmethod
#     def total_marks(marks_list):
#         total=0
#         for mark in marks_list:
#             total=total +mark
#         print(f"totak marks:{total}")
#         return total
    
# ram= Student("ram",18,"male")
# ram.info()
# students_list = [("StudentM1", 19, "Male"), ("StudentF1", 20, "Female")]

# students = []
# for name, age, gender in students_list:
#   s = Student(name, age, gender)
#   students.append(s)
# s.info()



    
