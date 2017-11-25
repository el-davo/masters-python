import sys
import argparse

sys.path.insert(0, "./src")
from ConfigurationService import ConfigurationService
from CopyService import CopyService

def list(args):
    ConfigurationService().listWatchingFiles(args.config)

def backup(args):
    watching = ConfigurationService().getFilesToWatch(args.storePath, args.config)

    for file in watching:
        if file.isFileChanged():
            CopyService().copyFileSnapshot(file)

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='config.dat')
    parser.add_argument("--storePath", default='.')
    parser.add_argument("--list", action = "store_true")

    args = parser.parse_args()

    if args.list:
        list(args)
    else:
        backup(args)


if __name__ == "__main__":
    main()
