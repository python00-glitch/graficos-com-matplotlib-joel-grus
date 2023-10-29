# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam 2 argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

from collections import Counter
# o Counter serve para contarmos a quantidade de ocorrências de elementos dentro de listas
#   exemplo: lista = [a, a, b, c, b]
#   contagem = Counter(lista)
#   print(contagem)
#   contagem = [{a: 2, b: 2, c: 1}]

from matplotlib import pyplot as plt

grades = [895.3, 234.4, 93.1, 912.0, 243.1, 43.2, 789.2, 493.6, 019.2, 91, 32, 43]
histograma = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histograma.keys()], histograma.values(), 10, edgecolor=(0, 0, 0))
# dentro dos colchetes [chaves], fora dos colchetes: valores
# primeiro = eixo X, segundo = eixo Y

# agora, você irá ditar de qual número até qual número cada eixo irá seguir
plt.axis([-5, 105, 0, 5])  # eixo X = -5 até 105, eixo Y = 0 até 5

# "ticks" são cada marcador do eixo escolhido, para marcar cada elemento mostrado
plt.xticks([10 * marker for marker in range(11)])  # a cada marcador, mostrar um número multiplicado por '10' (0, 10...)

# coloque um conjunto no eixo X para escrever
plt.xlabel("Variação")

# coloque um conjunto no eixo Y para escrever
plt.ylabel("# de Estudantes")

# coloque um título
plt.title("Distribuição de Notas do Exame 1")

# e mostre o gráfico
plt.show()
