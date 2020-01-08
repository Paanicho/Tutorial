def greetings(name) :
    print ("Hello " + name )

# a python object
def John():
    person = {
      "name": "John",
      "age": 30,
      "married": True,
      "divorced": False,
      "children": ("Ann","Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }
    return person

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#A function returning a lambda function
def myfunc(n):
  return lambda a : a * n

