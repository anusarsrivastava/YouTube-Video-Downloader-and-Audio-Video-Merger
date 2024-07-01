from moviepy.editor import VideoFileClip, AudioFileClip

_base_path = '_yt_downloaded_videos/flush/'
_output_path = '_yt_downloaded_videos/_audio_video_merge/'

# URL of the YouTube video Text File
with open('_yt_required_list/_yt_audio_list.txt', encoding='utf-8', mode ='r+')as file: #for opening file
    _yt_audio_urls = file.read() #for read
    _yt_audio_urls = _yt_audio_urls.split('\n')

# Remove empty or blank lines
_yt_audio_urls = [_yt_audio_url.strip() for _yt_audio_url in _yt_audio_urls if _yt_audio_url.strip()]

for _yt_audio in _yt_audio_urls:
    __base_path = _base_path + _yt_audio
    ___base_path = __base_path.split('.')
    _yt_audio.split('.')[0]

    # Load the video file
    ___yt_video = ___base_path[0]+".mp4"
    video = VideoFileClip(___yt_video)

    # Load the audio file
    audio = AudioFileClip(__base_path)

    # Set the audio of the video
    video = video.set_audio(audio)

    # Save the final video
    __output_base_path = _output_path + _yt_audio
    video.write_videofile(__output_base_path.split('.')[0]+'.mp4', codec="libx264", audio_codec="aac")