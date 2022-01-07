from mongoengine import Document, StringField, DateTimeField, DictField


class Contact(Document):
    _id = StringField()
    iban = StringField()
    name = StringField()
    organization = StringField()

    meta = {
        "indexes": ["name", "organization"]
    }


class Invoice(Document):
    _id = StringField()
    organization = StringField()
    createdAt = DateTimeField()
    updatedAt = DateTimeField()
    amount = DictField()
    contact = DictField()
    invoiceDate = DateTimeField()
    invoiceId = StringField()
