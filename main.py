import os
from lib.download_video import download_video
from lib.get_channel_videos import get_channel_videos

url_path = 'output/little_bear.txt'
channel_id = 'UCncFzSeWqySvOXEbQoEJsZg'
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
    # with open(url_path, 'r') as f:
    #     for line in f:
    #         print(f'Downloading {line.strip()}')
    #         url = line.strip()
    #         download_video(url, 'output')


if __name__ == "__main__":
    main()
