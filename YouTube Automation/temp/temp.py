from pytube import YouTube,Channel,Playlist
from pytube.cli import on_progress


# v = YouTube('https://www.youtube.com/watch?v=1tQvNuZI2qc')
# c = Channel('https://www.youtube.com/c/movietrailers-youtube/videos')
# p = Playlist('https://www.youtube.com/watch?v=VvH1WfiobIk&list=PL1AbY16T0oOErl9mOfIeWpqKCt070jgN0')

# a = "pip install"
# a = a.title()
# print(a)
# curl = v.channel_url
# print(curl)
# ch_name = Channel(v.channel_url).channel_name
# print(ch_name)
# link = 'https://youtu.be/LxEGWzq9njI'

# def dv(link):
# yt = YouTube(link , on_progress_callback=on_progress)
# yt.streams.get_highest_resolution().download()
# videos = yt.streams.all()

# videos[3].download()

# print("download ")
# v.streams.first() .download()  
# ch_name = Channel(YouTube('https://www.youtube.com/watch?v=1tQvNuZI2qc').channel_url).channel_name
# v_url =str(Channel("https://www.youtube.com/c/movietrailers-youtube/videos").video_urls[:1])
# v_id = YouTube(v_url).video_id
# v_len = v.length
# print(v_len)
# print(ch_name)
# print(v_title)
# yt = YouTube(link)
# path = "date/channel_name/video_name"
# v.streams.get_highest_resolution().download()

# print(Channel('https://www.youtube.com/c/movietrailers-youtube/videos').video_urls[:2])


# print(Channel(YouTube('https://www.youtube.com/watch?v=1tQvNuZI2qc').channel_url).channel_name)


#==============YouTube Object type========================
# print("channel id from video url-->",v.channel_id)
# print("channel url from video url-->",v.channel_url)
# print("video description from video url-->",v.description)
# print("fetch video keywords from video url-->",v.keywords)
# print("video length from video url-->",v.length)
# print("video publish_date from video url-->",v.publish_date)
# print("video rating from video url-->",v.rating)
# print("video thumbnail_url from video url-->",v.thumbnail_url)
# print(f"https://img.youtube.com/vi/{v.video_id}/maxresdefault.jpg")
# print("video title from video url-->",v.title)
# print("video vid_info (json) from video url-->",v.vid_info)
# print("video views from video url-->",v.views)


#==============Playlist Object type========================
# print("initial_data (json) from playlist url-->",p.initial_data)
# print("owner fetch no. video in playlist from playlist url-->",p.owner)
# print("owner_id fetch no. video in playlist from playlist url-->",p.owner_id)
# print("owner_url from playlist url-->",p.owner_url)
# print("playlist_id from playlist url-->",p.playlist_id)
# print("playlist_url playlist url-->",p.playlist_url)
# print("title of playlist from playlist url-->",p.title)
# print("return video_urls(list) of playlist from playlist url-->",p.video_urls)
# print("retutn videos id of playlist from playlist url",p.videos)
# print("playlist views from playlist url-->",p.views)


#==============Channel Object type========================
# print("channel_id from channel url-->",c.channel_id)
# print("channel_name from channel url-->",c.channel_name)


#-----errorsssssssss====================
# print("Extract the initial data from the channel page html.-->",c.initial_data)
# print("Extract the date that the channel was last updated. -->",c.last_updated)
# print("Extract the number of videos in the channel.-->",c.length)
# print("Get the base channel url.-->",c.playlist_url)
# print("Extract playlist title-->",c.title)