import hashlib
import os.path
from FileIO import FileIO

"""
Holds information about watched files
"""
class WatchingFile:

    def __init__(self, storePath, path):
        self.storePath = storePath
        self.path = path
        self.filename = os.path.basename(path).decode('utf-8')

    """
    Returns the location of the backups folder
    """
    def getStorePath(self):
        return self.storePath

    """
    Returns the fully qualified path the watched file
    """
    def getPath(self):
        return self.path

    """
    Returns only the filename without the path
    """
    def getFilename(self):
        return self.filename

    """
    Returns the last modification time of the watched file
    """
    def getLastModificationTime(self):
        return FileIO().getFileLastModificationTime(self.getPath())

    """
    Returns the path to the last modification time file
    """
    def getStoredLastModificationTimePath(self):
        return os.path.join(self.getStorePath(), self.getPathHash(), 'last-modification-date.txt')

    """
    Returns the last stored modification time of the watched file
    """
    def getStoredLastModificationTime(self):
        try:
            return FileIO().readFileLines(self.getStoredLastModificationTimePath())[0].decode('UTF-8')
        except:
            return ''

    """
    Creates a hash of the file path
    """
    def getPathHash(self):
        return hashlib.sha224(self.path).hexdigest()

    """
    Checks if a file has been modified by checking the modified metadata
    on the file against our stored modification time
    """
    def isFileChanged(self):
        return self.getStoredLastModificationTime() != self.getLastModificationTime()
