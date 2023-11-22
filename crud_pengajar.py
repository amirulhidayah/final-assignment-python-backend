from config import db
from models import Pengajar, PengajarSchema
from flask import jsonify,request
from datetime import datetime

pengajar_schema = PengajarSchema()

def get_all():
    daftarPengajar = Pengajar.query.order_by(Pengajar.id).all()
    pengajar_schema = PengajarSchema(many=True)
    data = pengajar_schema.dump(daftarPengajar)
    return data

def get_single(id):
    pengajar = Pengajar.query.filter(Pengajar.id == id).one_or_none()
    if pengajar is not None:
        data = pengajar_schema.dump(pengajar)
        return data
    
    else :
        return jsonify({'error': f"Pengajar dengan id : {id} tidak ditemukan"}), 404
    
def create():
    data = request.json
    pengajar = Pengajar(
        nama=data['nama'],
        keahlian=data['keahlian'],
        email=data['email'],
    )
    db.session.add(pengajar)
    db.session.commit()
    pengajar_schema = PengajarSchema(exclude=['milestones'])
    data = pengajar_schema.dump(pengajar)
    return data

def update(id):
    data = request.json
    pengajar = Pengajar.query.filter(Pengajar.id == id).one_or_none()
    if pengajar is not None:
        pengajar.nama=data['nama']
        pengajar.keahlian=data['keahlian']
        pengajar.email=data['email']
        pengajar.updated_at=datetime.utcnow()
        db.session.commit()
        data = pengajar_schema.dump(pengajar)
        return data
        
    else:
        return jsonify({'error': f"Pengajar dengan id : {id} tidak ditemukan"}), 404

def delete(id):
    pengajar = Pengajar.query.filter(Pengajar.id == id).one_or_none()
    if pengajar is not None:
        db.session.delete(pengajar)
        db.session.commit()
        data = pengajar_schema.dump(pengajar)
        return data
    
    else :
        return jsonify({'error': f"Pengajar dengan id : {id} tidak ditemukan"}), 404
