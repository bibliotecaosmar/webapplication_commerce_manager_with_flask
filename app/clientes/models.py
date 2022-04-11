from app import db
from flask_login import UserMixin
  
    
class Cliente(UserMixin, db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    foto_perfil = db.Column(db.LargeBinary)
    confirmado = db.Column(db.Boolean, nullable=False, default=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_modificacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    #Relacionamentos
    confirm_email = db.relationship('ConfirmEmail', uselist=False, backref='clientes') #Relacionamento 1 para 1

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return f'Cliente {self.nome}'

class ConfirmEmail(db.Model):
    __tablename__ = 'confirmacao_email'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(80), nullable=False)
    expiration = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

    def __init__(self, token, expiration, cliente_id):
        self.token = token
        self.expiration = expiration
        self.cliente_id = cliente_id