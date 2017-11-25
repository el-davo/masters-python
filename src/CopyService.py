import os.path
from FileIO import FileIO

class CopyService:

    def copyFileSnapshot(self, pathTo, file):
        fileLines = FileIO().readFileLines(file.getPath())
        copyPath = os.path.join(pathTo, file.getPathHash(), FileIO().getFileLastModificationTime(file))

        FileIO().createDirIfNotExists(copyPath)

        FileIO().writeFileLines(os.path.join(copyPath, file.getFilename), fileLines)

