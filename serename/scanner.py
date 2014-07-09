import hashlib
import os
import guessit
import xml.etree.ElementTree as ET
from entity.episode import Episode


class Scanner:

    def __init__(self, directory=None):
        self.directory = os.getcwd()
        if directory is not None:
            self.directory = directory

    @staticmethod
    def get_file_hash(filename):
        result = ""
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
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
        __episodes = self.get_metadata(__episodes)

        xml_episodes = ET.Element('episodes')
        for __episode in __episodes.values():
            xml_episode = ET.SubElement(xml_episodes, 'episode')

            xml_episode_name = ET.SubElement(xml_episode, 'name')
            xml_episode_name.text = str(__episode.name)

            xml_episode_season_nr = ET.SubElement(xml_episode, 'season_nr')
            xml_episode_season_nr.text = str(__episode.season_nr)

            xml_episode_episode_nr = ET.SubElement(xml_episode, 'episode_nr')
            xml_episode_episode_nr.text = str(__episode.episode_nr)

            xml_episode_episode_title = ET.SubElement(xml_episode, 'episode_title')
            xml_episode_episode_title.text = str(__episode.episode_title)

            xml_episode_files = ET.SubElement(xml_episode, 'files')
            for __file in __episode.files:
                xml_episode_file = ET.SubElement(xml_episode_files, 'file')

                xml_episode_file_name = ET.SubElement(xml_episode_file, "name")
                xml_episode_file_name.text = __file

                xml_episode_file_hash = ET.SubElement(xml_episode_file, "hash")
                xml_episode_file_hash.text = self.get_file_hash(__file)


        tree = ET.ElementTree(xml_episodes)
        tree.write('serename.xml', xml_declaration=True, encoding='utf-8', method="xml")

 #       with open('serename.xml', 'w') as f:
 #           f.write(str(ET.dump(xml_episodes)))


    def get_metadata(self, __episodes):
        for key in __episodes:
            guessit_result = guessit.guess_file_info(key)
            __episodes[key].name = guessit_result.get('series', '')
            __episodes[key].season_nr = guessit_result.get('season', '')
            __episodes[key].episode_nr = guessit_result.get('episodeNumber', '')
            __episodes[key].episode_title = guessit_result.get('title', '')
        return __episodes

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
        files = os.listdir(self.directory)
        filtered_files = []
        for f in files:
            if f[-4:].lower() in [".avi", ".mp4", ".mkv", ".srt", ".sub"]:
                filtered_files.append(f)
        return filtered_files
