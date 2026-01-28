# Exemplo básico de uso
import os
import sys
import win32com.shell.shell as shell
from win32com.shell import shellcon
from pytubefix import YouTube


def get_videos_folder():
    # Access the Videos folder using the Windows API
    videos_folder = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Videos, 0, None)
    return videos_folder

def main():

    # If you want to change the directory, update the directory variable
    directory = get_videos_folder() + "\\yt-downloader"

    if not os.path.exists(directory):
        os.makedirs(directory)

    size = len(sys.argv)
    enable_mp3 = False

    # If you want to insert the url in the code, insert it in the video_url variable
    video_url = "your url"

    match size:

        case 1:
            pass

        case 2:

            if sys.argv[1] == "mp3":
                enable_mp3 = True
            else:
                return print("Invalid Argument | Try mp3 or manual <url> mp3")

        case 3:

            if sys.argv[1] == "manual":
                video_url = sys.argv[2]

        case 4:

            if sys.argv[1] == "manual" and sys.argv[3] == "mp3":

                video_url = sys.argv[2]
                enable_mp3 = True

            else:
                return print("Invalid Arguments | Try manual <url> mp3")

        case _:
            return print("Many Arguments")

    try:
        yt = YouTube(video_url)
    except Exception as e:
        print("Invalid URL")
        print("If the url is correct, press 'y' to print the error log")
        if input().lower() == "y":
            print(e)
        else:
            sys.exit()

    if enable_mp3:

        print("Baixando MP3...")
        stream = yt.streams.filter(only_audio=True).first()

    else:
        stream = yt.streams.get_highest_resolution()

    # Download video
    print(f"Downloading: {yt.title}")
    stream.download(directory)
    print("Download completed!")


if __name__ == "__main__":
    main()
