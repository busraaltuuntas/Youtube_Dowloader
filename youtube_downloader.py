from pytube import YouTube

SAVE_PATH= "C:\indirlen_sarki"


link = input('Enter Youtube Video URL:')

try:
    yt= YouTube(link)
except:
    print("Connection Error")

mp4files = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)


