class Episode:

    def __init__(self, data):
        self.name = data["name"]
        self.files = data["files"]
        pass

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ and self.files.sort() == other.files.sort()
