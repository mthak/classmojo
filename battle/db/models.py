from mongoengine import *

class Battle(Document):

    Developer_Issues = IntField(required=True)
    Issues_Resolved = IntField(max_length=50)
    Issues_Pending = IntField(max_length=50)
    Component_Issues = IntField()
    Component_Failures = ListField()
    Total_Tickets = IntField()
    Jiras = ListField()
    Faq_Updated = IntField()
    Date_Updated = DateTimeField()


