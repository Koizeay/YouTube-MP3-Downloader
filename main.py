import warnings

warnings.filterwarnings("ignore")

import sys
from sys import exit
from pytube import YouTube
from pydub import AudioSegment
import os

try:

    def getFilesPath():
        try:
            basePath = sys._MEIPASS
        except Exception:
            basePath = os.path.abspath(".")

        return basePath


    bitrates = []
    bitrate = None

    youtubeUrl = input("YouTube URL : ")

    try:
        yt = YouTube(youtubeUrl)

        for vid in yt.streams.filter(only_audio=True):
            bitrates.append(vid.abr.replace("kbps", ""))

        if "192" in bitrates:
            bitrate = "192"
        elif "128" in bitrates:
            bitrate = "128"
        else:
            bitrate = max(bitrates)

        video = yt.streams.filter(only_audio=True, bitrate=bitrate + "kbps").first()
        youtubeTitle = yt.title

        print("Downloading \"" + youtubeTitle + "\" in " + bitrate + " kbps")
        outFile = video.download(output_path=".", filename="_music.tmp", skip_existing=False)

        try:
            os.remove("./_music.mp3")
        except:
            pass

        defaultWorkingDir = os.getcwd()
        os.chdir(getFilesPath())

        AudioSegment.from_file(defaultWorkingDir + "/_music.tmp").export(defaultWorkingDir + "/_music.mp3",
                                                                         format="mp3")

        os.chdir(defaultWorkingDir)

        try:
            os.remove("./_music.tmp")
        except:
            pass

        print("Download complete")
        input("Press Enter to exit...")
    except:
        print("Error, Please check you input and your internet connection.")
        input("Press Enter to exit...")
except KeyboardInterrupt:
    exit()
