from AdjacencyList import AdjacencyList
from GraphReader import GraphReader


class Graph:

    def __init__(self, adjacency_list):
        self.__adjacency_list = adjacency_list
        self.__heuristic_matrix = GraphReader("./direct-distance.csv").read()
        self.__color_line = None

    def neighborhood(self, node):
        return self.__adjacency_list[node]
    
    def heuristic(self, start, end):
        start = int(start[1:]) - 1 
        end = int(end[1:]) - 1
        return self.__heuristic_matrix[start][end] 

    def a_star(self, first_station, last_station):
      visited_stations = set([first_station])
      visited_neighbors = set([])

      g = {}
      g[first_station] = 0

      parents = {}
      parents[first_station] = first_station

      while len(visited_stations) > 0:
        current_station = None

        for station in visited_stations:
          if current_station == None or g[station] + self.heuristic(station, last_station) < g[current_station] + self.heuristic(current_station, last_station):
            current_station = station

        if current_station == None:
            print('Não existe caminho entre essas estações')
            return None

        if current_station == last_station:
            reconst_path = []

            while parents[current_station] != current_station:
                reconst_path.append(current_station)
                current_station = parents[current_station]

            reconst_path.append(first_station)

            reconst_path.reverse()

            print('Caminho encontrado: {}'.format(reconst_path))
            return reconst_path

        for (station, distance) in self.neighborhood(current_station):

            if station not in visited_stations and station not in visited_neighbors:
                visited_stations.add(station)
                parents[station] = current_station
                g[station] = g[current_station] + distance

            else:
                if g[station] > g[current_station] + distance:
                    g[station] = g[current_station] + distance
                    parents[station] = current_station

                    if station in visited_neighbors:
                        visited_neighbors.remove(station)
                        visited_stations.add(station)

        visited_stations.remove(current_station)
        visited_neighbors.add(current_station)

      print('Não existe caminho entre essas estações')
      return None


if __name__ == "__main__":
    reader = AdjacencyList("./real-distance.csv")
    adj_list = reader.read()
    oi = Graph(adj_list)
    oi.a_star("E1", "E7")
    # print(adj_list)

