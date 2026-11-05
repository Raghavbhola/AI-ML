#---------------------------------------[ Nov. 05, 2026]----------------------------------------------

#Dictionaries and its operation----->
{key:value} -> {UID_no:Name}
emp = {"code":"123", "name":"Shubham Tiwari A", "role":"Automation Engineer", "city":"Yamuna Nagar"} #key must be unique.
emp["city"] = "Yamuna Nagar"
print("Show details:- ",emp)
print("Show keys of dictionary:- ",emp.keys())
print("Show values of dict:- ",emp.values())
print("Show keys and values in single unit:- ",emp.items())
print(emp)
print("Show record and show default value if the record is not available:- ",emp.get("Salary","Not Available"))
emp.update({"city":"Bengaluru","active":True})
print("Show updated dictionary:- ", emp)
print(emp["dept"])
emp.setdefault("dept","AI and ML")
emp.setdefault("code","777")
print(emp["code"])
print("After setdefault() -> ", emp)
rem_item = emp.popitem()
print("Removed item is :- ", rem_item)
print(emp)

emp_copy = emp.copy()
emp.clear()
print("Copy of dictionary:- ",emp_copy)
print("After clear operation:- ", emp)

columns = ["Python", "Java", "SQL"]
default_score = dict.fromkeys(columns,100)
print("Fromkeys() perform:- ", default_score)
