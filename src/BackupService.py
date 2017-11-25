from ConfigurationService import ConfigurationService
from CopyService import CopyService
from FileIO import FileIO

"""
Service which handles backups
"""
class BackupService:

    def backup(self, storePath, config):
        watching = ConfigurationService().getFilesToWatch(storePath, config)

        for file in watching:
            if FileIO().fileExists(file.getPath()):
                if file.isFileChanged():
                    CopyService().copyFileSnapshot(file)
            else:
                print('Warning: ' + file.getPath().decode('UTF-8') + ' does not exist, skipping')