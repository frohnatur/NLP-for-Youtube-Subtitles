from Datenbeschaffung import get_video_ids
from Datenbeschaffung import get_video_subtitles

hob_playlist_id = 'PLrC7fxMTTSU0ufwlgt5wedoN9yHU7TQJT'
pietsmiet_playlist_id = 'PL5JK9SjdCJp_PJcK5ZYkhxJ7Bl8aSHKoD'
maxim_playlist_id = 'PLZF0NVc8Z9nrYso7SRugOHTO6eW12idWp'

if __name__ == '__main__':
    hob_ids = get_video_ids(hob_playlist_id)
    #pietsmiet_ids = get_video_ids(pietsmiet_playlist_id)
    #maxim_ids = get_video_ids(maxim_playlist_id)
    #get_video_subtitles(hob_ids, 'HandOfBloodSubtitles')
    #get_video_subtitles(pietsmiet_ids, 'PietSmietSubtitles')
    #get_video_subtitles(maxim_ids, 'MaximSubtitles')
