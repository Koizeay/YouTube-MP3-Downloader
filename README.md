# YouTube-MP3-Downloader
A simple YouTube to MP3 downloader in Python
## Which version should I choose ?
The `.exe` version (it's compatible with Windows and Linux, *not tested on macOS*).
## How to install ?
### `.exe` version
Download the .exe file from here https://github.com/Koizeay/YouTube-MP3-Downloader/releases/ \
**Windows :** Double-click on it.\
**Linux (e.g. Ubuntu) :** Make it executable and run it in a terminal (you need to have ffmpeg).
### `.py` version
Download the .py file from here https://github.com/Koizeay/YouTube-MP3-Downloader/releases/ \
You need Python 3 and ffmpeg on your computer\
Then install these packages with pip
```
pytube~=12.1.0
pydub~=0.25.1
```

## How to use ?
1. Open the EXE file or the Python script
2. Paste the YouTube video's url you want to download as MP3 (e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ) and press enter
3. The video will be downloaded as `_music.mp3` at the EXE file or Python script location

## What is the audio file bitrate ?
Often 128kbps\
The script chooses the bitrate in this priority order:\
`192kbps` -else-> `128kbps` -else-> The other highest bitrate
