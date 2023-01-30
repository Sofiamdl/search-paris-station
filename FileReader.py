from CharacterEnum import Character
from Alias import Header, Graph

class FileReader:

    def read(self, path: str) -> (Header, Graph):
        isHeader: bool = True

        header: Header = []
        content: Graph = []
    
        with open(path, 'r') as data:
            for line in data:
                line = line.strip()
                nodes = line.split(Character.LINE_SEPARATOR.value)
                if isHeader:
                    header = nodes
                    isHeader = False
                else:
                    content.append(nodes)

        header.pop(0)
        return (header, content)
