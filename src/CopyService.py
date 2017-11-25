import os.path
from FileIO import FileIO

class CopyService:

    def copyFileSnapshot(self, file):
        copyPath = os.path.join(file.getStorePath(), file.getPathHash(), file.getLastModificationTime())
        FileIO().createDirIfNotExists(copyPath)
        FileIO().copyFile(file.getPath().decode('UTF-8'), copyPath)
        self.updateModicationDate(file)

    def updateModicationDate(self, file):
        FileIO().writeFileLine(file.getStoredLastModificationTimePath(), file.getLastModificationTime())

