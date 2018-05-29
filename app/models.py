from . import db


# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return '<Role %r>' % self.name


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pwd = db.Column(db.String(30))

    def _init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        '''

            真实用户return Flase

        '''
        return False
