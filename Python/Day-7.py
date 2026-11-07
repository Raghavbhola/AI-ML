#---------------------------------[ Nov. 07, 2026 ]--------------------------------------------

#Way to define or create a set - set is always unordered and allow unique in nature
# s1 = {"Python", "Cloud", "Asha", "sizuka", "Ravi"}
# s2 = {"Ravi", "Meena", "John", "Cloud", "sizuka"}
# print(type(s1))

#Operations of a set
s1 = {"Python", "Cloud", "Asha", "sizuka", "Ravi"}
print(s1)
s2 = {"Ravi", "Meena", "John", "Cloud", "sizuka"}
print("Both elements:- ", s1.intersection(s2)) #Print comman elements
print("All objects:- ", s1.union(s2)) #Print unique element from both set
print("Only diffrent elements:-",s2.difference(s1)) #non-comman element from one set
print(s1)
s1.add("Divya") #to insert single element
s2.update(["Anil", "Akash", "Sara"]) #to insert multiple elements
print("After addition:- ", s1)
print("After update:- ", s2)

print("Symmetric difference:- ", s1.symmetric_difference(s2)) #unique elements from both the sets
#Subset - set of elements derive from base set
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print("After intersection update:- ", s1_copy) #Subset from existing set
s2.discard("Meena")
print("After discarding the element:- ", s2)
s2.remove("sizuka")
print("After remove:- ", s2)
print(s2)
s2.pop()
print("After pop operation", s2)

req_skills = {"Python", "SQL", "Java"}
cand_skills = {"Python", "SQL", "Excel"}
print("Is subset:- ", req_skills.issubset(cand_skills))
print("Is superset:- ", cand_skills.issuperset(req_skills))
print("Is disjoint:- ", {"Java"}.isdisjoint(req_skills))
