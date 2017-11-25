import os.path
from FileIO import FileIO

"""
Handles copy related activities
"""
class CopyService:

    """
    Creates a snapshot of a file in the given backup directory
    """
    def copyFileSnapshot(self, file):
        copyPath = os.path.join(file.getStorePath(), file.getPathHash(), file.getLastModificationTime())
        FileIO().createDirIfNotExists(copyPath)
        FileIO().copyFile(file.getPath().decode('UTF-8'), copyPath)
        self.updateModicationDate(file)

    """
    Creates a file which holds the last modification date for use in future comparisons
    """
    def updateModicationDate(self, file):
        FileIO().writeFileLine(file.getStoredLastModificationTimePath(), file.getLastModificationTime())
        print('Backed up: ' + file.getPath().decode('UTF-8'))

