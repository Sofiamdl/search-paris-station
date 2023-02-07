from AdjacencyList import AdjacencyList
from GraphReader import GraphReader
from GraphReaderType import GraphReaderType


class Graph:

    def __init__(self, adjacency_list):
        self.__adjacency_list = adjacency_list
        self.__heuristic_matrix = GraphReader("./data/direct-distance.csv").read()
        self.__color_matrix = GraphReader("./data/color-lines.csv", GraphReaderType.COLOR).read()

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
      # Estações já visitadas que não tiveram os vizinhos visitados
      visited_stations = set([first_station])
      # Estações que os vizinhos ja foram visitados
      visited_neighbors = set([])

      # Distancia de todos pontos até a primeira estação
      g = {}
      g[first_station] = 0

      parents = {}
      parents[first_station] = first_station

      while len(visited_stations) > 0:
        current_station = None

        # Esse "for" vai escolher qual a estação que foi visitada, mas não teve os vizinhos visitados ainda, tem a
        # menor (inicio até distância real + propria estação até o final), para no futuro calcular a distância dela até
        # todos seus vizinhos
        for station in visited_stations:
          if current_station == None or g[station] + self.heuristic(station, last_station) < g[current_station] + self.heuristic(current_station, last_station):
            current_station = station

        # Se não existir nenhum caminho entre estações
        if current_station == None:
            print('Não existe caminho entre essas estações')
            return

        # Se chegar na última estação, ele vai olhar a lista de pais e usá-la para printar o caminho
        if current_station == last_station:
            path = []

            # Os pais da primeira estação são ela mesma, então para quando parar na primeira estação e depois
            # faz o append dela na lista para ela não ficar sem a primeira estação
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

        # Aux guarda todas fronteiras que já passou
        aux = []
        # Esse "for" calcula a distancia da estação atual para todos vizinhos da estação atual (escolhida na linha 45).
        for (station, distance) in self.neighborhood(current_station):
            # Se a estação não foi visitada nem seus vizinhos foram visitados, vai adicionar a distancia em min
            # no g e adicionar a estação em visitada
            if station not in visited_stations and station not in visited_neighbors:
                visited_stations.add(station)
                parents[station] = current_station
                color_line_anterior = self.find_color(parents[current_station], current_station)
                color_line_aux = self.find_color(current_station, station)
                if color_line_anterior != color_line_aux and color_line_aux != "-" and color_line_anterior != "-":
                    g[station] = g[current_station] + distance + 4 * 60
                else:
                    g[station] = g[current_station] + distance 
                aux.append((station, f'{g[station]/60:.2f}', color_line_aux))
            # Se a "station" já foi visitada ou seus vizinhos foram visitados, vai ver se acha uma distância do inicio até 
            # o "station" menor do que a que já existia em g{}. Se achar ela substitui o g[station] pela menor. 
            else:
                if g[station] > g[current_station] + distance:
                    # g[station] = g[current_station] + distance
                    parents[station] = current_station

                    if station in visited_neighbors:
                        visited_neighbors.remove(station)
                        visited_stations.add(station)
                        
                    color_line_anterior = self.find_color(parents[current_station], current_station)
                    color_line_aux = self.find_color(current_station, station)
                    if color_line_anterior != color_line_aux and color_line_aux != "-" and color_line_anterior != "-":
                        g[station] = g[current_station] + distance + 4 * 60
                    else:
                        g[station] = g[current_station] + distance 
                    color_line_aux = self.find_color(current_station, station)
                    aux.append((station, f'{g[station]/60:.2f}', color_line_aux))

        print(f'Fronteiras de {first_station} - {current_station}: {aux}')
        visited_stations.remove(current_station)
        visited_neighbors.add(current_station)

      print('Não há caminhos')

if __name__ == "__main__":
    reader = AdjacencyList("./data/real-distance.csv")
    adj_list = reader.read()
    result = Graph(adj_list)
    print("Exemplo 1:")
    result.a_star("E7", "E11")
    print()
    print("Exemplo 2:")
    result.a_star("E12", "E2")


