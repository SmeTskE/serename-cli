class Episode:

    def __init__(self, data=None):
        self.name = ""
        self.files = []
        self.series = ""
        self.episode_nr = 0
        self.episode_title = ""
        self.season_nr = 0
        if data is not None:
            if data.get("name") is not None:
                self.name = data["name"]
            if data.get("files") is not None:
                self.files = data["files"]
            if data.get("series") is not None:
                self.series = data["series"]
            if data.get("episode_nr") is not None:
                self.episode_nr = data["episode_nr"]
            if data.get("episode_title") is not None:
                self.episode_title = data["episode_title"]
            if data.get("season_nr") is not None:
                self.season_nr = data["season_nr"]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ and self.files.sort() == other.files.sort()
