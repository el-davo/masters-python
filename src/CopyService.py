import os.path
from FileIO import FileIO

class CopyService:

    def copyFileSnapshot(self, file):
        fileLines = FileIO().readFileLines(file.getPath())
        copyPath = os.path.join(file.getStorePath(), file.getPathHash(), file.getLastModificationTime())
        FileIO().createDirIfNotExists(copyPath)
        FileIO().writeFileLines(os.path.join(copyPath, file.getFilename()), fileLines)
        self.updateModicationDate(file)

    def updateModicationDate(self, file):
        FileIO().writeFileLine(file.getStoredLastModificationTimePath(), file.getLastModificationTime())

