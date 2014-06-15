#!/usr/bin/env python3
from serename.scanner import Scanner
import os

class Serename:

    def __init__(self):
        pass

    def generate_xml(self, directory):
        __scanner = Scanner(directory)
        __scanner.generate_xml()

    def rename_files(self, input_file):

        pass


def main(args):
    input_file = args["input_file"]
    serename = Serename()
    if args.get("generate") is not None:
        serename.generate_xml(args.get("directory"))
    elif input_file is not None:
        serename.rename_files(input_file)


if __name__ == "__main__":
    #TODO: Use argparse
    arguments = {"generate": True, "input_file": None}
    main(arguments)
