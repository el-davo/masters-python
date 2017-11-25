from FileIO import FileIO
from WatchingFile import WatchingFIle

class ConfigurationService:

    def getFilesToWatch(self, storePath, configFile):
        files = FileIO().readFileLines(configFile)
        watchingFiles = []
        for file in files:
            watchingFiles.append(WatchingFIle(storePath, file))

        return watchingFiles

    def listWatchingFiles(self, configFile):
        files = FileIO().readFileLines(configFile)
        for file in files:
            print(file.decode('UTF-8'))

    def addToWatchingFiles(self, configFile, file):
        if FileIO().fileExists(file):
            FileIO().addLineToFile(configFile, file)
            print('File has been successfully added, we will monitor for changes')
        else:
            print('Unable to add, File does not exist')

    def removeWatchingFile(self, configFile, removeLine):
        FileIO().removeLineFromFile(configFile, removeLine)
        print('File has been removed')
