# Convert word-by-word JSON from whisper.cpp to the Podcast Namespace JSON structure
# Usage: python json-to-json.py <input.json>

import sys
import json

# read the json file
with open(sys.argv[1], 'r') as input_file:
    data = json.load(input_file)
    transcription = data['transcription']

# convert millisecond integers to seconds
def to_seconds(milliseconds):
    return int(milliseconds) / 1000

# create a transcript object
transcript = {
    'version': '1.0.0',
    'segments': []
}

# loop over the segments
for segment in transcription:
    # append a segment to the transcript segments array
    transcript['segments'].append({
        'startTime': to_seconds(segment['offsets']['from']),
        'endTime': to_seconds(segment['offsets']['to']),
        'body': segment['text'].strip()
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
with open(sys.argv[1].split('.')[0] + '-formatted.json', 'w') as output_file:
    json.dump(transcript, output_file, indent=4)
