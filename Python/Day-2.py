#-------------------------------{Day - 2 [Nov. 3, 2026]}-----------------------------------------

#String and its methods

name = 'Pyhton programming'
msg = "Welcome to " + name #concatination 
name3 = msg + name
multiline_str = """Pyhton
programming 
is
very
useful
"""
print(type(name))
print(msg)
print(name3)
print(multiline_str)
print(type(name))
print(id(name))

#String and its methods

text = '          Python Prograamming   Is    Very   Useful    '
print(text.strip())
print(text.upper())
print(text.lower())
print(text.strip().title())
print(text.replace('Python', 'Java'))
print(text.split())
print(text.split('a'))

#Removing spaces and changing letter case
raw_text = '          Python Programming   Is    Very   Useful    '
clean_text = raw_text.strip()
print("Strip:- ", clean_text)
print("Lower:- ", clean_text.lower())
print("Upper:- ", clean_text.upper())
print("Title:- ", clean_text.title())
print("Capitalize:- ", clean_text.capitalize())
print("Swap case:- ", clean_text.swapcase())

#Searching and checking string content
string = "The quick brown foxy fOx"
print("Find the word:- ", string.find('rat')) #it looks for whole
string and sub-string too
print("Find the word:- ", string.find('fox')) #it looks for whole
string and sub-string too, and gives the index for the 1st occurance
print("Count of character:- ", string.lower().count("o"))
print("Starts with:- ", string.lower().startswith("python"))
print("Ends with:- ", string.endswith("Analysis"))
print("Is the word in uppercase? :- ", "quick".isupper())
print("------------------------------------------------------------------------------------------")
print("Starts with:- ", string.lower().startswith("the"))
print("Ends with:- ", string.lower().endswith("fox"))
print("Is the word in uppercase? :- ", "DATA".isupper())

