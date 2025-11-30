from yt_dlp import YoutubeDL
from constant import ydl_opts
import yt_dlp
import os
import re

CYAN = "\033[94m"
RED = "\033[91m"
RESET_COLOR = "\033[0m"


class TubeToMP3:
    def __init__(self, input_file):
        self.input_file = input_file

    def get_urls(self):
        url_pattern = r'https?://[^\s"]+'
        with open(self.input_file, "r") as file:
            content = file.read()
        urls = re.findall(url_pattern, content)
        return urls


def update_yt_dlp():
    try:
        yt_dlp.update.update_self(quiet=True)
        print(f"{CYAN}yt-dlp updated to the latest version.{RESET_COLOR}")
    except Exception as e:
        print(f"{RED}Failed to update yt-dlp: {e}{RESET_COLOR}")


def download_youtube_video(url):
    try:
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)
        options = ydl_opts(download_dir)
        with YoutubeDL(options) as ydl:
            ydl.download([url])
            print("✅ Download completed successfully!")
            return True

    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False


if __name__ == "__main__":
    input_file = "target.txt"
    tube = TubeToMP3(input_file)
    urls = tube.get_urls()

    if not urls:
        print(f"{RED}No valid URLs found in {input_file}.{RESET_COLOR}")
        exit(1)

    update_yt_dlp()

    for url in urls:
        download_youtube_video(url)
