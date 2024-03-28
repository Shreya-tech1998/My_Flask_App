from . import db

class USERS(db.Model):
    __tablename__ = 'USERS'
    __table_args__ = {'schema': 'BULLFLIX'}
    USER_GUID = db.Column(db.String(1000), primary_key=True)  # primary keys are required by SQLAlchemy
    USER_NAME = db.Column(db.String(100))
    EMAIL  =    db.Column(db.String(100), unique=True)
    PIP_HASH =  db.Column(db.Integer, unique=True)
    FIRST_CREATED = db.Column(db.DateTime)
    LAST_UPDATED = db.Column(db.DateTime)
    RECO_LIMIT = db.Column(db.Integer)
    RECO_SUPPORT = db.Column(db.Integer)
    COSINE_NORM = db.Column(db.Integer)
    BIRTH_DECADE = db.Column(db.Integer)
    LAST_LOGIN =  db.Column(db.Date)
    LOGIN_DAYS = db.Column(db.Integer)
    


class TESTING123(db.Model):
    __tablename__ = 'TESTING123'
    __table_args__ = {'schema': 'BULLFLIX'}
    REC_ID = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    REC_NAME = db.Column(db.String(100), unique=True)

    
    def __repr__(self):
        return f'<TESTING123 {self.REC_NAME}>'
    