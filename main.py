import os
import itertools
from lib.download_video import download_video
from lib.get_channel_videos import get_channel_videos

# Little Bear
url_path = 'output/little_bear.txt'
channel_id = 'UCncFzSeWqySvOXEbQoEJsZg'
# Bogyo es Baboca
# url_path = 'output/bogyo_es_baboca.txt'
# channel_id = 'UCmsxuZrnb-MNYpqPd-XxLog'
# Wall-E
# url_path = 'output/wall_e.txt'
# channel_id = 'UCGh0buCqdEGegoIkU8ZVxuQ'
max_videos = 1
overwrite = False


def main():
    """
    This function is the entry point of the program.
    It retrieves the channel videos, reads the URLs from a file,
    and downloads the videos one by one.
    """
    if overwrite and os.path.exists(url_path):
        os.remove(url_path)
    if not os.path.exists(url_path):
        get_channel_videos(channel_id, url_path)
    with open(url_path, 'r') as f:
        for line in itertools.islice(f, max_videos):
            print(f'Downloading {line.strip()}')
            url = line.strip()
            download_video(url, 'output')


if __name__ == "__main__":
    main()
