# YouTube-MP3-Downloader
A simple YouTube to MP3 downloader in Python

## How to install ?
You need Python 3 on your computer\
Then install these packages with pip
```
pytube~=12.1.0
pydub~=0.25.1
```

## How to use ?
1. Open the Python script (main.py) with Python
2. Paste the YouTube video's url you want to download as MP3 (e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ) and press enter
3. The video will be downloaded as `_music.mp3` at the Python script location

## What is the audio file bitrate ?
Often 128kbps\
The script chooses the bitrate in this priority order:\
`192kbps` -else-> `128kbps` -else-> The other highest bitrate
