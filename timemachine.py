import sys
import argparse

sys.path.insert(0, "./src")
from ConfigurationService import ConfigurationService
from BackupService import BackupService

def list(args):
    ConfigurationService().listWatchingFiles(args.config)

def add(args):
    ConfigurationService().addToWatchingFiles(args.config, args.add)

def remove(args):
    ConfigurationService().removeWatchingFile(args.config, args.remove)

def backup(args):
    BackupService().backup(args.storePath, args.config)

"""
Entry point for parsing arguments

command 

    python3 ./timemachine.py --help
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.dat', help='Path to configuration file for watched files')
    parser.add_argument('--storePath', default='./backup', help='Path to store backups under')
    parser.add_argument('--list', action='store_true', help='List all files currently being watched')
    parser.add_argument('--add', help='Add a new file to be watched')
    parser.add_argument('--remove', help='Removes a file from the list of watched files')

    args = parser.parse_args()

    if args.list:
        list(args)
    elif args.add:
        add(args)
    elif args.remove:
        remove(args)
    else:
        backup(args)

if __name__ == "__main__":
    main()
