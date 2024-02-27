from mongoengine import connect, Document, ListField, StringField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=50)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField()
