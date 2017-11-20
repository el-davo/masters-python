import os.path, sys
import argparse
import hashlib
sys.path.insert(0, "./src")
from FileIO import FileIO
from CopyService import CopyService

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='config.dat')
    parser.add_argument("--storePath", default='.')
    args = parser.parse_args()

    watchingFiles = FileIO().readFileLines(args.config)

    CopyService().copyFiles(args.storePath, watchingFiles)

if __name__ == "__main__":
    main()