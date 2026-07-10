# Dictionary

student = {
    "name": "Vishal",
    "age": 21,
    "city": "Mumbai",
    "marks": 96.48,
    "passed": True,
    "skills": ["Java", "Python", "Node.js"]
}

# if else with dictionary
if "city" in student:
    print("Key Found ✅")
    print(student["city"])
else :
    print("Key Not Found ❌") 

# for value in student.values():
    # print(value)

# for key, value in student.items():
#     print(key, " : ", value)

# second type to create a dictionary
# student = {}
# student = dict(
#     name = "Vishal",
#     age = 21
# )

# student["gender"] = "male"
# student["age"] = 22

# print(student["skills"])
# print(student["skills"][1])

# print(type(student))
# print(student["name"])
# print(student)

# students = {
#     "Student1" : {
#         "name": "Vishal",
#         "age": 21
#     },
#     "Student2" : {
#         "name": "Aryan",
#         "age": 12
#     }
# }

# print(students["Student2"]["name"])