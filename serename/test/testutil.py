import os
import shutil

TEST_DIR = "test_data"


EPISODES = [
    "The.Walking.Dead.s01e01.x264.mp4",
    "The.Walking.Dead.s01e01.x264.en.srt",
    "The.Walking.Dead.S01E02.mp4",
    "The.Walking.Dead.S01E02.srt",
    "The.Walking.Dead.103.x264.mp4",
    "The.Walking.Dead.103.x264.sub"
]

EPISODES_EXPECTED = [
    "The.Walking.Dead.s01e01.x264",
    "The.Walking.Dead.S01E02",
    "The.Walking.Dead.103.x264"
]

EPISODES_EXTENSIONS = {
    "avi": "The.Walking.Dead.avi",
    "mkv": "The.Walking.Dead.mkv",
    "mp4": "The.Walking.Dead.mp4",
    "langsrt": "The.Walking.Dead.en.srt",
    "srt": "The.Walking.Dead.srt",
    "langsub": "The.Walking.Dead.en.sub",
    "sub": "The.Walking.Dead.sub"
}

EPISODES_EXTENSIONS_EXPECTED = [
    "The.Walking.Dead"
]


def create_tmp_dir():
    os.mkdir(TEST_DIR)


def create_tmp_episodes():
    for value in EPISODES:
        tmp_file_path = os.path.join(TEST_DIR, value)
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value)
    pass


def create_tmp_episodes_extensions():
    for key, value in EPISODES_EXTENSIONS.iteritems():
        tmp_file_path = os.path.join(TEST_DIR, value[0])
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value[0])
    pass


def remove_tmp_dir():
    shutil.rmtree(TEST_DIR)


def get_expected_files_extensions():
    files_expected = []
    for key, value in EPISODES_EXTENSIONS.iteritems():
        files_expected.append(value)
    return files_expected


def get_expected_files():
    return EPISODES_EXPECTED