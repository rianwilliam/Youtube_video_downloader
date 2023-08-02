"""Perform URL validations."""
import re

def is_video_url(url: str) -> bool:
    """
    Checks if the user-provided video URL is valid.
    * Args:
        \t - url (str): youtube video url.
    * Returns:
        bool: True if the given url is valid and false otherwise.
    """
    video_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([a-zA-Z0-9_-]{11})"
    if not re.compile(video_pattern).match(url):
        return False
    return True

def is_playlist_url(url: str) -> bool:
    """
    Checks if the user-provided playlist URL is valid.
    * Args:
        \t - url (str): youtube playlist url.
    * Returns:
        bool: True if the given url is valid and false otherwise.
    """
    playlist_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/playlist\?list=([a-zA-Z0-9_-]+)"
    if not re.compile(playlist_pattern).match(url):
        return False
    return True
