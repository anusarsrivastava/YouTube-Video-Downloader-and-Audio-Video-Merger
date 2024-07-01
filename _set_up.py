import os, csv

#List of Requirements
file_list = ['pip install pytube', 'pip install moviepy']

#Install the requirements
for file in file_list:
    #os.system('cmd /k "'+file+'"')
    os.system('"start /wait cmd /c '+file+'"')