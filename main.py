# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

grafo = {
    '1': set(['2', '3', '8', '13']),
    '2': set(['3', '8', '12', '1']),
    '3': set(['2', '4', '8', '13']),
    '4': set(['3', '7', '6', '5', '10', '9', '14']),
    '5': set(['7', '6', '10', '4']),
    '6': set(['7', '4', '6', '10']),
    '7': set(['11', '5', '6', '4']),
    '8': set(['2', '3', '1', '13', '12']),
    '9': set(['4', '13', '10', '14', '16']),
    '10': set(['9', '4', '6', '5', '11', '15', '14']),
    '11': set(['7', '18', '10', '6', '15']),
    '12': set(['1', '16', '8', '13', '2']),
    '13': set(['12', '3', '8', '9', '14', '16']),
    '14': set(['13', '16', '9', '4', '10', '15', '17']),
    '15': set(['14', '17', '18', '14', '11', '10']),
    '16': set(['12', '13', '9', '14', '17']),
    '17': set(['16', '14', '15', '18']),
    '17': set(['17', '15', '11'])
}

def dfs_caminhos(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio])]

    while pilha:
        (vertice, caminho) = pilha.pop()

        for proximo in grafo[vertice] - set(caminho):

            if proximo == objetivo:
                return caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))



    return 'Caminho não encontrado!'

print(dfs_caminhos(grafo, '1', '18'))
