#!/usr/bin/env python3

import subprocess

RADIO_STREAMS = [
    {
        'id': 'bbc3',
        'name': 'BBC Radio 3 (Classical)',
        'uri': 'http://www.radiofeeds.co.uk/bbcradio3.pls',
        'mplayer flags': ['-playlist']
    },
    {
        'id': 'cprc',
        'name': 'Colorado Public Radio Classical',
        'uri': 'http://livestream.cprnetwork.org/pls/live_classical_aac.pls',
        'mplayer flags': ['-playlist'],
    },
    {
        'id': 'cproa',
        'name': 'Colorado Public Radio Open Air',
        'uri': 'http://livestream.cprnetwork.org/pls/live_openair_aac.pls',
        'mplayer flags': ['-playlist']
    }
]

def prompt():
    print("Please select radio stream.")

    for i, stream in enumerate(RADIO_STREAMS):
        print("{}.) {}".format(i, stream['name']))

    selection = input("Selection: ")

    if 0 <= int(selection) < len(RADIO_STREAMS):
        return RADIO_STREAMS[int(selection)]

def play(stream):
    print('Playing "{}"'.format(stream['name']))

    invocation = ['mplayer'] + stream['mplayer flags']
    invocation.append(stream['uri'])
    print(invocation)
    subprocess.call(invocation)


s = prompt()

while not s:
    s = prompt()

play(s)
