import os.path, sys
sys.path.insert(0, "./src")
from FileReader import FileReader

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    configFile = args[0] if len(args) > 0 else "config.dat"

    watchingFiles = FileReader(configFile).readFileLines()

    for file in watchingFiles:
        print(file)

if __name__ == "__main__":
    main()