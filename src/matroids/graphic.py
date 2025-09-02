import networkx as nx
from .base import Matroid

class GraphicMatroid(Matroid):
    def __init__(self, G: nx.Graph):
        super().__init__(G.edges())
        self.G = G

    def is_independent(self, subset):
        H = nx.Graph()
        H.add_nodes_from(self.G.nodes())
        H.add_edges_from(subset)
        # Independent iff no cycle: each component must have |E| <= |V|-1
        return nx.number_of_edges(H) == (H.number_of_nodes() - nx.number_connected_components(H))
