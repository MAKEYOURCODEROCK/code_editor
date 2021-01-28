from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# creating YouTube object
yt = YouTube("https://www.youtube.com/watch?v=1csFTDXXULY") 

# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first() 

# download into working directory
stream.download()