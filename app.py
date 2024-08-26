import logging
import os
from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
database = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database
db = SQLAlchemy(app)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.DEBUG)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 25, type=int)

    users = User.query.paginate(page=page, per_page=per_page)
    logger.info('%s users retreived from database as page %s', users.per_page, users.page)

    return jsonify({
        'users': [user.to_dict() for user in users.items],
        'total': users.total,
        'page': users.page,
        'per_page': users.per_page,
        'pages': users.pages
    })

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
