import requests
from bs4 import BeautifulSoup

from pytube import YouTube


def get_video_title(url):
    """
    Get the title of a YouTube video.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        str: The title of the YouTube video.
    """
    youtube = YouTube(url)
    return youtube.title


def slugify_title(title):
    """
    Converts a given title into a slug format.

    Args:
        title (str): The title to be slugified.

    Returns:
        str: The slugified title.

    """
    return title.replace(' ', '_').replace('-', '_').replace('|', '-').replace('/', '-').lower()


def download_video(url, path):
    """
    Downloads a video from the given URL and saves it to the specified path.

    Args:
        url (str): The URL of the video to download.
        path (str): The path where the downloaded video will be saved.

    Returns:
        None
    """
    title = get_video_title(url)
    filename = slugify_title(title)
    yt = YouTube(url)
    yt.streams.first().download(output_path=path, filename=filename)
