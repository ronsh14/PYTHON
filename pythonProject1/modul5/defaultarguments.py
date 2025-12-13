def greet_person(name, greeting="hello"):
    message = f"{greeting}, {name}"
    return message

default_greeting = greet_person("alice")

print(default_greeting)

custom_greeting = greet_person("bob", "hi")
print(custom_greeting)