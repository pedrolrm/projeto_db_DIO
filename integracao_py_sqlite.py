from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(9), nullable=False)
    endereco = Column(String(9), nullable=False)
    
    contas = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', endereco='{self.endereco}')>"

class Conta(Base):
    __tablename__ = 'conta'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(DECIMAL, nullable=False)
    
    cliente = relationship('Cliente', back_populates='contas')

    def __repr__(self):
        return f"<Conta(id={self.id}, tipo='{self.tipo}', agencia='{self.agencia}', num={self.num}, id_cliente={self.id_cliente}, saldo={self.saldo})>"

# SQLite database setup
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Cliente and Conta
cliente1 = Cliente(nome='Pedro Manera', cpf='123456789', endereco='123456789')
conta1 = Conta(tipo='corrente', agencia='001', num=12345, id_cliente=1, saldo=1000.50)

# Add to the session and commit
session.add(cliente1)
session.add(conta1)
session.commit()

# Retrieve all clients
def get_all_clients():
    clients = session.query(Cliente).all()
    return clients

# Retrieve a client by ID
def get_client_by_id(client_id):
    client = session.query(Cliente).filter_by(id=client_id).first()
    return client

# Retrieve all accounts for a client
def get_accounts_by_client_id(client_id):
    accounts = session.query(Conta).filter_by(id_cliente=client_id).all()
    return accounts

# Test the methods
print(get_all_clients())
print(get_client_by_id(1))
print(get_accounts_by_client_id(1))
