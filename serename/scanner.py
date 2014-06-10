import os
from episode import Episode


class Scanner:

    def __init__(self, directory):
        self.directory = directory
        pass

    @staticmethod
    def remove_filename_extension(f):
        filename = ""
        if f[-4:].lower() in [".avi", ".mp4", ".mkv"]:
            filename = f[0:-4]
        elif f[-4:].lower() in [".srt", ".sub"]:
            if f[-7:-4].lower() in [".en", ".nl"]:
                filename = f[0:-7]
            else:
                filename = f[0:-4]
        return filename

    def get_files(self):
        return os.listdir(self.directory)

    def get_episodes(self):
        file_names = self.get_files()
        episodes = {}
        for file_name in file_names:
            episode_name = Scanner.remove_filename_extension(file_name)
            __episode = episodes.get(episode_name)
            if __episode is None:
                __episode = Episode({
                    "name": episode_name,
                    "files": [file_name]
                })
            else:
                __episode.files.append(file_name)
                __episode.files.sort()
            episodes[episode_name] = __episode
        return episodes
