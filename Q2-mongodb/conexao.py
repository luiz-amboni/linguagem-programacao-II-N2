from pymongo import MongoClient

class MongoConnect():

    def save(self, json):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.prova
            musica = banco.musica
            id = musica.insert_one(json).inserted_id
        
        except Exception as e:
            print("Erro no registro. Tente novamente.")
            print(json)
            print(e)