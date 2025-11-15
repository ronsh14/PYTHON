contact_info = {
    "alice": "555-123",
    "bob": "234-123"
}

alice_phone =contact_info["alice"]
print(alice_phone)

contact_info["alice"] = "123-456"
print(contact_info)

contact_info["eva"] = "345-345"
print(contact_info)

del contact_info["bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {
    "alice" : {
        "phone_number" : "123-555",
        "email" : "alice@gmail.com",
        "birthday" : "20/11/2000"
    } ,

"bob" : {
        "phone_number" : "845-555",
        "email" : "bob@gmail.com",
        "birthday" : "27/11/2005"
    }

}

print(contact_information)
print(contact_information["bob"])