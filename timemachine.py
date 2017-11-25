import sys
import argparse

sys.path.insert(0, "./src")
from ConfigurationService import ConfigurationService
from CopyService import CopyService

def list(args):
    ConfigurationService().listWatchingFiles(args.config)

def add(args):
    ConfigurationService().addToWatchingFiles(args.config, args.add)

def delete(args):
    ConfigurationService().removeWatchingFile(args.config, args.delete)

def backup(args):
    watching = ConfigurationService().getFilesToWatch(args.storePath, args.config)

    for file in watching:
        if file.isFileChanged():
            CopyService().copyFileSnapshot(file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='config.dat')
    parser.add_argument("--storePath", default='.')
    parser.add_argument("--list", action = "store_true")
    parser.add_argument("--add")
    parser.add_argument("--delete")

    args = parser.parse_args()

    if args.list:
        list(args)
    elif args.add:
        add(args)
    elif args.delete:
        delete(args)
    else:
        backup(args)

if __name__ == "__main__":
    main()
