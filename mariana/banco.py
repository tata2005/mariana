from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xJhMvupCHJrWEbxdfwcoaEOWpzQPhsAx@shuttle.proxy.rlwy.net:31491/railway//PGPASSWORD=xJhMvupCHJrWEbxdfwcoaEOWpzQPhsAx psql -h shuttle.proxy.rlwy.net -U postgres -p 31491 -d railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# Criar o banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar_produto():
    data = request.json
    novo_produto = Produto(nome=data['nome'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto adicionado!'})

@app.route('/listar', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome} for p in produtos])

if __name__ == '__main__':
    app.run(debug=True)