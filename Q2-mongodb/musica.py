from conexao import MongoConnect

class Musica():

    def save(self, nome, autor, genero):
        conexao = MongoConnect()
        coletanea = {"nome": nome, "autor": autor, "genero": genero}
        conexao.save(coletanea)