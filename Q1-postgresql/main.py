from operacao_banco import Operacoes

operacao = Operacoes()

#id_musica = int(input("Digite a ID da música: "))

nome= str(input("Digite o nome da música: "))
autor = str(input("Digite o autor da música: "))
genero = str(input("Digite o gênero da música: "))
operacao.salvar(nome, autor, genero)
operacao.buscar()