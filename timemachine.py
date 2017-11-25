import sys
import argparse

sys.path.insert(0, "./src")
from ConfigurationService import ConfigurationService
from CopyService import CopyService


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='config.dat')
    parser.add_argument("--storePath", default='.')
    args = parser.parse_args()

    watching = ConfigurationService().getFilesToWatch(args.config)

    for file in watching:
        CopyService().copyFileSnapshot(args.storePath, file)


if __name__ == "__main__":
    main()
