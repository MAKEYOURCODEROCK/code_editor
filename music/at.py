import youtube_dl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def run():
    video_url = input("URL: ")

    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f'{video_info["title"]}.mp3'
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
            #'preferredquality': '192',
        }]
    }
    with YouTube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


if __name__ == '__main__':
    run()