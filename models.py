from datetime import datetime
from config import db, ma

class Milestones(db.Model):
    __tablename__ = 'milestones'
    id = db.Column(db.Integer, primary_key=True)
    pelajaran = db.Column(db.String(255), nullable=False)
    pencapaian = db.Column(db.String(255), nullable=False)
    keterangan = db.Column(db.Text)
    is_complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    pengajar_id = db.Column(db.Integer, db.ForeignKey('pengajar.id'))

class MilestonesSchema(ma.SQLAlchemyAutoSchema):
    pengajar = ma.Nested('PengajarSchema', exclude=('milestones',))

    class Meta:
        model = Milestones
        sqla_session = db.session

class Pengajar(db.Model):
    __tablename__ = 'pengajar'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255), nullable=False)
    keahlian = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    milestones = db.relationship('Milestones', backref='pengajar', lazy='dynamic')

class PengajarSchema(ma.SQLAlchemyAutoSchema):
    milestones = ma.Nested(MilestonesSchema, many=True,exclude=('pengajar',))

    class Meta:
        model = Pengajar
        sqla_session = db.session
