arquivo = open('arq-limpo3.txt', 'r')

le_arquivo = arquivo.read()

#print(le_arquivo)

result = le_arquivo.split("\n")

#print(result)


for i in result:
    print(i)