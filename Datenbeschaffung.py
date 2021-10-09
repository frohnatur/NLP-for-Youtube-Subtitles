from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import googleapiclient.discovery
import pandas as pd


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
        try:
            video_transcript = YouTubeTranscriptApi.get_transcript(item, languages=['de'])
            formatted = formatter.format_transcript(video_transcript)

            with open(directory + '/video' + str(count) + '.txt', 'w', encoding='utf-8') as file:
                file.write(formatted)
        except:
               with open(directory + '/video' + str(count) + '.txt', 'w', encoding='utf-8') as file:
                  file.write("NoSubtitles")
        count += 1

def get_video_statistics(video_ids):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="Developer Key")

    playlist_stats = []

    for id in video_ids:

        video_stats = {}

        request = youtube.videos().list(
            part="statistics, snippet",
            id=id
        )

        response = request.execute()
        response_statistics = response['items'][0]['statistics']
        response_snippet = response['items'][0]['snippet']

        video_stats["title"] = response_snippet["title"]

        stats_list = ['favoriteCount', 'viewCount', 'likeCount',
                          'dislikeCount', 'commentCount']

        for stat in stats_list:
            try:
                video_stats[stat] = response_statistics[stat]
            except:
                video_stats[stat] = 'xxNoneFoundxx'

        playlist_stats.append(video_stats)

    playlist_stats = pd.DataFrame(playlist_stats)
    return playlist_stats
