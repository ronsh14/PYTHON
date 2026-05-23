from pydantic import BaseModel,conint,constr

#class User(BaseModel):
#    id: int
#    name: str
#    age: int
#    email: str


# user = User(id=1,name="John Doe", age=20,email='johndoe@gmail.com')
# print(user)

class User(BaseModel):
   id: int
   name: str
   age: int = 0
   email: str = "noemail@example.com"

user1 = User(id=2,name="John")
print(user1)

user2 = User(id=3,name="Alice",age=25)
print(user2)


class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2,max_length=50)


valid_user = another_user(id=1,name="Ron")
print(valid_user)



