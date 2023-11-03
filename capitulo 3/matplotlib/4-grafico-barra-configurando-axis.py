# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam mais argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

from matplotlib import pyplot as p

# crie uma lista com números limite que você quer para cada eixo
years = [2017, 2018]  # eixo X
times = [500, 503]  # eixo Y (como não iremos especificar como marcadores, ele irá mostrar de 0 - 500 e um pequeno
# para o meio decil que representa o '5')

# defina em quais números começarã e terminará cada eixo
p.axis([2016.5, 2018.5, 499, 505])  # '2016.5' e '2018.5' significa que o X começará no meio de 2016, e terminará no meio
# do número 2018

# defina o eixo X, eixo Y, largura, bordas para melhor vizualização, logo os marcadores do eixo X, e o título do eixo Y
p.bar(years, times, 0.8, edgecolor=(0, 0, 0))  # respectivamente: p.bar ( X, Y, width, edgecolor=() )
p.xticks(years)  # colocando cada elemento da lista "years" como um marcador
p.ylabel("Vezes que ouvi sobre ciencia de dados")  # título do conjunto no eixo Y
p.xlabel("Anos que se passaram")

p.show()
