class Serename:

    def __init__(self):
        pass

    def generate_xml(self):
        pass

    def rename_files(self, input_file):
        pass


def main(args):
    input_file = args["input_file"]
    serename = Serename()
    if args["generate"]:
        serename.generate_xml()
    elif input_file is not None:
        serename.rename_files(input_file)


if __name__ == "__main__":
    #TODO: Use argparse
    args = {"generate": True, "input_file": None}
    main(args)