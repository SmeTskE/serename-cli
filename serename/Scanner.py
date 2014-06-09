import os

class Scanner:

    def __init__(self):
        pass

    def remove_filename_extension(self, f):
        filename = ""
        if f[-4:].lower() in [".avi", ".mp4", ".mkv"]:
            filename = f[0:-4]
        elif f[-4:].lower() in [".srt", ".sub"]:
            if f[-7:-4].lower() in [".en", ".nl"]:
                filename = f[0:-7]
            else:
                filename = f[0:-4]

        return filename

    def scan_directory(self, directory):
        return os.listdir(directory)

