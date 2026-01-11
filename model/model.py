import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self._idMap = {}

    def get_years(self):
        return DAO.get_all_years()

    def get_teams_by_year(self, year):
        self._nodes = DAO.get_teams_by_year(year)
        self._idMap = {t.id: t for t in self._nodes}
        return self._nodes

    def build_graph(self, year):
        self._graph.clear()

        self._nodes = DAO.get_teams_by_year(year)
        self._graph.add_nodes_from(self._nodes)

        self._idMap = {t.id: t for t in self._nodes}

        for i in range(len(self._nodes)):
            for j in range(i + 1, len(self._nodes)):
                u = self._nodes[i]
                v = self._nodes[j]

                weight = u.tot_salary + v.tot_salary

                self._graph.add_edge(u, v, weight=weight)

    def get_graph_details(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_team_by_id(self, id):
        return self._idMap.get(id)

    def get_sorted_neighbors(self, team_obj):
        neighbors = []
        for neighbor in self._graph.neighbors(team_obj):
            weight = self._graph[team_obj][neighbor]['weight']
            neighbors.append((neighbor, weight))

        neighbors.sort(key=lambda x: x[1], reverse=True)
        return neighbors





