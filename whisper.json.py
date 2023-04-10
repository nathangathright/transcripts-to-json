# Convert word-by-word SRT from whisper.cpp to the Podcast Namespace JSON structure
# Usage: python whisper.json.py <input.srt>

import sys
import re
import json

# read the srt file
with open(sys.argv[1], 'r') as input_file:
    srt = input_file.read()

# create a transcript object
transcript = {
    'version': '1.0.0',
    'segments': []
}

# split the srt file into blocks
blocks = re.split(r"\n\n(?=\d+)", srt, maxsplit=0, flags=0)

def to_seconds(time):
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2].split(',')[0]) + int(time[2].split(',')[1]) / 1000

# loop over the blocks
for block in blocks:
    # split the block into lines
    lines = block.split('\n')

    # split the first line into start and end
    start_end = lines[1].split(' --> ')

    # split the start and end into hours, minutes, seconds, and milliseconds
    # convert the start and end to seconds
    # append a segment to the transcript segments array
    transcript['segments'].append({
        'startTime': to_seconds(start_end[0].split(':')),
        'endTime': to_seconds(start_end[1].split(':')),
        'body': lines[2].strip()
        
    })

# if a segment has no body, remove it
transcript['segments'] = list(filter(lambda segment: segment['body'] != '', transcript['segments']))

# if a segment just contains puctuation, combine it with the previous segment
for i in range(len(transcript['segments']) - 1, 0, -1):
    if transcript['segments'][i]['body'] in ['.', ',', '!', '?']:
        transcript['segments'][i - 1]['body'] += transcript['segments'][i]['body']
        transcript['segments'][i - 1]['endTime'] = transcript['segments'][i]['endTime']
        transcript['segments'].pop(i)

# write the transcript to the output file
with open(sys.argv[1] + '.json', 'w') as output_file:
    json.dump(transcript, output_file, indent=4)
