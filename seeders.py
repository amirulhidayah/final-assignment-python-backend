import os
from config import db
from models import Milestones,Pengajar
from app import connex_app
from datetime import datetime

# Data to initialize the database with
DAFTAR_PENGAJAR = [
    {'nama': 'Abdillah Fajar', 'keahlian': 'Back End', 'email': 'abdillahfajar@example.com'},
    {'nama': 'Rizky Akbar', 'keahlian': 'Front End', 'email': 'rizkyakbar@example.com'},
    {'nama': 'Sandhika Galih', 'keahlian': 'Web Developer', 'email': 'sandhikagalih@example.com'},
]

MILESTONES = [
    {'pelajaran': 'Introduction to Backend', 'pencapaian': 'Setup Development Environment', 'keterangan': 'Install and configure necessary development tools', 'is_complete': True, 'pengajar_id': 1},
    {'pelajaran': 'Database Design', 'pencapaian': 'Create Database Schema', 'keterangan': 'Design and implement the database schema for the project', 'is_complete': False, 'pengajar_id': 2},
    {'pelajaran': 'RESTful API Implementation', 'pencapaian': 'Implement User Authentication', 'keterangan': 'Integrate user authentication functionality into the API', 'is_complete': False, 'pengajar_id': 1},
    {'pelajaran': 'Testing and Debugging', 'pencapaian': 'Write Unit Tests', 'keterangan': 'Develop and execute unit tests for critical components', 'is_complete': False, 'pengajar_id': 3},
]

# Delete database file if it exists currently
if os.path.exists('milestones.db'):
    os.remove('milestones.db')

# Create the database
with connex_app.app.app_context():
    db.create_all()

    # Seed Pengajars
    for pengajar_data in DAFTAR_PENGAJAR:
        pengajar = Pengajar(
            nama=pengajar_data['nama'],
            keahlian=pengajar_data['keahlian'],
            email=pengajar_data['email'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(pengajar)

    # Seed Milestones
    for milestone in MILESTONES:
        pengajar = Pengajar.query.filter(Pengajar.id == milestone['pengajar_id']).first()
        m = Milestones(
            pelajaran=milestone['pelajaran'],
            pencapaian=milestone['pencapaian'],
            keterangan=milestone['keterangan'],
            is_complete=milestone['is_complete'],
            pengajar_id=milestone['pengajar_id'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(m)

    db.session.commit()
