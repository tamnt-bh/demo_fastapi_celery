from mongoengine import Document, StringField, EmailField


class UserModel(Document):
    email = EmailField(required=True, unique=True)
    fullname = StringField(required=True)
    password = StringField(required=True)

    @classmethod
    def from_mongo(cls, data: dict, id_str=False):
        if not data:
            return data
        id = data.pop("_id", None) if not id_str else str(data.pop("_id", None))
        if "_cls" in data:
            data.pop("_cls", None)
        return cls(**dict(data, id=id))

    meta = {
        "collection": "Users",
        "indexes": ["email"],
        "allow_inheritance": True,
        "index_cls": False,
    }
