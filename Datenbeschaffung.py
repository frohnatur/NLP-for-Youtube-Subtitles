from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import googleapiclient.discovery


def get_video_ids(playlist_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="Developer Key")

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    playlist_items_video_ids = []
    for item in playlist_items:
        playlist_items_video_ids.append(item["snippet"]["resourceId"]["videoId"])

    print(playlist_items_video_ids)
    print(len(playlist_items_video_ids))
    return playlist_items_video_ids


def get_video_subtitles(video_ids, directory):
    formatter = TextFormatter()
    count = 0
    for item in video_ids:
        count += 1
        video_transcript = YouTubeTranscriptApi.get_transcript(item, languages=['de'])
        formatted = formatter.format_transcript(video_transcript)

        with open(directory + '/video' + str(count) + '.txt', 'w', encoding='utf-8') as file:
            file.write(formatted)

# video_transcript1 = YouTubeTranscriptApi.get_transcript('xvqsFTUsOmc', languages=['en'])
# video_transcript2 = YouTubeTranscriptApi.get_transcript('44atyNUpAmY', languages=['de'])
# video_transcript3 = YouTubeTranscriptApi.get_transcript('Ljcz4tA101U', languages=['de'])

# formatter = TextFormatter()
# formatted1 = formatter.format_transcript(video_transcript2)
# formatted2 = formatter.format_transcript(video_transcript1)
# formatted3 = formatter.format_transcript(video_transcript3)

# with open('test1.txt', 'w', encoding='utf-8') as file1:
# file1.write(formatted1)

# with open('test2.txt', 'w', encoding='utf-8') as file2:
# file2.write(formatted2)

# with open('test3.txt', 'w', encoding='utf-8') as file3:
# file3.write(formatted3)


# print(video_transcript1)
# print(video_transcript2)
