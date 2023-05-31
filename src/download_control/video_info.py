"""Here the download information is entered."""
import os
from .video import download_video
from .playlist import download_playlist
from src.screens.user_screens import options, colors
from src.validations.url_validation import is_playlist_url, is_video_url

def get_url() -> str:
    """Get the video or playlist url"""
    url = input("Insira a url: ")
    while not is_video_url(url) and not is_playlist_url(url):
        url = input("Insira uma url válida: ")
    return url

def get_path() -> str:
    """Gets the directory where the file will be saved"""
    path = ""
    while not os.path.exists(path):
        path = input(
            "Insira o diretório de download (deixar em branco para diretório atual): "
        )
        if not path:
            path = os.getcwd()
    return path

def get_video_format() -> str:
    """Gets what format the file will be downloaded in"""
    video_format = ""
    while not video_format:
        video_format = options(
            message = "Qual o formato do download",
            choices = ["video", "audio"]
        )
    return video_format

def download(url: str, path: str, video_format: str) -> None:
    """
    Identifies the url type and downloads the video

    * Args
        \t - url (str): Video url
        \t - path (str): Directory where the files will be saved
        \t - video_format (str): User-supplied video format (video or audio)
    """
    print("Baixando...(não feche o programa)")
    colors("green")
    if is_video_url(url):
        download_video(url, path, video_format)
    elif is_playlist_url(url):
        download_playlist(url, path, video_format)
    colors("reset")
    print("Download Finalizado!!")
    input("Pressione enter para sair")

def get_video_info() -> None:
    """
    This is where the video download information is taken from the user.
    * url;
    * path;
    * file type (video or audio).
    """
    url = get_url()
    path = get_path()
    video_format = get_video_format()

    download(url, path, video_format)


