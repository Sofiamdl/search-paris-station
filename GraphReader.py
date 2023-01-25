
class GraphReader:

    def __init__(self, path, isColor=False):
        self.__path = path
        self.__matrix = []
        self.__isColor = isColor

    
    def read(self):
        isHeader = True
        
        with open(self.__path, 'r') as data:
            for line in data:
                line = line.strip()
                nodes = line.split(";")
                if isHeader:
                    isHeader = False
                    continue
                else:
                    newLine = self.parseColor(nodes) if self.__isColor else self.parseFloat(nodes)
                    self.__matrix.append(newLine)
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
    reader = GraphReader("./color-lines.csv", True)
    lista = reader.read()
    print(lista)

