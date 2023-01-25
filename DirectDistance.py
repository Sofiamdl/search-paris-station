
class DirectDistance:

    def __init__(self, path):
        self.__path = path
        self.__matrix = []

    
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
                    newLine = self.parseFloat(nodes)
                    self.__matrix.append(newLine)
        print(self.__matrix)

    def __toFloat(self,number):
        if number == "-": return 0.0
        return number.replace(",", ".")

    def parseFloat(self, nodes):
        key = nodes.pop(0)
        return list(map(self.__toFloat, nodes))

if __name__ == "__main__":
    teste = DirectDistance("./direct-distance.csv")
    teste.read()
