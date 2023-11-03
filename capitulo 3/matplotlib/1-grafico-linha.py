# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam mais argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

# importe o módulo "plot" da biblioteca "matplotlib"
from matplotlib import pyplot as p

# crie duas listas, e como boa prática, coloque a de cima como eixo X (vertical), e a de cima como eixo Y (horizontal)
notas = [12.3, 13.1, 10.2, 14.9, 15.0, 12.9, 9.8]
provas = ["matematica", "ingles", "historia", "geografia", "espanhol", "ciencias", "educacao f."]

# logo após, escreva a sintaxe que criará o gráfico de linhas
p.plot(provas, notas, marker="o", linestyle="solid")
# exemplo de sintaxe ( eixo X, eixo Y, cor="cor", marcador="tipo_de_marcador", linestyle="tipo_de_linha" )

# em seguida, coloque o título do gráfico com o ".title"
p.title("Notas do aluno Fulano")

# adicione um conjunto ao eixo Y
p.ylabel("Notas")

# e mostre o gráfico
p.show()
