import networkx as nx
from .base import Matroid

class TransversalMatroid(Matroid):
    def __init__(self, G: nx.Graph, U):
        super().__init__(U)
        self.G = G
        self.U = set(U)

    def is_independent(self, subset):
        # Independent iff subset is matchable to V
        subU = list(subset)
        H = self.G.copy()
        H.remove_nodes_from([u for u in self.U if u not in subU])
        matching = nx.algorithms.bipartite.maximum_matching(H, top_nodes=subU)
        # Count matches on U
        return sum(1 for u in subU if u in matching) == len(subU)
