"""Download playlist"""
from pytube import Playlist
from pytube.cli import on_progress
from src.validations.visibility import is_video_private

def download_playlist(url: str, path: str, video_format: str) -> None:
    """
    Get the videos from the playlist and download them
    * Args:
        \t - url (str): playlist url
        \t - path (str): Directory where the files will be saved
        \t - video_format (str): User-supplied video format (video or audio)
    """
    playlist = Playlist(url).videos
    for video in playlist:
        private = is_video_private(video)
        video.register_on_progress_callback(on_progress)
        if not video.age_restricted and not private:
            if video_format == "video":
                video.streams \
                .get_highest_resolution() \
                .download(path)
            elif video_format == "audio":
                video.streams \
                .get_audio_only() \
                .download(path)
            print("\n")