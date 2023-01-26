
from FileReader import FileReader
from GraphReaderType import GraphReaderType
class GraphReader:

    def __init__(self, path: str, typeReader: GraphReaderType = GraphReaderType.NORMAL):
        self.__path = path
        self.__matrix = []
        self.__isColor: bool = typeReader.value

    def read(self):
        header, data = FileReader().read(self.__path)

        for node in data:
            node_values = self.parseColor(node) if self.__isColor else self.parseFloat(node)
            self.__matrix.append(node_values)

        return self.__matrix if self.__isColor else self.__fixDirection()

    def parseColor(self, nodes):
        key = nodes.pop(0)
        return nodes

    def __toFloat(self,number):
        if number == "-": return 0.0
        return float(number.replace(",", "."))

    def __fixDirection(self):
        for row in range(14):
            for column in range(14):
                if self.__matrix[row][column] != 0:
                    self.__matrix[column][row] = self.__matrix[row][column]
                else:
                    self.__matrix[row][column] = self.__matrix[column][row]
        return self.__matrix
                     
    def parseFloat(self, nodes):
        key = nodes.pop(0)
        return list(map(self.__toFloat, nodes))

if __name__ == "__main__":
    reader = GraphReader("./direct-distance.csv")
    lista = reader.read()
    print(lista)
    reader = GraphReader("./color-lines.csv", GraphReaderType.COLOR)
    lista = reader.read()
    print(lista)

