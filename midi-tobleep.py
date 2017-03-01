#!/usr/bin/env python
import argparse, csv

parser = argparse.ArgumentParser(description='Convert midi files to beep tunes')
parser.add_argument('-f', type=str, help='a filepath to the midi you want played')
parser.add_argument('-l', type=str, help='the length of the midi you would like translated to beep')
# Need an arguement to supress beep
# Need an arguement to print to console
args = parser.parse_args()
bpm = 192
spd_mod = 0.9
oct_mod = 0.7


def getTempo(temp):
    return float(60000000. / float(temp))


def getDuration(end, start):
    return float(end - start) / float(bpm * spd_mod) / 8.0


def getFreq(row):
    return str(midiNumToFreq(int(row[4].strip())))


def midiNumToFreq(midiNumber):
    return 440 * pow(2, (int(midiNumber) - 69) / float(12)) * oct_mod


def beepString(note, duration, lastnote):
    freq = str(midiNumToFreq(note))
    nlen = str(duration * 1000)
    if lastnote != 0:
        return str(' -n ' + " -f " + freq + " -l " + nlen )
    else:
        return str(" -f " + freq + " -l " + nlen )



def buildBeep():
    with open('beep.sh', 'w') as outfile:
        csvFile = csv.reader(open(args.f, 'rb'))
        lastnote = 0
        outfile.write('beep ')

        nodestack = [];
        # Track, Time, Note_on_c, Channel, Note, Velocity
        for row in csvFile:
            if 'Tempo' in row[2]:
                # handle Tempo messages
                bpm = getTempo(row[3]);
                print('BPM: ', bpm)
            elif 'Note_on_c' in row[2]:
                # starts a note and add to stack
                nodestack.append([row[4], row[1]])

            elif 'Note_off_c' in row[2]:
                # Pop node from stack if it was used before
                for idx, note in enumerate(nodestack):
                    if note[0] == row[4]:
                        nodestack.pop(idx)
                        duration = getDuration(int(row[1]), int(note[1]))
                        outfile.write(beepString(note[0], duration, lastnote))
                        lastnote += 1
    return


if not args.f:
    parser.print_help()
else:
    buildBeep()
