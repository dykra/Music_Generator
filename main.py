import argparse
from miditime.miditime import MIDITime
from heartbeat import give_heart_beat_music
from randomtracks import give_random_music


def parse_args():
    parser = argparse.ArgumentParser(description='Generates some music.')
    parser.add_argument('--destination', type=str, help='Output file destination', default='myMusic.mid')
    parser.add_argument('--heart_beat', type=int, help='Is the main beat of the song is like heart rate.', default=0)
    parser.add_argument('--maths', type=int, help='Maths patterns', default=0)
    return parser.parse_args()


def give_tracks(heart_rate, maths):
    if 0 != heart_rate:
        return [give_heart_beat_music()]
    return [give_random_music(maths)]


def main():
    args = parse_args()
    mymidi = MIDITime(1000, args.destination)

    for track in give_tracks(args.heart_beat, args.maths):
        mymidi.add_track(track)
    mymidi.save_midi()

if __name__ == '__main__':
    main()
