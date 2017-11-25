import hashlib
from os.path import basename

class WatchingFIle:

    def __init__(self, path):
        self.path = path
        self.filename = basename(path)

    def getPath(self):
        return self.path

    def getFilename(self):
        return self.filename

    def getPathHash(self):
        return hashlib.sha224(self.path).hexdigest()
