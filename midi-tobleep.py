#!/usr/bin/env python
import argparse, csv

parser = argparse.ArgumentParser(description='Convert midi files to beep tunes')
parser.add_argument('-f', type=str, help='a filepath to the midi you want played')
parser.add_argument('-l', type=str, help='the length of the midi you would like translated to beep')
# Need an arguement to supress beep
# Need an arguement to print to console
args = parser.parse_args()
bpm = 120
spd_mod = 0.65
oct_mod = 1

channel = '0'


def getTempo(temp):
    return float(60000000. / float(temp))


def getDuration(end, start):
    return float(end - start) / float(bpm) / 8.0 * spd_mod


def getFreq(row):
    return str(midiNumToFreq(int(row[4].strip())))


def midiNumToFreq(midiNumber):
    return 440 * pow(2, (int(midiNumber) - 69) / float(12)) * oct_mod


def beepString(note, duration, lastnote, delay=0):
    freq = str(midiNumToFreq(note))
    nlen = str(duration * 1000)
    if lastnote != 0:
        return str(' -D ' + str(delay * 1000) + ' -n ' + " -f " + freq + " -l " + nlen )
    else:
        return str(" -f " + freq + " -l " + nlen)



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
            elif 'Note_on_c' in row[2] and channel in row[3]:
                # starts a note and add to stack
                tmp = [row[4], row[1]]
                # bei doppelten Noten, nimm die hoehere
                if tmp in nodestack:
                    old = nodestack.pop()
                    if tmp[0] > old[0]:
                        nodestack.append(old)
                else:
                    nodestack.append(tmp)
            elif 'Note_off_c' in row[2] and channel in row[3]:
                # Pop node from stack if it was used before
                for idx, note in enumerate(nodestack):
                    if note[0] == row[4]:
                        nodestack.pop(idx)
                        duration = getDuration(int(row[1]), int(note[1]))
                        if lastnote < note[1]:
                            delay = getDuration(int(note[1]), int(lastnote))
                        else:
                            delay = 0.0
                        if delay < 0:
                            print "WRONG", delay, note[1]
                            delay = 0
                        if delay > 5:
                           print "WRONG", delay, note[1]
                           delay = 2
                        outfile.write(beepString(note[0], duration, lastnote, delay))
                        # the last played notes time
                        lastnote = row[1]
    return


if not args.f:
    parser.print_help()
else:
    buildBeep()
