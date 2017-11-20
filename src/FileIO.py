class FileIO:

    def readFileLines(self, file):

        openFile = open(file, "r")
        lines = []

        for line in openFile:
            lines.append(line)
        
        return lines

    def writeFileLines(self, file, lines):

        itemsfile = open(file, "w")
        for line in lines:
            itemsfile.write(str(line))
            itemsfile.write("\n")

        itemsfile.close()

