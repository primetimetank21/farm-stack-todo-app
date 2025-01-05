from pydantic import BaseModel, Field, field_serializer, ConfigDict
from bson import ObjectId


class Todo(BaseModel):
    id: ObjectId = Field(alias="_id")
    title: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1, max_length=250)
    is_completed: bool = Field(default=False)

    @field_serializer("id")
    @classmethod
    def serialize_id(cls, value: ObjectId) -> str:
        print(f"{type(value)=}")
        # print(f"{ObjectId(value)=}")
        return str(value)

    model_config = ConfigDict(arbitrary_types_allowed=True)


class TodoPost(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1, max_length=250)
    is_completed: bool = Field(default=False)
