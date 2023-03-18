
grafo = {
    '1': {'2': 20, '8': 29, '12': 29, '13': 37},
    '2': {'1': 20, '3': 25, '8': 28, '12': 39},
    '3': {'2': 25, '4': 25, '8': 30, '13': 54},
    '4': {'3': 25, '5': 39, '6': 32, '7': 42, '9': 23, '10': 33, '14': 56},
    '5': {'4': 39, '6': 12, '7': 26, '10': 19},
    '6': {'4': 32, '5': 12, '7': 17, '10': 35, '11': 30},
    '7': {'4': 42, '5': 26, '6': 17, '11': 38},
    '8': {'1': 29, '2': 28, '3': 30, '12': 25, '13': 22},
    '9': {'4': 23, '10': 26, '13': 34, '14': 37, '16': 43},
    '10': {'4': 33, '5': 19, '6': 35, '9': 26, '11': 24, '14': 30, '15': 19},
    '11': {'6': 30, '7': 38, '10': 24, '15': 26, '18': 36},
    '12': {'1': 29, '2': 39, '8': 25, '13': 27, '16': 43},
    '13': {'1': 37, '3': 54, '8': 22, '9': 34, '12': 27, '14': 24, '16': 19},
    '14': {'4': 56, '9': 37, '10': 30, '13': 24, '15': 20, '16': 19, '17': 17},
    '15': {'10': 19, '11': 26, '14': 20, '17': 18, '18': 21},
    '16': {'9': 43, '12': 43, '13': 19, '14': 19, '17': 26},
    '17': {'14': 17, '15': 18, '16': 26, '18': 15},
    '18': {'11': 36, '15': 21, '17': 15},
}

# inicia com grafo, 1, 18 e quantidade de rotas igual a 5
def dfs_caminhos(grafo, inicio, objetivo, qdt_caminhos=5):
    # uma pilha com inicio e um valor dentro da lista
    # inicialmente a pilha contem o valor 1 como partida e 1 que representa o caminho percorrido até o momento
    pilha = [(inicio, [inicio], 0)]

    caminhos_encontrados = []

    while pilha:

        # vertice recebe o primeiro elemento da tupla retornada pelo método pop()
        # caminho recebe o segundo elemento da tupla, que represneta o caminho percorrido até o vértice atual
        (vertice, caminho, custo_total) = pilha.pop()


        if vertice == objetivo:
            caminho_completo = caminho + [vertice, custo_total]
            caminhos_encontrados.append(caminho_completo)
            if len(caminhos_encontrados) == qdt_caminhos:
                return caminhos_encontrados

        # Para cada vertice adjacente dentro do conjunto grafo[vertice] que ainda não foi visitado. Execute o for
        #for proximo in grafo[vertice] - set(caminho):
        for proximo in set(grafo[vertice]) - set(caminho):

            custo = grafo[vertice][proximo]

            pilha.append((proximo, caminho + [proximo], custo_total + custo))
            # if proximo == objetivo:
            #     return caminho + [proximo]
            # else:
            #     pilha.append((proximo, caminho + [proximo]))

    if len(caminhos_encontrados) == qdt_caminhos:
        return caminhos_encontrados
    else:
        return f'Não foram econtrados os {qdt_caminhos} caminhos'

caminhos = dfs_caminhos(grafo, '1', '10')

for caminho in caminhos:
    print(f"Caminho: {caminho[:-1]}, Custo Total: {caminho[-1]}")


# Definindo melhor caminho entre os encontrados
menor_custo = float("inf")  # define o menor custo inicial como infinito
melhor_caminho = None

for caminho in caminhos:
    custo = caminho[-1]  # extrai o custo do caminho atual
    if custo < menor_custo:  # verifica se o custo atual é menor que o menor custo encontrado até o momento
        menor_custo = custo  # atualiza o menor custo
        melhor_caminho = caminho[:-1]  # atualiza o melhor caminho

print(f"Melhor Caminho: {melhor_caminho}, Custo Total: {menor_custo}")