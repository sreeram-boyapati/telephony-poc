from datetime import datetime, timedelta

from plivo.app import db


class SMS(db.Model):
    __tablename__ = 'sms'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(16), index=True)
    receiver = db.Column(db.String(16), index=True)
    sms_text = db.Column(db.String(120))
    sent_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "SMS ID: " + str(self.id)
