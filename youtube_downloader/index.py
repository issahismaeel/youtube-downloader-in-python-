from pytube import YouTube

# Function to download a YouTube video
def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading {yt.title}...")
        stream.download(output_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

# URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=DJ6tXTsjX_A&t=122s&ab_channel=Intellipaat'
# Path where you want to save the video
output_path = 'C:/Users/Isma\'eel/Downloads'

download_video(video_url, output_path)

