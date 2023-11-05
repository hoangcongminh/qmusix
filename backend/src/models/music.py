from src.framework.database import db


class Music(db.Model):
    __tablename__ = "music"
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(), nullable=False)
