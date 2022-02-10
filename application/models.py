import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id         = db.IntField(unique=True)
    first_name      = db.StringField(max_length=50)
    last_name       = db.StringField(max_length=50)
    email           = db.StringField(max_length=30, unique=True)
    password        = db.StringField()

    #Setters and getters
    def set_password(self, password):
         self.password= generate_password_hash(password)

    def get_password(self, password):
         return check_password_hash(self.password, password)


class Course(db.Document):
    courseID=db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description =db.StringField(max_length=255)
    credits = db.IntField()
    term= db.StringField(max_length=25)

#Many to many relationship,query from both tables, need to have third table the junction table, join to query data back
#one student can enrol in many courses and many students belong to many courses 
class Enrollment(db.Document):
    user_id= db.IntField()#Use the one that is stored in the database
    courseID=db.StringField(max_length=10)

    

