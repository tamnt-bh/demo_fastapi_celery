from typing import Any

from bson import ObjectId
from pydantic import BaseModel, ConfigDict
from pydantic_core import core_schema


class BaseEntity(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    @classmethod
    def from_mongo(cls, data: dict, id_str=False):
        if not data:
            return data
        id = data.pop("_id", None) if not id_str else str(data.pop("_id", None))
        return cls(**dict(data, id=id))


class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)
