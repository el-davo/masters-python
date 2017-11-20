import os.path, sys
import argparse
sys.path.insert(0, "./src")
from FileReader import FileReader

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='config.dat')
    args = parser.parse_args()

    watchingFiles = FileReader(args.config).readFileLines()

    for file in watchingFiles:
        print(file)

if __name__ == "__main__":
    main()