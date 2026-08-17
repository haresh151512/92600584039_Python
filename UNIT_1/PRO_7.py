# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.
     Program to demonstrate dictionary methods and iteration

student = {
    "name": "HARESH",
    "age": 21,
    "course": "python"
}

print("Dictionary =", student)
print("Name =", student["name"])

student["age"] = 21
print("Updated age =", student["age"])

student["city"] = "Morbi"
print("After adding city =", student)

student.pop("course")
print("After removing course =", student)

print("\nIteration:")
for key in student:
    print(key, "=", student[key])