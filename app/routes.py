from flask import Blueprint, request, render_template, redirect, url_for
from app.services import cadastrar_usuario, cadastrar_relato, listar_relatos

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/usuarios/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario_view():
    if request.method == 'POST':
        try:
            data = {
                'nome': request.form['nome'],
                'documento': request.form['documento'],
                'email': request.form['email'],
                'telefone': request.form['telefone'],
                'localizacao': request.form['localizacao'].split(',')
            }
            cadastrar_usuario(data)
            return redirect(url_for('routes.index'))
        except Exception as e:
            return render_template('cadastro_usuario.html', erro=str(e))
    return render_template('cadastro_usuario.html')

@bp.route('/relatos/cadastrar', methods=['GET', 'POST'])
def cadastrar_relato_view():
    if request.method == 'POST':
        try:
            data = {
                'tipo': request.form['tipo'],
                'descricao': request.form['descricao'],
                'coordenadas': [
                    request.form['coordenada_lat'],
                    request.form['coordenada_lon']
                ],
                'relator_documento': request.form['relator_documento']
            }
            cadastrar_relato(data)
            return redirect(url_for('routes.listar_relatos_view'))
        except Exception as e:
            return render_template('cadastro_relato.html', erro=str(e))
    return render_template('cadastro_relato.html')

@bp.route('/relatos/listar')
def listar_relatos_view():
    relatos = listar_relatos()
    return render_template('listar_relatos.html', relatos=relatos)
