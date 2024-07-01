import pytube
from pytube import YouTube
import csv
import datetime

# YT Video List
f = open("_yt_required_list/_yt_video_list.txt", 'r+') #for opening file
_yt_video_urls = f.read() #for read
_yt_video_urls = _yt_video_urls.split('\n')
f.close() #close

# List of YT Video ID
f = open("_yt_reports/_yt_video_id_list.txt", 'r+') #for opening file
_yt_video_id_lists = f.read() #for read
_yt_video_id_lists = _yt_video_id_lists.split('\n')
f.close() #close

# Function for fetching YT Video Details
def _yt_video_details(_yt_video_url):
    video_url = YouTube(_yt_video_url)
    return video_url.video_id,_yt_video_url,video_url.title,video_url.description,video_url.length,video_url.thumbnail_url,video_url.views,video_url.rating,video_url.age_restricted,video_url.author,video_url.caption_tracks,video_url.captions,video_url.channel_id,video_url.channel_url,video_url.check_availability,video_url.metadata,video_url.publish_date,video_url.keywords,datetime.datetime.now()#,video_url.fmt_streams

# Function to update the Video ID List
def _yt_video_id_list_update(_video_id):
    with open('_yt_reports\_yt_video_id_list.txt', 'a', newline='', encoding='utf-8') as f:
        f.write(_video_id+"\n")

# Function for updating the Video id list itself
def _yt_reports(_yt_video_details,_yt_video_id_lists):
    _yt_video_is_exits = False  #Assign variable to check Video Id is exits or not

    for _yt_video_id_list in _yt_video_id_lists:
        if _yt_video_id_list == _yt_video_details[0]:
            _yt_video_is_exits = True

    if _yt_video_is_exits == False:
        _yt_video_id_list_update(_yt_video_details[0])

counter = 0

#Set File name for every video file
_time = str(datetime.datetime.now()).split(" ")[1].replace(".","_").replace(":","")
_date = str(datetime.datetime.now()).split(" ")[0].replace("-","_")
_file_name = '_yt_reports_main/_yt_videos_details_'+_date+"_"+_time

#Save and Udpate the Video Details
with open( _file_name + '.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Video Id','URL','Title','Description','Length','Thumbnail Url','Views','Rating','Age Restricted','Author','Caption Tracks','Captions','Channel Id','Channel URL','Check Availability','Metadata','Publish Date','keywords','Time Stamp'])
    for _yt_video_url in _yt_video_urls:
        _yt_video_detail = _yt_video_details(_yt_video_url)
        writer.writerow(_yt_video_detail)
        _yt_reports(_yt_video_detail,_yt_video_id_lists)
        print(counter)
        counter += 1