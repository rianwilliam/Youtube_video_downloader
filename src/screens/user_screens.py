"""Responsible for the terminal interface"""
import sys
import os
from typing import List

def clear_screen() -> None:
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_lines(num_lines: int):
    """
    Clears x number of lines from the terminal
    * Args:
        \t - num_lines (int): Number of lines to be deleted
    """
    for _ in range(num_lines):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')

def options(message: str, choices: List[str] = None) -> str:
    """
    Prints a small menu of options for the user
    * Args:
        \t - message (str): Menu title message
        \t - choices (list[str], optional): List of options present in the menu
    * Returns:
        \t - str: Returns the text of the option chosen by the user
    """
    print(message)
    if choices:
        for index,item in enumerate(choices):
            print(f"[{index+1}] - {item}")

    selected_choice = input("Insira a opção desejada: ")
    if not selected_choice.isdigit():
        clear_lines(2 + len(choices))
        return ""
    elif int(selected_choice) > len(choices) or int(selected_choice) <= 0:
        clear_lines(2 + len(choices))
        return ""
    return choices[int(selected_choice)-1]

def colors(color: str) -> None:
    """
    Changes the text or background color of the terminal
    * Args:
        \t - color (str): Act with dict key to select color
    * Returns:
        \t - If the provided color is present in "colors" it will execute a print containing the value of this color in ASCII
    """
    colors = {
        # ANSI color codes
        "red": "\033[1;31m", # red
        "background_white": "\033[47m", # background white,
        "reset": "\033[0m", # reset,
        "green": "\033[0;32m", # green
    }
    if colors.get(color):
        print(colors.get(color), end="")

def youtube_logo() -> None:
    colors("background_white")
    colors("red")
    print(f"""
█████████████
█████░▀██████
█████░░░▀████
█████░░░▄████
█████░▄██████
█████████████
""")
    colors("reset")
    colors("red")
    print("YOUTUBE VIDEO DOWNLOADER")
    print("")
    colors("reset")
