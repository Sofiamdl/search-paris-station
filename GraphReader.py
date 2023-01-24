import csv

class GraphReader:

    def __init__(self, path):
        self.__path = path
        self.__adjacency_list = {}

    
    def read(self):
        isHeader = True

        with open(self.__path, 'r') as data:
            for line in data:
                line = line.strip()
                nodes = line.split(";")
                if isHeader:
                    nodes = nodes[1::]
                    self.__getNodes(nodes)
                    isHeader = False
                else:
                    self.__getValues(nodes)

        return self.__adjacency_list
    
    def __getNodes(self, nodes):
        for node in nodes:
            self.__adjacency_list[node] =[]

    def __getValues(self, nodes):
        key = nodes.pop(0)
        for index, value in enumerate(nodes):
            if value == "-": continue
            newNode = (f'E{index+1}', float(value.replace(',', '.')))
            self.__adjacency_list[key].append(newNode)

if __name__ == "__main__":
    reader = GraphReader("./real-distance.csv")
    adj_list = reader.read()
    print(adj_list)

