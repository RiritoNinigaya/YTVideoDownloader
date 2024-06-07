import pytube as youtube_py
import ctypes
def Main():
    kernel32 = ctypes.CDLL("Kernel32")
    converted_titleAnsi = bytes("YTVideoDownloader | Made by RiritoNinigaya", "UTF-8")
    kernel32.SetConsoleTitleA(converted_titleAnsi)
    yt_down = input("Please Write YouTube Link: ")

    video_link = youtube_py.YouTube(str(yt_down))

    videol = video_link.streams.filter(file_extension="mp4") 

    res720 = videol.filter(res="720p")

    if(res720):
        print("This Resolution Is Founded... Downloading...")
        res720[0].download()
    else:
        print("This Resolution Is Not Founded... Pls Try Another Video")
        return

if __name__ == "__main__":
    Main()
