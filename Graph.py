from GraphReader import GraphReader

class Graph:

    def __init__(self, adjacency_list):
        self.__adjacency_list = adjacency_list
    
    def neighborhood(self, node):
        return self.__adjacency_list[node]
    
    def heuristic(self, n):
        H = {
            'E1': 1,
            'E2': 1,
            'E3': 1,
            'E4': 1,
            'E5': 1,
            'E6': 1,
            'E7': 1,
            'E8': 1,
            'E9': 1,
            'E10': 1,           
            'E11': 1,
            'E12': 1,
            'E13': 1,
            'E14': 1
        }

        return H[n]

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
          if current_station == None or g[station] + self.heuristic(station) < g[current_station] + self.heuristic(current_station):
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
    reader = GraphReader("./real-distance.csv")
    adj_list = reader.read()
    oi = Graph(adj_list)
    print(adj_list)
    oi.a_star("E1", "E7")
    # print(adj_list)

