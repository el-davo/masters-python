from FileIO import FileIO
from WatchingFile import WatchingFIle

class ConfigurationService:

    def getFilesToWatch(self, configFile):
        files = FileIO().readFileLines(configFile)
        watchingFiles = [];
        for file in files:
            watchingFiles.append(WatchingFIle(file))

        return watchingFiles
