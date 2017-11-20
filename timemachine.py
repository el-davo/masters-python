import os.path, sys
import argparse
sys.path.insert(0, "./src")
from FileReader import FileReader

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config")
    args = parser.parse_args()

    configFile = args.config if args.config else "config.dat"

    watchingFiles = FileReader(configFile).readFileLines()

    for file in watchingFiles:
        print(file)

if __name__ == "__main__":
    main()