greeting = "hello"
name = "bob"

def greet():
    global greeting
    name = "alice"

    message = f"{greeting}, {name}!"
    print(message)

greet()

print(greeting)

print(name)
