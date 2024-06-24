import pytube as youtube_py
import ctypes
from time import sleep
def Main():
    kernel32 = ctypes.CDLL("Kernel32")
    converted_titleAnsi = bytes("YTVideoDownloader | Made by RiritoNinigaya", "UTF-8")
    kernel32.SetConsoleTitleA(converted_titleAnsi)
    yt_down = input("Please Write YouTube Video Link: ")

    video_link = youtube_py.YouTube(str(yt_down))

    videol = video_link.streams.filter(file_extension="mp4") 

    res720 = videol.filter(res="720p")

    if(res720):
        print("This Resolution Is Founded... Downloading...")
        res720[0].download()
        print("Download is Completed!!! Thank you for Choosing this Program!!! \nMade by RiritoNinigaya!!!")
        sleep(3)
        exit(676)
    else:
        print("This Resolution Is Not Founded... Pls Try Another Video")
        return

if __name__ == "__main__":
    Main()
