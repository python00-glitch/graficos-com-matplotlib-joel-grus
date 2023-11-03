# NOTAS IMPORTANTES: funções do módulo "pyplot", exemplificando ".axis()", levam apenas 1 ARGUMENTO, por isso
#    sempre coloque argumentos que levam mais de um elemento entre colchetes [] para ser considereado 1 argumento
#    funções que determinam a anela do gráfico, como ".plot" ou ".bar" são exceções que levam mais argumentos, mas caso
#    precise fazer um fluxo de controle, ter de se colocar o fluxo entre colchetes []
# funções são todas as ações marcadas com ponto antes da palavra, e um parênteses no final dela [.funcao()]

from matplotlib import pyplot as p

variantes = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_quadrado = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error = [x + y for x, y in zip(variantes, bias_quadrado)]  # [soma os elementos PARA as duas listas no conjunto()]
#       o resultado de cada elemento de 'total_error' é a soma [x + y] de cada valor ['x' e 'y'] de cada lista
#       [variantes[x], bias_quadrado[y]] conjuntadas no 'zip()'

# a função 'enumerate()' cria um indice para cada elemento de uma lista
# assim, para cada elemento [x] em 'variantes', e cada elemento [i] de 'enumerate()', 'xs' recebe um par(i, x), mas
#       apenas o valor do indice [i] é atribuido á lista 'xs'
xs = [i for i, _ in enumerate(variantes)]  # atribui o elemento[i] de cada elemento[i] como um indice[enumerate] criado
#       criado através da lista(variantes)

# o .plot() pode ser usado várias vezes para mostrar várias linhas no gráfico
p.plot(xs, variantes, 'g-', label="imprevisibilidade")  # adicionando rótulos para legendas
# 'g' = 'green' / '-' = 'tracejado', é usado para mostrar uma LINHA TRACEJADA em VERDE
p.plot(xs, bias_quadrado, 'r-.', label="bias ao quadrado")  # adicionando rótulos para legendas
# 'r' = 'red' / '-.' = 'tracejada com ponto', é usado para mostrar uma LINHA DE PONTO TRACEJADA em VERMELHO
p.plot(xs, total_error, 'b:', label="total de erros")  # adicionando rótulos para legendas
# 'b' = 'blue' / ':' = 'pontilhada', é usado para mostrar uma LINHA PONTILHADA em AZUL

# agora, vamos posicionar as legendas que escrevemos nos '.plot' no centro do gráfico
p.legend(loc=9)  # o argumento 'loc=' tem números de 0-10, posicionando a 'label' de acordo com o número
# normalmente, '0' e '9' são centralizados na parte superior

p.xlabel("complexidade do modelo")
p.xticks([])
p.title("O Dilema Viés-Variância")

p.show()
