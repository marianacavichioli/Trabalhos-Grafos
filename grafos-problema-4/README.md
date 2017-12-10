# PROJETO 4: ÁRVORES DE CAMINHOS MÍNIMOS E AGRUPAMENTO DE DADOS
A partir de um dataset específico (grafo ponderado armazenado em arquivo .gml, .graphml, .txt, .net, etc) e implementar o algoritmo de Dijkstra para extrair uma árvore de caminhos mínimos de G.

## Metodologia

Após a implementação do algoritmo, uma forma de crescer várias subárvores de caminhos mínimos é inicializar várias sources, ou seja, atribuir custo inicial zero a um número K de vértices. O restante do algoritmo permanece intacto. O que irá acontecer é um processo de disputa entre cada uma das raízes para verificar qual delas irá conquistar cada vértice de G. Ao final da execução um vértice estará "pendurado" apenas a uma única subárvore, fazendo com que tenhamos vários grupos de nós, similar ao que acontecia com as MST's. Porém aqui há supervisão no processo de formação dos grupos, uma vez que o usuário pode definir de onde as subárvores irão iniciar o crescimento (esses pontos devem ser escolhidos de forma a definir o centro dos agrupamentos).

## QUESTIONAMENTOS

### Considerando o grafo em questão, mostre os resultados (plote graficamente) obtidos para:
### a) 2 agrupamentos (K = 2) 
### b) 3 agrupamentos (K = 3)
