from matplotlib import pyplot as plt

anos_namoro = [2022, 2023]
quant_amor = [50, 100]

plt.axis([2021.5, 2023.5, 0, 100.90])

plt.bar(anos_namoro, quant_amor, width=0.5, edgecolor=(0, 0, 0))
plt.xticks(anos_namoro)
# plt.yticks(quant_amor)


plt.title("O quanto eu amo a minha noiva:")
plt.ylabel("Quantidade do meu amor por ti <3")
plt.xlabel("Anos de namoro")

plt.show()
