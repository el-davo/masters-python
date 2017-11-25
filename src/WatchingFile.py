import hashlib
from os.path import basename
from FileIO import FileIO

class WatchingFIle:

    def __init__(self, path):
        self.path = path
        self.filename = basename(path).decode("utf-8")

    def getPath(self):
        return self.path

    def getFilename(self):
        return self.filename

    def getLastModificationTime(self):
        return FileIO().getFileLastModificationTime(self.getPath())

    def getPathHash(self):
        return hashlib.sha224(self.path).hexdigest()
