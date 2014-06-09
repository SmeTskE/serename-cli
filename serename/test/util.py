
TEST_DIR = "test_data"

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

EPISODES = {
    "The.Walking.Dead.s01e01.x264.mp4",
    "The.Walking.Dead.s01e01.x264.en.srt",
    "The.Walking.Dead.S01E02.mp4",
    "The.Walking.Dead.S01E02.srt",
    "The.Walking.Dead.103.x264.mp4",
    "The.Walking.Dead.103.x264.sub"
}

EPISODES_EXPECTED = {
    "The.Walking.Dead.s01e01.x264",
    "The.Walking.Dead.S01E02",
    "The.Walking.Dead.103.x264"
}

def get_expected_files_extensions():
    files_expected = []
    for key, value in EPISODES_EXTENSIONS.iteritems():
        files_expected.append(value)
    return files_expected

def get_expected_files():
    files_expected = []
    for key, value in EPISODES.iteritems():
        files_expected.append(value[0])
    return files_expected