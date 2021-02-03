"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    events_attending = db.relationship('Event', secondary="guest_event_table" , back_populates="guests")




# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80))
    date_and_time = db.Column(db.DateTime, unique=True)
    guests = db.relationship('Guest', secondary="guest_event_table" , back_populates="events_attending")



guest_event_table = db.Table("guest_event_table",
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)