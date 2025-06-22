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
