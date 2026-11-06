#-----------------------------[ Nov. 06, 2026 ]-----------------------------------

#In python, its allowed to create combined objects
student = {
    "name": "Meena",
    "age": 22,
    "subjects": ["Python", "SQL"],
    "marks": (85, 91),
    "certificates": {"Python", "Cloud"},

print(student)

#Type conversion
#1. Implicit type conversion
#2. Explicit type conversion

number_text = "100"
#number = int(number_text)
scores = tuple([80, 90, 95])
unique_scores = set(scores)
print(number + 50)
print(scores, unique_scores)

#Way to define or create a set 
s = {"Python", "Cloud"}
print(type(s))
