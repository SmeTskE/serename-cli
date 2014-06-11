import os
import shutil
from serename.episode import Episode

TEMP_DIR = "temp_data"


EPISODES_FILES = [
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
    "The.Walking.Dead.103.x264",
    "The.Walking.Dead"
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
    os.mkdir(TEMP_DIR)


def create_tmp_episodes():
    for value in EPISODES_FILES:
        tmp_file_path = os.path.join(TEMP_DIR, value)
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value)


def create_tmp_episodes_extensions():
    for key, value in EPISODES_EXTENSIONS.iteritems():
        tmp_file_path = os.path.join(TEMP_DIR, value)
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value)


def remove_tmp_dir():
    shutil.rmtree(TEMP_DIR)


def get_expected_files_extensions():
    files_expected = []
    for key, value in EPISODES_EXTENSIONS.iteritems():
        files_expected.append(value)
    return files_expected


def get_expected_files():
    expected_files = []
    for key, value in EPISODES_EXTENSIONS.iteritems():
        expected_files.append(value)
    for value in EPISODES_FILES:
        expected_files.append(value)
    return expected_files


def get_expected_episodes():
    twd_files = [
        "The.Walking.Dead.avi",
        "The.Walking.Dead.mkv",
        "The.Walking.Dead.mp4",
        "The.Walking.Dead.en.srt",
        "The.Walking.Dead.srt",
        "The.Walking.Dead.en.sub",
        "The.Walking.Dead.sub"
    ]
    twd01_files = [
        "The.Walking.Dead.s01e01.x264.mp4",
        "The.Walking.Dead.s01e01.x264.en.srt"
    ]
    twd02_files = [
        "The.Walking.Dead.S01E02.mp4",
        "The.Walking.Dead.S01E02.srt"
    ]
    twd03_files = [
        "The.Walking.Dead.103.x264.mp4",
        "The.Walking.Dead.103.x264.sub"
    ]

    twd_files.sort()
    twd01_files.sort()
    twd02_files.sort()
    twd03_files.sort()

    return {
        "The.Walking.Dead": Episode({
            "name": "The.Walking.Dead",
            "files": twd_files
        }),
        "The.Walking.Dead.s01e01.x264": Episode({
            "name": "The.Walking.Dead.s01e01.x264",
            "files": twd01_files
        }),
        "The.Walking.Dead.S01E02": Episode({
            "name": "The.Walking.Dead.S01E02",
            "files": twd02_files
        }),
        "The.Walking.Dead.103.x264": Episode({
            "name": "The.Walking.Dead.103.x264",
            "files": twd03_files
        })
    }