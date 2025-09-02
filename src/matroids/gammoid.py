import networkx as nx
from .base import Matroid

class Gammoid(Matroid):
    def __init__(self, D: nx.DiGraph, S, T):
        super().__init__(T)  # elements are targets
        self.D, self.S, self.T = D, set(S), set(T)

    def is_independent(self, subset):
        # Independent iff there exist |subset| vertex-disjoint paths from S to subset
        # Greedy disjoint-paths via node-splitting + max-flow
        D = self.D.copy()
        for v in list(D.nodes()):
            D.add_node((v, "in"))
            D.add_node((v, "out"))
            D.add_edge((v, "in"), (v, "out"), capacity=1)
        for u, v in list(self.D.edges()):
            D.add_edge((u, "out"), (v, "in"), capacity=1)
        src = "SRC"; sink = "SNK"
        D.add_node(src); D.add_node(sink)
        for s in self.S:
            D.add_edge(src, (s, "in"), capacity=1)
        for t in subset:
            D.add_edge((t, "out"), sink, capacity=1)
        flow_value, _ = nx.maximum_flow(D, src, sink)
        return flow_value == len(list(subset))
