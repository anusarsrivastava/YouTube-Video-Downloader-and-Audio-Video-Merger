#List of all the libraries are using
import pytube  
from pytube import Channel
from pytube import Playlist
from pytube import YouTube
import csv
import datetime
import os

#File List
file_list = ['_yt_bot_playlist.py', '_yt_bot_videos_downloader.py']#, '_yt_audio_list_gen.py', '_audio_video_merger.py']

#Function for executing the URLs
def _auto_run_url():
    for URL in file_list:
        #Execute File
        exec(open(URL).read())
        print("Updating the script")

# Display message and take input to start
print("Welcome in YT Video Analysis")
print("Input 0 to fresh start or Input 1 to continue")
_user_input = input()

#Check how to user want to start
if _user_input == "0":
    print("Starting")
    exec(open("_yt_flush_video_list.py").read())
    _auto_run_url()
    print("Completed")
elif(_user_input == "1"):
    print("Starting")
    _auto_run_url()
    print("Completed")
else:
    print("Wrong input, try again")