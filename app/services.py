from datetime import datetime
import math
from app.models import db, Usuario, Relato

CENTRO = (-23.5505, -46.6333)

def calcular_distancia(coord1, coord2):
    R = 6371
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))

def usuario_por_documento(documento):
    return Usuario.query.filter_by(documento=documento).first()

def cadastrar_usuario(data):
    if usuario_por_documento(data['documento']):
        raise ValueError("Documento já cadastrado.")
    usuario = Usuario(
        nome=data['nome'],
        documento=data['documento'],
        email=data['email'],
        telefone=data['telefone'],
        localizacao_lat=float(data['localizacao'][0]),
        localizacao_lon=float(data['localizacao'][1])
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario

def cadastrar_relato(data):
    lat = float(data['coordenadas'][0])
    lon = float(data['coordenadas'][1])
    if calcular_distancia((lat, lon), CENTRO) > 10:
        raise ValueError("Fora do raio de 10 km do ponto central.")
    relator = usuario_por_documento(data['relator_documento'])
    if not relator:
        raise ValueError("Relator não cadastrado.")
    relato = Relato(
        tipo=data['tipo'],
        descricao=data['descricao'],
        data_hora=datetime.now(),
        coordenadas_lat=lat,
        coordenadas_lon=lon,
        relator_id=relator.id
    )
    db.session.add(relato)
    db.session.commit()
    return relato

def listar_relatos():
    return Relato.query.all()
