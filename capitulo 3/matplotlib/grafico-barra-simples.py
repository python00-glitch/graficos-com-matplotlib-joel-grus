# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam 2 argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

# (de acordo com a versão livro da USP, precisamos ajustar as coordenadas dos gráficos, oque se prova o contrário no
# livro físico original)

# importe o módulo "plot" da biblioteca "matplotlib"
from matplotlib import pyplot as p
import random

movies = ["Guardioes da Galáxia", "Eternos", "Vingadores 1", "Vingadores 2", "Vingadores 3", "Doutor Estranho"
          , "De volta pra casa", "Miles Morales"]
notas = [10.0, 8.3, 7.6, 9.4, 10.0, 7.9, 8.8, 9.8]
# notas = [random.randint(1, 10)]

# as barras de um gráfico costumam ter 0.8 de espaço, então, adicionaremos 0.1 para às coordenadas á esquerda para que
# as barras sejam centralizadas
# xs = [i + 0.1 for i, _ in enumerate(movies)] (versão livro da USP)

# as barras do gráfico com as coordenadas X á esquerda [xs], alturas [num_oscars]
# p.bar(xs, notas) (versão livro da USP)
p.bar(movies, notas)
# p.bar ( eixo X, eixo Y)

p.ylabel("Notas")
p.title("Notas para meus filmes favoritos")

# coloca os nomes dos filmes centralizados na variável [xs]
# p.xticks([i + 0.5 for i, _ in enumerate(movies)], movies) (versão livro da USP)

# e mostre o gráfico
p.show()
