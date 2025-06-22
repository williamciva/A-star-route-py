import streamlit as st
import heapq

class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for b, dist in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        return links if b is None else links.get(b)

# Heurística (neutra)
def heuristic(a, b):
    return 0

# Algoritmo A*
def astar_search(graph, start, end):
    open_list = []
    heapq.heappush(open_list, (0, start, []))
    visited = set()

    while open_list:
        cost, current, path = heapq.heappop(open_list)

        if current == end:
            path.append(current)
            return path, cost

        if current not in visited:
            visited.add(current)
            for neighbor, distance in graph.get(current).items():
                total_cost = cost + distance + heuristic(neighbor, end)
                heapq.heappush(open_list, (total_cost, neighbor, path + [current]))

    return None, float('inf')


def build_graph():
    graph = Graph(directed=False)

    connections = [
        ("PFB - Passo Fundo", "GRU - São Paulo", 792),
        ("GRU - São Paulo", "FLN - Florianópolis", 513),
        ("GRU - São Paulo", "POA - Porto Alegre", 863),
        ("FLN - Florianópolis", "POA - Porto Alegre", 450),
        ("POA - Porto Alegre", "CXJ - Caxias do Sul", 98),
        ("POA - Porto Alegre", "GEL - Santo Ângelo", 254),
        ("GEL - Santo Ângelo", "CXJ - Caxias do Sul", 306),
    ]

    for a, b, dist in connections:
        graph.connect(a, b, dist)

    return graph

def main():
    st.title("🛩️ Algoritmo A* - Aeroportos do Sul/Sudeste")
    
    st.markdown("""
    ### 🧠 Explicação do Algoritmo A*

    O algoritmo **A\\*** é um dos algoritmos mais eficientes e populares para encontrar o **caminho mais curto** entre dois pontos em um grafo, como no caso de rotas entre cidades ou aeroportos.

    Ele combina duas abordagens:

    - 🔍 **Busca de custo uniforme** (Dijkstra): prioriza caminhos com menor custo real.
    - 🤖 **Busca heurística** (Busca Gulosa): tenta estimar o custo até o destino para ser mais eficiente.

    #### 📌 Como funciona?
    O A\\* avalia os nós com base na função de custo:

    **f(n) = g(n) + h(n)**

    - `g(n)` → custo real do caminho do início até o nó `n`
    - `h(n)` → estimativa (heurística) do custo de `n` até o destino
    - `f(n)` → custo total estimado do caminho passando por `n`

    Ele sempre escolhe o próximo nó com menor valor de `f(n)`.

    #### 🧮 Heurística (h)
    A heurística é uma forma de **"adivinhar"** o custo restante até o destino. Em mapas reais, normalmente se usa a **distância em linha reta** (como o GPS). Neste projeto, para simplificar, usamos `h(n) = 0`, ou seja, **nenhuma estimativa** – o algoritmo se comporta como o Dijkstra puro.

    #### ✅ Vantagens do A\\*
    - Garante encontrar o caminho mais curto (se a heurística for admissível)
    - É mais rápido que Dijkstra em grafos grandes com uma boa heurística

    #### 🚫 Limitações
    - Se a heurística for mal escolhida, pode se comportar de forma ineficiente
    - Pode consumir muita memória dependendo do tamanho do grafo

    """)

    graph = build_graph()
    cities = sorted(graph.graph_dict.keys())

    origem = st.selectbox("✈️ Cidade de origem", cities)
    destino = st.selectbox("🏁 Cidade de destino", cities)

    if st.button("Calcular menor rota"):
        if origem == destino:
            st.warning("As cidades devem ser diferentes.")
        else:
            path, cost = astar_search(graph, origem, destino)
            if path:
                st.success(f"🗺️ Rota: {' → '.join(path)}")
                st.info(f"📏 Distância total: {cost} km")
            else:
                st.error("❌ Nenhum caminho encontrado.")

if __name__ == "__main__":
    main()
