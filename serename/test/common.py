import os
import shutil
from serename.episode import Episode

TEMP_DIR = "temp_data"
TEMP_DIR_EPISODES = "temp_data_episodes"

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

EPISODES = [
    Episode({
        "name": "The.Walking.Dead.S03E01.x264-2HD.[VTV]",
        "series": "The Walking Dead",
        "episode_nr": "1",
        "episode_title": "Seed",
        "season_nr": "3",
        "files": [
            {
                "file_name": "The.Walking.Dead.S03E01.x264-2HD.[VTV].mp4",
                "filename_md5": "5931726081fb60cacf0ddd1aea79c9cc",
                "content_md5": "243923cfc116b2bc5456b30acf2e9ebe",
                "dummy_content": b'This is episode 01 - Seed\n'
            },
            {
                "file_name": "The.Walking.Dead.S03E01.x264-2HD.[VTV].en.srt",
                "filename_md5": "3a9d74c55135ef265dda631756fe2c9b",
                "content_md5": "2465e893ebf6f4ee10aebd122b0a6135",
                "dummy_content": b'This is the English subtitle for episode 01 - Seed\n'
            },
            {
                "file_name": "The.Walking.Dead.S03E01.x264-2HD.[VTV].nl.srt",
                "filename_md5": "c3c5c7647b971a436587be4b5fcfce24",
                "content_md5": "71b0119f189dbf51e32cfca7c755baa6",
                "dummy_content": b'This is the Dutch subtitle for episode 01 - Seed\n'
            },
        ]
    })
]


def create_tmp_dir():
    os.mkdir(TEMP_DIR)
    os.mkdir(TEMP_DIR_EPISODES)


def create_tmp_episodes():
    for value in EPISODES_FILES:
        tmp_file_path = os.path.join(TEMP_DIR, value)
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value)

    for __episode in EPISODES:
        for __file in __episode.files:
            tmp_file_path = os.path.join(TEMP_DIR_EPISODES, __file["file_name"])
            tmp_file = open(tmp_file_path, 'wb')
            tmp_file.write(__file['dummy_content'])


def create_tmp_episodes_extensions():
    for key, value in EPISODES_EXTENSIONS.items():
        tmp_file_path = os.path.join(TEMP_DIR, value)
        tmp_file = open(tmp_file_path, 'w+')
        tmp_file.write(value)


def remove_tmp_dir():
    shutil.rmtree(TEMP_DIR)
    shutil.rmtree(TEMP_DIR_EPISODES)


def get_expected_files_extensions():
    files_expected = []
    for key, value in EPISODES_EXTENSIONS.items():
        files_expected.append(value)
    return files_expected


def get_expected_files():
    expected_files = []
    for key, value in EPISODES_EXTENSIONS.items():
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
