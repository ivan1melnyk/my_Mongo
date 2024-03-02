from mongoengine import connect, Document, ListField, StringField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=100)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author)
    quote = StringField()
