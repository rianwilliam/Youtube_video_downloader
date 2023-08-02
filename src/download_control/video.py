"""Download video"""
from pytube import YouTube
from pytube.cli import on_progress
from src.validations.visibility import is_video_private

def download_video(url: str, path: str, video_format: str) -> None:
    """
    Download a single video
    * Args:
        \t - url (str): playlist url
        \t - path (str): Directory where the files will be saved
        \t - video_format (str): User-supplied video format (video or audio)
    """
    video = YouTube(url,on_progress)
    private = is_video_private(video)
    if not video.age_restricted and not private:
        if video_format == "video":
            stream = video.streams.get_highest_resolution()
            stream.download(path)
        elif video_format == "audio":
            stream = video.streams.get_audio_only()
            stream.download(path)
        print("\n")
