from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    localizacao_lat = db.Column(db.Float, nullable=False)
    localizacao_lon = db.Column(db.Float, nullable=False)
    relatos = db.relationship('Relato', backref='relator', lazy=True)

class Relato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    coordenadas_lat = db.Column(db.Float, nullable=False)
    coordenadas_lon = db.Column(db.Float, nullable=False)
    relator_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
