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
    # replace | and / with hyphen
    title = title.replace('|', '-').replace('/', '-')
    # keep only A-Z, 0-9, whitespace and hyphen
    title = ''.join(e for e in title if e.isalnum() or e.isspace() or e == '-')
    return title


def download_video(url, path, overwrite=False, extension='mp4', skip_words=None):
    """
    Downloads a video from the given URL and saves it to the specified path.

    Args:
        url (str): The URL of the video to download.
        path (str): The path where the downloaded video will be saved.
        overwrite (bool, optional): If set to True, the video will be downloaded even if a file with the same name already exists in the specified path. Defaults to False.
        extension (str, optional): The file extension of the downloaded video. Defaults to 'mp4'.
        skip_words (list, optional): A list of words. If any of these words are found in the video title, the download will be skipped. Defaults to None.

    Returns:
        None
    """
    title = get_video_title(url)
    if skip_words and any(word in title.lower() for word in skip_words):
        print(f"Skipping {title} because it contains one of the skip words.")
        return
    title_slug = slugify_title(title)
    filename = f"{title_slug}.{extension}"
    filepath = os.path.join(path, filename)
    if not overwrite and os.path.exists(filepath):
        print(f"{filename} already exists. Skipping download.")
        return
    print(f'Downloading {url} into {filename}')
    YouTube(url).streams.first().download(output_path=path, filename=filename)
