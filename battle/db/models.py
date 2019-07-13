from mongoengine import *
from datetime import datetime

class Battle(Document):

    Developer_Issues = IntField(required=True)
    Issues_Resolved = IntField(max_length=50)
    Issues_Pending = IntField(max_length=50)
    Component_Issues = IntField()
    Component_Failures = ListField()
    Total_Tickets = IntField()
    Jiras = ListField()
    Faq_Updated = IntField()
    Date_Updated = DateTimeField(default=datetime.now)


class School(Document):
      Name = StringField(required=True)
      Address = StringField(required=True)
      Type = StringField()

class Teacher(Document):
      Name = StringField(required=True)
      Classes = ListField()
      Notes = StringField()
      School = StringField(required=True)
      Level = StringField()
      Schedule = DictField()

class Student(Document):
    Name = StringField(required=True)
    classroom = StringField()
    Age = StringField()
    Rollnumber = IntField()
    Id = StringField()
    Gender = StringField()
    Contact_number = IntField()
    Address = StringField()
    FeeStructure = StringField()
    Points_parent = IntField()
    Points_teacher = IntField()
    Score = IntField()

class Parent(Document):
    Name = StringField(required=True)
    child = StringField()
    Relationship = StringField()
    Age = StringField()
    Gender = StringField()
    Contact_number = IntField()
    preferred_contact = StringField()
    Address = StringField()

class Classroom(Document):
       Level = StringField()
       Id = StringField()
       TimeTable = DictField()

