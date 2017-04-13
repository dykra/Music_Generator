from random import randint
from copy import copy
from randomtracks import give_3_random_tracks


def give_heart_beat_music():
    background = HeartbeatStyle()
    tracks_list = background.background_heart_track()
    tracks_list.extend(background.generate_tracks_whole_song(10))
    tracks_list.extend(background.generate_tracks_whole_song(50))
    return tracks_list


class HeartbeatStyle:

    def __init__(self):
        self.background_increase = 20
        self.background_tracks = [[0, 4,  175, 10],
                                  [0, 90, 200, 4],
                                  [0, 9, 175, 4],
                                  [0, 29, 175, 4],
                                  [0, 115, 175, 8],
                                  [0, 80, 200, 4]]

    def choose_main_motive(self):
        i = randint(0, len(self.background_tracks) - 1)
        return self.background_tracks[i]

    def generate_tracks_whole_song(self, start):
        result = give_3_random_tracks(start, 0, 0)
        step = randint(self.background_increase, self.background_increase * 2)
        amount = randint(10, 15)
        j = result[0][0]
        k = result[1][0]
        m = result[2][0]
        tmp_j = copy(result[0][1:])
        tmp_k = copy(result[1][1:])
        tmp_m = copy(result[2][1:])
        for i in range(1, amount):
            a = [i * step + j]
            a.extend(tmp_j)
            b = [i * step + k]
            b.extend(tmp_k)
            c = [i * step + m]
            c.extend(tmp_m)
            result.extend([a, b, c])
        return result

    def background_heart_track(self):
        result = [self.choose_main_motive()]
        j = result[0][1]
        k = result[0][2]
        m = result[0][3]
        for i in range(0, 30):
            tmp = [i * self.background_increase, j, k, m]
            result.append(tmp)
        return result
