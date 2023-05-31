"""Download playlist"""
from pytube import Playlist
from pytube.cli import on_progress

def download_playlist(url: str, path: str, video_format: str) -> None:
    """
    Get the videos from the playlist and download them
    * Args:
        \t - url (str): playlist url
        \t - path (str): Directory where the files will be saved
        \t - video_format (str): User-supplied video format (video or audio)
    """
    playlist = Playlist(url).videos
    for stream in playlist:
        stream.register_on_progress_callback(on_progress)
        if video_format == "video":
            video = stream.streams.get_highest_resolution()
            stream.download(path)
        elif video_format == "audio":
            video = stream.streams.get_audio_only()
            video.download(path)
        print("\n")

