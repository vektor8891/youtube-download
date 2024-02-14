import os
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
    #keep only A-Z, 0-9 and whitespace
    title = ''.join(e for e in title if e.isalnum() or e.isspace())
    return title


def download_video(url, path, overwrite=False, extension='mp4'):
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
    filepath = os.path.join(path, f"{filename}.{extension}")
    if not overwrite and os.path.exists(filepath):
        print(f"File {filename}.{extension} already exists. Skipping download.")
        return
    YouTube(url).streams.first().download(output_path=path, filename=filename)
