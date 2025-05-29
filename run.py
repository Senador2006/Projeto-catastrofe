from flask import Flask
from app import routes
from app.models import db

app = Flask(__name__, template_folder='app/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catastrofes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Criar tabelas ao iniciar o app
with app.app_context():
    db.create_all()

app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run(debug=True)
