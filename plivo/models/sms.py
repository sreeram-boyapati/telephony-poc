from plivo.app import db


class SMS(db.Model):
    __tablename__ = 'sms'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(16), index=True)
    receiver = db.Column(db.String(16))
    sms_text = db.Column(db.String(120))
    sent_at = db.Column(db.TIMESTAMP)
