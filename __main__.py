import os.path, sys
sys.path.insert(0, "./src")
from FileReader import FileReader

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    watchingFiles = FileReader(args[0]).readFileLines()

    for file in watchingFiles:
        print(file)

if __name__ == "__main__":
    main()