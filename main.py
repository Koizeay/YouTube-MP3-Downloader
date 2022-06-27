from pytube import YouTube
from pydub import AudioSegment
import os

try:
    bitrates = []
    bitrate = None

    yt_url = input("YouTube URL : ")

    try:
        yt = YouTube(yt_url)

        for vid in yt.streams.filter(only_audio=True):
            bitrates.append(vid.abr.replace("kbps", ""))

        if "192" in bitrates:
            bitrate = "192"
        elif "128" in bitrates:
            bitrate = "128"
        else:
            bitrate = max(bitrates)

        video = yt.streams.filter(only_audio=True, bitrate=bitrate + "kbps").first()
        yt_title = yt.title

        print("Downloading \"" + yt_title + "\" in " + bitrate + " kbps")
        out_file = video.download(output_path=".", filename="_music.tmp", skip_existing=False)

        try:
            os.remove("./_music.mp3")
        except:
            pass

        AudioSegment.from_file("./_music.tmp").export("./_music.mp3", format="mp3")
        try:
            os.remove("./_music.tmp")
        except:
            pass

        print("Download complete")
    except:
        print("Error ! Please check you input.")
except KeyboardInterrupt:
    exit()
