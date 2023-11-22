from config import db
from models import Milestones, MilestonesSchema,Pengajar
from flask import request,jsonify
from datetime import datetime

milestones_schema = MilestonesSchema()

def get_all():
    milestones = Milestones.query.all()
    data = milestones_schema.dump(milestones,many=True)
    return data

def get_single(id):
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    if milestone is not None:
        data = milestones_schema.dump(milestone)
        return data
    
    else :
        return jsonify({'error': f"Milestone dengan id : {id} tidak ditemukan"}), 404

def create():
    data = request.json
    pengajar = Pengajar.query.filter(Pengajar.id == data['pengajar_id']).one_or_none()

    if pengajar is not None:
        milestone = Milestones(
            pelajaran=data['pelajaran'],
            pencapaian=data['pencapaian'],
            keterangan=data['keterangan'],
            is_complete=data['is_complete'],
            pengajar_id=data['pengajar_id']
        )
        db.session.add(milestone)
        db.session.commit()
        milestones_schema = MilestonesSchema(exclude=['pengajar'])
        data = milestones_schema.dump(milestone)
        return data
    
    else:
        return jsonify({'error': f"Pengajar dengan id : {data['pengajar_id']} tidak ditemukan"}), 404
    
def update(id):
    data = request.json
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    if milestone is not None:
        pengajar = Pengajar.query.filter(Pengajar.id == data['pengajar_id']).one_or_none()
        if pengajar is not None:
            milestone.pelajaran=data['pelajaran']
            milestone.pencapaian=data['pencapaian']
            milestone.keterangan=data['keterangan']
            milestone.is_complete=data['is_complete']
            milestone.pengajar_id=data['pengajar_id']
            milestone.updated_at=datetime.utcnow()
            db.session.commit()
            data = milestones_schema.dump(milestone)
            return data
        
        else:
            return jsonify({'error': f"Pengajar dengan id : {data['pengajar_id']} tidak ditemukan"}), 404
        
    else:
        return jsonify({'error': f"Milestone dengan id : {id} tidak ditemukan"}), 404

    
def delete(id):
    milestone = Milestones.query.filter(Milestones.id == id).one_or_none()
    if milestone is not None:
        db.session.expunge(milestone.pengajar)
        db.session.delete(milestone)
        db.session.commit()
        data = milestones_schema.dump(milestone)
        return data
    
    else :
        return jsonify({'error': f"Milestone dengan id : {id} tidak ditemukan"}), 404
