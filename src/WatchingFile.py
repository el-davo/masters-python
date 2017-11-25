import hashlib
import os.path
from FileIO import FileIO

class WatchingFIle:

    def __init__(self, storePath, path):
        self.storePath = storePath
        self.path = path
        self.filename = os.path.basename(path).decode('utf-8')

    def getStorePath(self):
        return self.storePath

    def getPath(self):
        return self.path

    def getFilename(self):
        return self.filename

    def getLastModificationTime(self):
        return FileIO().getFileLastModificationTime(self.getPath())

    def getStoredLastModificationTimePath(self):
        return os.path.join(self.getStorePath(), self.getPathHash(), 'last-modification-date.txt')

    def getStoredLastModificationTime(self):
        try:
            return FileIO().readFileLines(self.getStoredLastModificationTimePath())[0].decode('UTF-8')
        except:
            return ''

    def getPathHash(self):
        return hashlib.sha224(self.path).hexdigest()

    def isFileChanged(self):
        return self.getStoredLastModificationTime() != self.getLastModificationTime()
