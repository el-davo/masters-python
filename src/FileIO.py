import datetime
import os
import shutil

"""
Handles all file related activities
"""
class FileIO:
    """
    Returns a list of lines from a given file
    """
    def readFileLines(self, file):
        try:
            openFile = open(file, 'r')
            lines = []

            for line in openFile:
                lines.append(line.rstrip('\r\n').encode('utf-8'))

            return lines
        except IOError:
            return None

    """
    Copies a file from a source to a given destination
    """
    def copyFile(self, src, dst):
        shutil.copy2(src, dst)

    """
    Writes a list of lines to a file in bulk
    """
    def writeFileLines(self, file, lines):

        itemsfile = open(file, 'w')
        for line in lines:
            itemsfile.write(line.decode('utf-8'))
            itemsfile.write("\n")

        itemsfile.close()

    """
    Writes a file with a single line of text
    """
    def writeFileLine(self, file, txt):
        itemsfile = open(file, 'w')
        itemsfile.write(txt)
        itemsfile.write("\n")
        itemsfile.close()

    """
    Appends a line to an existing file
    """
    def addLineToFile(self, file, newLine):
        with open(file, 'a') as appendFile:
            appendFile.write('\n' + newLine)

    """
    Checks if a file exists
    """
    def fileExists(self, file):
        return os.path.exists(file)

    """
    Removes a specific line from a file. The removeLine parameter must match exactly to a line to be removed
    """
    def removeLineFromFile(self, file, removeLine):
        r = open(file, 'rt')
        lines = r.readlines()
        r.close()

        w = open(file, 'wt')
        for line in lines:
            if line.strip('\n') != removeLine:
                w.write(line)
        w.close()

    """
    Creates a directory if it does not already exist. If it does exist then do not create the directory
    """
    def createDirIfNotExists(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    """
    Retrieves the last modification time of a file
    """
    def getFileLastModificationTime(self, path):
        timestamp = os.path.getmtime(path)
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')
