from appniche.extensions import db, pwd_context

class Analysis(db.Model):
    """
    Basic analysis model which contains app niche analysis information
    """
    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)
    