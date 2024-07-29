from pymongo import MongoClient

client = MongoClient("sua_uri_mongodb_atlas")
db = client['seu_banco_de_dados']

# Definindo a coleção
collection = db['bank']

# Inserindo documentos
clientes = [
    {
        "nome": "Pedro Manera",
        "cpf": "123456789",
        "endereco": "123456789",
        "contas": [
            {
                "tipo": "corrente",
                "agencia": "001",
                "num": 12345,
                "saldo": 1000.50
            }
        ]
    },
    {
        "nome": "Maria Silva",
        "cpf": "987654321",
        "endereco": "987654321",
        "contas": [
            {
                "tipo": "poupanca",
                "agencia": "002",
                "num": 54321,
                "saldo": 2000.75
            }
        ]
    }
]

collection.insert_many(clientes)

# Recuperar todos os clientes
todos_os_clientes = collection.find()
for cliente in todos_os_clientes:
    print(cliente)

# Recuperar um cliente específico pelo CPF
cliente_especifico = collection.find_one({"cpf": "123456789"})
print(cliente_especifico)

# Recuperar contas de um cliente específico
contas_cliente = collection.find_one({"cpf": "123456789"}, {"contas": 1, "_id": 0})
print(contas_cliente)

# Recuperar clientes com saldo maior que um determinado valor
clientes_com_saldo_alto = collection.find({"contas.saldo": {"$gt": 1500}})
for cliente in clientes_com_saldo_alto:
    print(cliente)
