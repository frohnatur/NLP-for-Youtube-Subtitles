from Datenbeschaffung import get_video_ids
from Datenbeschaffung import get_video_subtitles
from Datenbeschaffung import get_video_statistics
import pandas as pd

hob_playlist_id = 'PLrC7fxMTTSU0ufwlgt5wedoN9yHU7TQJT'
pietsmiet_playlist_id = 'PL5JK9SjdCJp_PJcK5ZYkhxJ7Bl8aSHKoD'
maxim_playlist_id = 'PLZF0NVc8Z9nrYso7SRugOHTO6eW12idWp'
grummel_fritz_playlist_id = 'PLJzHt0Z4xWmN3Wt8eFdjDWAAzX29RAJCC'
beam_playlist_id = 'PL5KHd4q0vXyxrjC9CMOGZngzvrrI0HWH_'

if __name__ == '__main__':

    hob_ids = get_video_ids(hob_playlist_id)
    #pietsmiet_ids = get_video_ids(pietsmiet_playlist_id)
    #maxim_ids = get_video_ids(maxim_playlist_id)
    #grummel_fritz_ids = get_video_ids(grummel_fritz_playlist_id)
    #beam_ids = get_video_ids(beam_playlist_id)

    #get_video_subtitles(hob_ids, 'HandOfBloodSubtitles')
    #get_video_statistics(hob_ids).to_csv("VideoStatisiken/HandOfBlood")

    #get_video_subtitles(pietsmiet_ids, 'PietSmietSubtitles')
    #get_video_statistics(pietsmiet_ids).to_csv("VideoStatisiken/PietSmiet")

    #get_video_subtitles(maxim_ids, 'MaximSubtitles')
    #get_video_statistics(maxim_ids).to_csv("VideoStatisiken/Maxim")

    #get_video_subtitles(grummel_fritz_ids, 'GrummelFritzSubtitles')
    #get_video_statistics(grummel_fritz_ids).to_csv("VideoStatisiken/GrummelFritz")

    #get_video_subtitles(beam_ids, 'BeamSubtitles')
    #get_video_statistics(beam_ids).to_csv("VideoStatisiken/Beam")
