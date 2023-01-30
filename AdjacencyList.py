from CharacterEnum import Character
from FileReader import FileReader
from TrainTimer import TrainTimer
from Alias import Header, Graph

class AdjacencyList:

    __slots__ = "__path", "__adjacency_list"

    def __init__(self, path: str):
        self.__path = path
        self.__adjacency_list = {}

    def read(self):
        header, data = FileReader().read(self.__path)
        self.__set_adjacency_list_header(header)
        self.__set_adjacency_list_data(data)

        return self.__adjacency_list

    def __set_adjacency_list_header(self, header: Header):
        for node in header:
            self.__adjacency_list[node] = []

    def __set_adjacency_list_data(self, data: Graph):
        for row in data:
            self.__get_values(row)

    def __get_values(self, nodes: Header):
        key = nodes.pop(0)
        for index, time in enumerate(nodes):
            if time == "-": continue
            station = f"E{index+1}"
            seconds = TrainTimer.parseSeconds(time)
            self.__adjacency_list[key].append((station, seconds))
            self.__adjacency_list[station].append((key, seconds))

if __name__ == "__main__":
    reader = AdjacencyList("./data/real-distance.csv")
    print(reader.read())
