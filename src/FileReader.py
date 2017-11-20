class FileReader:

    file

    def __init__(self, file):
        self.file = file

    def readFileLines(self):

        file = open(self.file, "r")
        lines = []

        for line in file:
            lines.append(line)
        
        return lines