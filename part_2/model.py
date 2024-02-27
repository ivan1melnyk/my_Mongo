from mongoengine import connect, Document, StringField, BooleanField


class Contact(Document):
    name = StringField(max_length=50)
    email = StringField(max_length=30)
    is_sent = BooleanField(default=False)
