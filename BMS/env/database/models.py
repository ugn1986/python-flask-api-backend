from .db import db


class User(db.Document):
    username = db.StringField(required=True, unique=True, min_length=6)
    password = db.StringField(required=True,min_length=6)
    address = db.StringField(required=True)
    state = db.StringField(required=True)
    country = db.StringField(required=True)
    emailAddress = db.EmailField(required=True)
    pan = db.StringField(required=True, min_length=6,max_length=10)
    contactNo = db.IntField(required=True,min_length=10,max_length=12)
    DOB = db.StringField(required=True)
    accountType = db.StringField(required=True)    
     

class Loan(db.Document):
    username=db.StringField(required=True)
    loan_type = db.StringField(required=True, min_length=3)
    loan_Amount = db.FloatField(required=True, min_length=4)
    date=db.StringField(required=True)
    rate_of_interest = db.IntField(required=True, min_length=1)
    duration_of_loan = db.IntField(required=True, min_length=1)