import os.path
from FileIO import FileIO

class CopyService:

    def copyFileSnapshot(self, pathTo, file):
        fileLines = FileIO().readFileLines(file.getPath())
        copyPath = os.path.join(pathTo, file.getPathHash(), file.getLastModificationTime())
        FileIO().createDirIfNotExists(copyPath)
        FileIO().writeFileLines(os.path.join(copyPath, file.getFilename()), fileLines)
        self.updateModicationDate(pathTo, file)

    def updateModicationDate(self, pathTo, file):
        path = os.path.join(pathTo, file.getPathHash())
        FileIO().writeFileLine(os.path.join(path, 'last-modifaction-date.txt'), file.getLastModificationTime())

