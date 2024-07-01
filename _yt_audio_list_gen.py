import os

def list_files_in_directory(directory, extensions):
    # Get list of all files and directories
    all_items = os.listdir(directory)
    
    # Filter out directories and files without the desired extensions
    files = [item for item in all_items if os.path.isfile(os.path.join(directory, item)) and item.endswith(extensions)]
    
    return files

directory_path = '_yt_downloaded_videos/flush/'
extensions = ('.webm', '.m4a')
_files = list_files_in_directory(directory_path, extensions)


#Save and Udpate the Video List
with open('_yt_required_list/_yt_audio_list.txt', 'w', newline='', encoding='utf-8') as f:
    for _file in _files:
        f.write(_file+'\n')