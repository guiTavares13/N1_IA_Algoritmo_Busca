# N1_IA_Algoritmo_Busca

O algoritmo de Dijkstra é baseado em um conjunto de vértices conhecidos como conjunto "S" (shortest path tree) que contém os vértices para os quais o caminho mais curto da origem foi encontrado. Inicialmente, S contém apenas o vértice de origem. O algoritmo então expande S para incluir novos vértices à medida que os caminhos mais curtos são encontrados.

O algoritmo de Dijkstra utiliza uma estrutura de dados conhecida como heap mínimo (ou min-heap) para armazenar os vértices que ainda não foram incluídos em S e cujos custos de caminho mais curto foram atualizados. A heap mínima é utilizada para garantir que o vértice com o menor custo seja sempre selecionado como próximo vértice a ser adicionado a S.

O algoritmo de Dijkstra funciona da seguinte maneira:

Inicialize o conjunto S com o vértice de origem e defina a distância de todos os outros vértices como infinita.
Inicialize uma heap mínima com o vértice de origem e sua distância como 0.
Enquanto a heap mínima não estiver vazia, faça o seguinte:
Remova o vértice com a menor distância da heap mínima.
Para cada vértice adjacente ao vértice removido, atualize a distância e o caminho se um caminho mais curto for encontrado.
Se o vértice adjacente não estiver em S, adicione-o à heap mínima.