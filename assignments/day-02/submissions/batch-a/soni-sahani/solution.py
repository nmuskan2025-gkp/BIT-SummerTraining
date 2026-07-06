#assignment_2

#Question 1
#Write a program to check whether a number is positive, negative, or zero.
num = float(input("Enter your number:"))
if num > 0:
    print("Given number is positive")
elif num < 0:
    print("Given number is negative")
else:
    print("Given number is zero")        


#Question 2
#Write a program to check whether a number is even or odd.
num = int(input("Enter your number:"))
if num % 2 ==0:
    print("Given number is even")
else:
    print("Given number is odd")


#Question 3
#Create a list of 10 numbers and print each number using a loop.
numbers= [45, 56, 90, 12, 50, 23, 35, 19, 30, 49]
for num in numbers:
    print(num)


#Question 4
#Write a function named calculate_average that takes 3 marks and returns the average.
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average
#Exampale
result = calculate_average(85, 90, 95)
print("Average:", result) 
# Output: Average: 90.0

#Question 5
#Write a function named grade_student that prints a grade based on marks.
def grade_student(marks):
    if marks >= 90:
        print("grade: A")
    elif marks >= 75:
        print("grade: B")
    elif marks >= 60:
        print("grade: C")
    elif marks >= 40:
        print("grade: D")
    else:
        print("grade: F")

#Exampale
grade_student(67)
