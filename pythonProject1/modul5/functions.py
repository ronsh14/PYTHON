def greet():
    print("hello world")

greet()

def greet_person(name):
    print("hello,", name)

greet_person("emily")
greet_person("alice")


'''
def add(x,y):
     z=x+y
     return z
     
add(3,7)
'''


def add(x,y):
    z=x+y
    return z

result = add(3,7)

print("the result of 3+7 =", result)