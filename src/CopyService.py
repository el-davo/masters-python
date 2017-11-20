from FileIO import FileIO
import hashlib

class CopyService:

    def copyFiles(self, pathTo, filesFrom):
        for file in watchingFiles:
            print(file)
            fileLines = FileIO().readFileLines(file)
            FileIO().writeFileLines()

    def generateFileHash(self, file):
        return hashlib.sha224(file).hexdigest()
        
