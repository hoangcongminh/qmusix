from backend.framework.database import db


class Music(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(), nullable=False)
