from CharacterEnum import Character

class FileReader:

    def read(self, path: str) -> (list[str], list[list[str]]):
        isHeader: bool = True

        header: list[str] = []
        content: list[list[str]] = []
    
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
