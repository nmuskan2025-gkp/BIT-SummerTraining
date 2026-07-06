#assigment-4
#Question 1: List Append(Create a list of 5 student names. Add one new student name to the list and print the final list.)
# Expected Output:['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']
student_name = ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
student_name.append('vivek')
print(student_name)

#Question 2:Tuple Indexing(Create a tuple of 5 city names and print the third city.)
#Expected Output:Delhi
city_name = ("Mumbai","lucknow","Delhi","Kolkata","chennai",)
print(city_name[2])



#Question 3:Set Add(Create a set of 4 course names. Add "AI" to the set and print the sorted list of courses.)
#Expected Output:['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']
courses = {"Python","SQL","Machine Learning","Data Analytics"}
courses.add("AI")
print(sorted(courses))



#Question 4:Dictionary Access(Create a dictionary with keys name, course, batch, and city. Print the student's name and course.)
# Expected Output:
# Name: Rahul 
# Course: Python Data AI
student_Detaile ={
    "name" :"Soni",
    "course": "B.Tech(ECE) ",
    "city" :"Gorakhpur",
    "batch": "A"
}





#Question 5:Filter Even Numbers(Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.)
# Expected Output:[2, 4, 6, 8, 10]



#Question 6:Count Word Frequency(Create a list of words)
#words = ["python", "ai", "python", "data", "ai", "python"]
#Use a dictionary to count how many times each word appears and print the dictionary.
# Expected Output:{'python': 3, 'ai': 2, 'data': 1}




#Question 7:Nested Student Dictionary(Create a nested dictionary for one student with name, marks, and skills. Add one new skill "Pandas" and print the updated dictionary.)
#Expected Output:{'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}




#Question 8:Common Elements(Create two sets)
#python_students = {"Aman", "Priya", "Raj", "Neha"}
#ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
#Find the common students and print them as a sorted list.
#Expected Output:['Neha', 'Raj']