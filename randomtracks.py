from copy import copy
from random import randint


def give_3_random_tracks(start, safe, maths):
    result = []
    if maths == 0:
        randoms_list = [randint(24, 107), randint(24, 107), randint(1, 127)]
    else:
        randoms_list = rands_from_one_octave()
    randoms_list = sorted(randoms_list)
    list_tmp = [randoms_list[1] - randoms_list[0], randoms_list[2] - randoms_list[1]]
    if 0 == list_tmp[0] and list_tmp[1] == 0:
        if safe != -1:
            return give_3_random_tracks(start, -1, maths)
        else:
            result.append([start, randoms_list[0], 200, 4])
            result.append([start + 4, randoms_list[1] + 12, 200, 4])
            result.append([start + 8, randoms_list[2] + 24, 100, 4])
    else:
        if list_tmp[1] == 0:
            result.append([start, randoms_list[0], 200, 4])
            result.append([start + 8, randoms_list[1], 200, 4])
            result.append([start + 12, randoms_list[2] + 12, 100, 4])
        else:
            if list_tmp[0] == 0:
                result.append([start, randoms_list[0], 200, 4])
                result.append([start + 8, randoms_list[1] + 24, 200, 4])
                result.append([start + 12, randoms_list[2], 100, 4])
            else:
                result.append([start, randoms_list[0], 200, 4])
                result.append([start + 4, randoms_list[1], 200, 4])
                result.append([start + 8, randoms_list[2], 100, 4])
    return result


def rands_from_one_octave():
    octave = randint(1, 11)
    result = [randint(0, 11) + (octave * 12) % 127, randint(0, 11) + (12 * octave) % 127, randint(0, 11) + (12 * octave) % 127]
    return result


class RandomTracks:

    def __init__(self):
        self.different_tracks = randint(5, 15)

    def tracks_all_song(self, maths):
        result = []
        for x in range(1, self.different_tracks):
            partial_result = give_3_random_tracks(0, 0, maths)
            j = partial_result[0][0]
            k = partial_result[1][0]
            m = partial_result[2][0]
            amount = randint(1, 3)
            step = randint(4, 50)
            tmp_j = copy(partial_result[0][1:])
            tmp_k = copy(partial_result[1][1:])
            tmp_m = copy(partial_result[2][1:])
            for i in range(1, amount):
                a = [i * step + j]
                a.extend(tmp_j)
                b = [i * step + k]
                b.extend(tmp_k)
                c = [i * step + m]
                c.extend(tmp_m)
                result.extend([a, b, c])
                result.extend(partial_result)
        return result


def give_random_music(maths):
    random_tracks = RandomTracks()
    return random_tracks.tracks_all_song(maths)
