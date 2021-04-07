import sys


class DictionaryGraph:
    def __init__(self, n):
        """
        :param n: The number of vertices
        """
        self.vertices = n
        self.dictionary = {}
        self.costs = {}
        for i in range(n):
            self.dictionary[i] = []
            for j in range(n):
                self.costs[(i, j)] = None

    def is_edge(self, x, y):
        return y in self.dictionary[x]

    def add_edge(self, x, y, cost):
        if not self.is_edge(x, y):
            self.dictionary[x].append(y)
            self.costs[(x, y)] = cost
            self.dictionary[y].append(x)
            self.costs[(y, x)] = cost

    def parse_x(self):
        return self.dictionary.keys()

    def dijkstra_algorithm(self, source, destination):
        distance = [sys.maxsize] * self.vertices
        distance[source] = 0
        node_cost = {source: 0}
        while node_cost:
            source_node = min(node_cost, key=lambda x: node_cost[x])
            del node_cost[source_node]

            if self.costs[(source_node, destination)] is not None:
                if distance[destination] > distance[source_node] + self.costs[(source_node, destination)]:
                    distance[destination] = distance[source_node] + self.costs[(source_node, destination)]
                    node_cost[destination] = distance[destination]

        print("The distance from", source, "to", destination, "is:", distance[destination])


class MainProgram:
    def __init__(self):
        file = open("input.txt", "r")
        number_of_vertices, number_of_edges = map(int, file.readline().split())
        self.g = DictionaryGraph(int(number_of_vertices))

        for edge in range(number_of_edges):
            x, y, cost = map(int, file.readline().split())
            self.g.add_edge(x, y, cost)

    def run(self):
        self.g.dijkstra_algorithm(0, 4)


program = MainProgram()
program.run()