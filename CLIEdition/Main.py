import pytube as youtube_py

def Main():
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
