from googleapiclient.discovery import build
from dotenv import load_dotenv
import os


def get_channel_videos(channel_id, output_file):
    """
    Retrieves all video links from a YouTube channel and saves them to a file.

    Args:
        channel_id (str): The ID of the YouTube channel.
        output_file (str): The path to the output file where the video links will be saved.

    Returns:
        None
    """
    # load .env from home directory
    load_dotenv(dotenv_path=os.path.expanduser('~/.env'))

    api_key = os.getenv('API_KEY')

    youtube = build('youtube', 'v3', developerKey=api_key)

    video_links = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part='id',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type='video'
        )

        response = request.execute()

        video_links += ['https://www.youtube.com/watch?v=' +
                        item['id']['videoId'] for item in response['items']]

        next_page_token = response.get('nextPageToken')

        if next_page_token is None:
            break

    with open(output_file, 'w') as f:
        for url in video_links:
            f.write(url + '\n')
