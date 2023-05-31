"""Performs main functions."""
from src.download_control.video_info import get_video_info
from src.screens.user_screens import youtube_logo, clear_screen

def main() -> None:
    """Prints que Youtube logo and Download options."""
    clear_screen()
    youtube_logo()
    get_video_info()
