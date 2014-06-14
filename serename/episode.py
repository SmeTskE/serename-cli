class Episode:

    def __init__(self, data=None):
        print(str(data))
        self.name = ""
        self.files = []
        if data is not None:
            if data.get("name") is not None:
                self.name = data["name"]
            if data.get("files") is not None:
                self.files = data["files"]
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ and self.files.sort() == other.files.sort()

    def add_file(self, file):
        self.files.append(file)

    def add_files(self, files):
        for f in files.items():
            if f not in files.items():
                self.files.add(f)

    def get_name(self):
        return self.name

    def get_files(self):
        return self.files

    def set_files(self, files):
        self.files = files

    def set_name(self, name):
        self.name = name
