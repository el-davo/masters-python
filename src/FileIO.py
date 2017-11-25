import datetime
import os
import shutil

class FileIO:
    def readFileLines(self, file):
        try:
            openFile = open(file, 'r')
            lines = []

            for line in openFile:
                lines.append(line.rstrip('\r\n').encode('utf-8'))

            return lines
        except IOError:
            print('Error: File does not appear to exist')
            return None

    def copyFile(self, src, dst):
        shutil.copy2(src, dst)

    def writeFileLines(self, file, lines):

        itemsfile = open(file, 'w')
        for line in lines:
            itemsfile.write(line.decode('utf-8'))
            itemsfile.write("\n")

        itemsfile.close()

    def writeFileLine(self, file, txt):
        itemsfile = open(file, 'w')
        itemsfile.write(txt)
        itemsfile.write("\n")
        itemsfile.close()

    def addLineToFile(self, file, newLine):
        with open(file, 'a') as appendFile:
            appendFile.write('\n' + newLine)

    def fileExists(self, file):
        return os.path.exists(file)

    def createDirIfNotExists(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def getFileLastModificationTime(self, path):
        timestamp = os.path.getmtime(path)
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')
