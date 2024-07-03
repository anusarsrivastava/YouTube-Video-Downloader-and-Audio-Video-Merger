from pytube import Channel
import urllib.error

# YouTube Channel List
with open('_yt_required_list/_yt_channel_list.txt', mode ='r+')as file: #for opening file
    _yt_channel_lists = file.read() #for read
    _yt_channel_lists = _yt_channel_lists.split('\n')

# Remove empty or blank lines
_yt_channel_lists = [_yt_channel_list.strip() for _yt_channel_list in _yt_channel_lists if _yt_channel_list.strip()]

# Create Blank List to save Video Links
_yt_videos_url = []

#Function to Save Video Links
def _yt_channel_BOT(channel,_yt_videos_url):
    for url in channel.video_urls:
        print(url)
        _yt_videos_url.append(url)

# Function to get all video URLs from a channel
def get_channel_video_urls(channel_url):
    try:
        channel = Channel(channel_url)
        print(f'Extracting videos from: {channel.channel_name}')
        _yt_channel_BOT(channel,_yt_videos_url)
    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Start Extracting video urls
for _yt_channel_url in _yt_channel_lists:
    get_channel_video_urls(_yt_channel_url)

# Save the list to a file
with open('_yt_required_list/_yt_video_list.txt', 'a') as f:
    for _url in _yt_videos_url:
        f.write(_url + '\n')