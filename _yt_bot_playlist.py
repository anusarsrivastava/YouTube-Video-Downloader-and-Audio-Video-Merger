from pytube import Playlist

# URL of the YouTube Playlist Text File
with open('_yt_required_list/_yt_playlist.txt', mode ='r+')as file: #for opening file
    _yt_playlists = file.read() #for read
    _yt_playlists = _yt_playlists.split('\n')

#Open File and Remove White space from YT Video List
with open('_yt_required_list/_yt_video_list.txt', mode ='r+')as file: #for opening file
    _yt_video_lists = file.read() #for read
    _yt_video_lists = _yt_video_lists.split('\n')

_length_video_lists = len(_yt_video_lists)-1
if _yt_video_lists[_length_video_lists] == "":
    _yt_video_lists.pop()

#Create Blank List to save Video Links
_yt_videos_url = []

#Function to Save Video Links
def _yt_playlist_BOT(playlist,_yt_videos_url):
    p = Playlist(playlist)
    for url in p.video_urls:
        _yt_videos_url.append(url)

#Fetch Video Links from the YT Playlist
for playlist in _yt_playlists:
    _yt_playlist_BOT(playlist,_yt_videos_url)

#Save and Udpate the Video List
with open('_yt_required_list/_yt_video_list.txt', 'a', newline='', encoding='utf-8') as f:
    for _yt_video_url in _yt_videos_url:
        f.write(_yt_video_url+'\n')