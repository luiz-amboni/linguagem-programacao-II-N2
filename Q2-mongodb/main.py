from musica import Musica

colecao = Musica()

nome = str(input("Digite o nome da música: "))
autor = str(input("Digite o autor da música: "))
genero = str(input("Digite o gênero da música: "))

colecao.save(nome, autor, genero)