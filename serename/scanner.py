from functools import partial
import hashlib
import os
from serename.episode import Episode


class Scanner:

    def __init__(self, directory=None):
        self.directory = os.getcwd()
        if directory is not None:
            self.directory = directory

    @staticmethod
    def get_file_hash(filename):
        result = ""
        md5 = hashlib.md5()
        with open(filename,'rb') as f:
            for chunk in iter(lambda: f.read(md5.block_size), b''):
                md5.update(chunk)
            result = md5.hexdigest()
        return result

    @staticmethod
    def get_filename_hash(file_name):
        return hashlib.md5(file_name.encode('utf-8')).hexdigest()

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

    def generate_xml(self):
        __episodes = self.get_episodes()
        print(__episodes)

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

    def get_files(self):
        return os.listdir(self.directory)
