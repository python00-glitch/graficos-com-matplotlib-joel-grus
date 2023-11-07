# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam mais argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

from matplotlib import pyplot as p

# quantidade de amigos que cada usuário tem no site
amigos = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutos que cada usuário passa utilizando o site
minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# a etiqueta (nome) de cada usuário

# cria o gráfico em formato de dispersão (ou scatterplots)
p.scatter(amigos, minutos)

# coloque etiqueta em cada ponto
# portugol: "para cada elemento de todas as listas que foram compactadas no 'zip':"
for etiqueta, amigos_count, minutos_count in zip(etiquetas, amigos, minutos):
    # portugol: "p.etiquete( cada etiqueta de 'etiquetas', xy=('amigos_c' no eixo X, 'minutos_c' no Y), coordenadas das
    # etiquetas, e o tipo de sistema de coordanadas da 'xytext'
    p.annotate(etiqueta, xy=(amigos_count, minutos_count), xytext=(5, -5), textcoords='offset points')
    # 'xytext=', 'textcoords=', e outras funções dentro do '.annotate' são opcionais, sendo não obrigatórias para o
    # funcionamento do gráfico. servindo apenas mostrar as etiquetas ao lado dos dados marcados no gráfico

p.title("Minutos Diários vs Quant. de Amigos")
p.xlabel("Numero de amigos")
p.ylabel("Minutos gastos no site")

p.show()


