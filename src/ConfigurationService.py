from FileIO import FileIO
from WatchingFile import WatchingFile

"""
Handles configuration related activities
"""
class ConfigurationService:

    """
    Gets a list of currently watched files
    """
    def getFilesToWatch(self, storePath, configFile):
        files = FileIO().readFileLines(configFile)
        watchingFiles = []
        for file in files:
            watchingFiles.append(WatchingFile(storePath, file))

        return watchingFiles

    """
    Lists the files that we are currently watching
    """
    def listWatchingFiles(self, configFile):
        files = FileIO().readFileLines(configFile)
        for file in files:
            print(file.decode('UTF-8'))

    """
    Adds a new file to the list of watched files
    """
    def addToWatchingFiles(self, configFile, file):
        if FileIO().fileExists(file):
            if FileIO().isLineInFile(configFile, file):
                print('File has not been added to config as it already exists in the config file')
            else:
                FileIO().addLineToFile(configFile, file)
                print('File has been successfully added, we will monitor for changes')
        else:
            print('Unable to add, File does not exist')

    """
    Removes a file from the list of watched files
    """
    def removeWatchingFile(self, configFile, removeLine):
        if FileIO().isLineInFile(configFile, removeLine):
            FileIO().removeLineFromFile(configFile, removeLine)
            print('File has been removed')
        else:
            print('File is not in config file, Skipping remove')
