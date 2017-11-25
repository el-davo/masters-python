from FileIO import FileIO
from WatchingFile import WatchingFIle

class ConfigurationService:

    def getFilesToWatch(self, storePath, configFile):
        files = FileIO().readFileLines(configFile)
        watchingFiles = [];
        for file in files:
            watchingFiles.append(WatchingFIle(storePath, file))

        return watchingFiles

    def listWatchingFiles(self, configFile):
        files = FileIO().readFileLines(configFile)
        for file in files:
            print(file.decode('UTF-8'))
