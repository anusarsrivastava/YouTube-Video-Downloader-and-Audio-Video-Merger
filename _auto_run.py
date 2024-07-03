# List of all the libraries are using
import csv, datetime, os

# File List
file_list = ['_yt_bot_videos_downloader.py', '_yt_audio_list_gen.py', '_audio_video_merger.py']

# Function for executing the URLs
def _auto_run_url():
    print("Processing your request")
    for URL in file_list:
        #Execute File
        exec(open(URL).read())
    print("Your Request is Completed successfully")

# Display Welcome message and take input to start
print("Welcome in YouTube Video Downloader and Analyzer")
print("Do You want to Download YouTube Videos using the following options:\n 1. Press 1 to Download YouTube Complete Channel Video\n 2. Press 2 to Download YouTube Complete Playlist Video\n 3. Press 3 to Download YouTube Videos")
_feature_input = input()

# Clear Cache
exec(open("_yt_flush_video_list.py").read())

# Request to add request file and status
print("Add URL's in the respected file as per your request. When you are done Enter 1 ")
_file_status_input = input()

# Check Input Request is Valid
if _file_status_input == "1":
    #Check how to user want to start
    if _feature_input == "1":
    #    exec(open("_yt_bot_channel.py").read())
    #    _auto_run_url()
        print("Currently this feature is done")
    elif _feature_input == "2":
        exec(open("_yt_bot_playlist.py").read())
        _auto_run_url()
    elif _feature_input == "3":
        _auto_run_url()
    else:
        print("Wrong input, try again")
else:
        print("Wrong input, try again")

# Documentation for Pytube
# https://pytube.io/en/latest/user/channel.html
# https://www.geeksforgeeks.org/youtube-video-downloader-using-django/?ref=ml_lbp