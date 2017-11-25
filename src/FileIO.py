import datetime
import os

class FileIO:

    def readFileLines(self, file):

        openFile = open(file, 'r')
        lines = []

        for line in openFile:
            lines.append(line.rstrip('\r\n').encode('utf-8'))

        return lines

    def writeFileLines(self, file, lines):

        itemsfile = open(file, 'w')
        for line in lines:
            itemsfile.write(line.decode('utf-8'))
            itemsfile.write("\n")

        itemsfile.close()

    def createDirIfNotExists(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def getFileLastModificationTime(self, file):
        timestamp = os.path.getmtime(file.getPath())
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
