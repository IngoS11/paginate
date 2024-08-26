import pandas as pd
from app import db, User

def load_users_from_csv(filename):
    db.drop_all()
    db.create_all()
    df = pd.read_csv(filename)
    # Add each user from the CSV file to the session
    for index, row in df.iterrows():
        user = User(name=row['name'], email=row['email'])
        db.session.add(user)
        db.session.commit()
