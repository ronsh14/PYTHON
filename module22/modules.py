from pydantic import BaseModel,constr,conint,FieldValidationInfo,field_validator

class User(BaseModel):
   id: int
   name: str
   age: int

   @field_validator('age')
   def age_must_be_pocitive(cls,v,info):
      if v <=0:
        raise ValueError("Age must be positive")
      return v


try:
    user = User(id=1,name="John",age=5)

except ValueError as e:
    print(e)