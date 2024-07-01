import pytube  
from pytube import YouTube
from time import sleep

# Function for Download YT Audio 
def _yt_audio_download(yt, op_path):

    # Desired bitrate
    desired_bitrates = ['webm','mp4']
    bitrates_dict = {
    "webm": ["137", "248", "251", "250", "249"],
    "mp4": ["140"]
    }

    # Get the highest quality desired audio stream
    for desired_bitrate in desired_bitrates:
        # Get the audio stream
        audio_streams = yt.streams.filter(only_audio=True, file_extension=desired_bitrate)

        # Check the desired audio stream is avilable or not
        if not audio_streams:
            continue
            #print(f"No streams available in {desired_bitrate}.")
        else:
            for __itag in bitrates_dict[desired_bitrate]:
                # Get the desired itag
                audio_stream = audio_streams.get_by_itag(__itag)

                # Check the desired itag is avilable or not
                if not audio_stream:
                    continue
                    #print(f"No streams available in {desired_bitrate}.")
                else:
                    # Download the audio file
                    _new_op_path = op_path  + '/flush'
                    audio_stream.download(output_path=_new_op_path)
                    print(f"Audio Downloaded [itag: {__itag} and file_formate: {desired_bitrate}]")
                    break
            break

# Function for Download YT Videos
def _yt_video_download(yt, op_path):

    # Desired resolution
    desired_resolutions = ['4320p','2160p','1440p','1080p','720p','480p','360p']

    for desired_resolution in desired_resolutions:
        # Filter streams by the desired resolution and file extension
        streams = yt.streams.filter(res=desired_resolution, file_extension='mp4')

        # Check if any streams are available in the desired resolution
        if not streams:
            continue
            #print(f"No streams available in {desired_resolution}.")
        else:
            # Select folder to dump file
            if desired_resolution == '360p':
                _new_op_path = op_path + '/360p'
            else:
                _new_op_path = op_path + '/flush'
            
            # Select the first available stream in the desired resolution
            stream = streams.first()

            # Download the selected stream
            stream.download(output_path=_new_op_path)

            print(f"Video Downloaded [{desired_resolution} resolution].")
            break
    return desired_resolution

#Start from here

# URL of the YouTube video Text File
with open('_yt_required_list/_yt_video_list.txt', mode ='r+')as file: #for opening file
    _yt_video_urls = file.read() #for read
    _yt_video_urls = _yt_video_urls.split('\n')

# Remove empty or blank lines
_yt_video_urls = [_yt_video_url.strip() for _yt_video_url in _yt_video_urls if _yt_video_url.strip()]

print('--------------------------------------------------------')

for video_url in _yt_video_urls:
    yt = pytube.YouTube(video_url)
    op_path = '_yt_downloaded_videos/'
    print(f"{yt.title} : ({video_url})")
    desired_resolution = _yt_video_download(yt, op_path)
    if desired_resolution != '360p':
        _yt_audio_download(yt, op_path)
    sleep(5)
    print('--------------------------------------------------------')