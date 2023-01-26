from AdjacencyList import AdjacencyList
from GraphReader import GraphReader
from GraphReaderType import GraphReaderType


class Graph:

    def __init__(self, adjacency_list):
        self.__adjacency_list = adjacency_list
        self.__heuristic_matrix = GraphReader("./direct-distance.csv").read()
        self.__color_matrix = GraphReader("./color-lines.csv", GraphReaderType.COLOR).read()

    def neighborhood(self, node):
        return self.__adjacency_list[node]
    
    def heuristic(self, start, end):
        start = int(start[1:]) - 1 
        end = int(end[1:]) - 1
        return self.__heuristic_matrix[start][end] 
    
    def find_color(self, start, end):
        start = int(start[1:]) - 1 
        end = int(end[1:]) - 1
        return self.__color_matrix[start][end] 

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
            return

        if current_station == last_station:
            path = []

            while parents[current_station] != current_station:
                path.append(current_station)
                current_station = parents[current_station]

            path.append(first_station)

            target = path[0]
            targetInMinutes = g[target]/60

            path.reverse()

            print('Caminho: {}'.format(path))
            print(f"Duração: {targetInMinutes:.2f} minutos")
            
            return path

        for (station, distance) in self.neighborhood(current_station):
            if station not in visited_stations and station not in visited_neighbors:
                visited_stations.add(station)
                parents[station] = current_station
                color_line_anterior = self.find_color(parents[current_station], current_station)
                color_line_aux = self.find_color(current_station, station)
                if color_line_anterior != color_line_aux and color_line_aux != "-" and color_line_anterior != "-":
                    g[station] = g[current_station] + distance + 4 * 60
                else:
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

      print('Não há caminhos')


if __name__ == "__main__":
    reader = AdjacencyList("./real-distance.csv")
    adj_list = reader.read()
    oi = Graph(adj_list)
    oi.a_star("E2", "E12")

