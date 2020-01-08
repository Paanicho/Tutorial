import json
import re
import mypythonmodule as mpm

mpm.greetings("Jonathan")
mpm.greetings(mpm.person1["name"])

x = dir(mpm)
print(x)

#Convert from JSON to Python:
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convert Python to json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = mpm.John()

#Converted to a json string
y = json.dumps(x)
print(y)

#lambda functions
#myfunc returns a lambda function
mydoubler = mpm.myfunc(2)
mytrippler = mpm.myfunc(3)
print(mydoubler(11))
print(mytrippler(11))

txt = "The rain in Spain"

#searches for a match with line starting with 'The' and ending with 'Spain'
x = re.search("^The.*Spain$", txt)
print (x)

#searches for a word starting with 'S'
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())


#read all the lines in a file
f = open("demofile.txt", "r")
for x in f:
  print(x)

