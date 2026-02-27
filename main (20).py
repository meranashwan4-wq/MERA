from pydantic import BaseModel, Field, field_validator
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

class StudentCreate(BaseModel):  # input
    name: str
    email: EmailStr | None = None
    age: int = Field(ge=18, le=60)
    phone: PhoneNumber | None = None
    major_id: int

    # THE FIX: Intercept and clean the phone number before validation
    @field_validator('phone', mode='before')
    @classmethod
    def format_phone(cls, value: str) -> str:
        if isinstance(value, str) and value.startswith('00'):
            # Replace the first two characters ('00') with a '+'
            return '+' + value[2:]
        return value


class StudentUpdate(BaseModel):
    name: str | None = Field(min_length=3)
    age: int  | None = Field(ge=18, le=60)
    phone: PhoneNumber | None = None
    major_id: int  | None = None
    email: EmailStr | None = None

class StudentRead(BaseModel):
    student_id: int
    name: str
    age: int
    major_id: int
    email: EmailStr | None
    phone: PhoneNumber | None

    model_config = {"from_attributes": True}
