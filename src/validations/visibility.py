"""File responsible for checking video visibility"""
from pytube import YouTube

def is_video_private(video: YouTube):
    """
    Here it is checked if the video is public

    * Args
        \t - video (Youtube) An object from the pytube youtube class
    """
    try:
        video.check_availability()
    except:
        return True
    return False
    