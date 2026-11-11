#----------------------[ Nov. 11, 2026 ]-------------------------

#Iteration, Iterators - doing a task continously until a specific sitaution to be met
#1. Basic for loop body
courses = ["Python", "SQL", "Excel", "Java"]
for i in courses: #no data-type needed varible, no initialization, (auto-increment - its dedicatedly only for FOR loop)
    print(i)

#2. Range function
for i in range(2,60,2): #range functionality - start,end,jump - is any parameter mandatory (yes, end is mand.)
    print(i)

#3. While loop
count = 1
while count <= 5:
    print(count)
    count +=1
  

#4. Break statement
for numb in range(1,11):
    if numb == 6:
        break
    print(numb)

#5. Continue statement
for i in range(1,11):
    if i % 2 == 0:
        #print("I found a even number", i)
        continue
    print(i)

#6. Nested loops
for row in range(1,5):
    for column in range(1,5):
        print(row, column)
for int i = 1, i++, i<10

#7. Enumerate
li = ["Akash", "Ravi", "Raghav", "Navya", "Kunal", "Kritika"]
score = [20,30,45,52,46,27]
for position,name in enumerate(li, start=1):
    print(position, name)

#8. Zip function
li = ["Akash", "Ravi", "Raghav", "Navya", "Kunal", "Kritika"]
scores = [20,30,45,52,24,53,48]
for name, score in zip(li, scores):
    print(name, score)
