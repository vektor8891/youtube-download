from pytube import YouTube


def download_video(url, path, filename):
    yt = YouTube(url)
    yt.streams.first().download(output_path=path, filename=filename)


# Use the function
download_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ',
               'output', 'my_video')
