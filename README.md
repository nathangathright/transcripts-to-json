# Podcasting 2.0 JSON

Whisper.cpp supports [word-by-word timestamps](https://github.com/ggerganov/whisper.cpp#word-level-timestamp), but doesn’t support exporting them in the [Podcast Namespace JSON structure](https://github.com/Podcastindex-org/podcast-namespace/blob/main/transcripts/transcripts.md#json). This is a quick guide on how to do that.

## Quick Start
1. Setup whisper.cpp:
   ```sh
   # Clone whisper.cpp and navigate into it’s directory:
   git clone https://github.com/ggerganov/whisper.cpp.git && cd whisper.cpp/

   # Download a language model:
   bash ./models/download-ggml-model.sh base.en

   # Build the project:
   make
   ```
1. Transcribe an audio file with the `--max-len` argument:
   ```sh
   ./main -m ./models/ggml-base.en.bin -f <input.wav> -ml 1
   
   # **Warning**
   # The main example currently runs only with 16-bit WAV files, so make sure to convert your input before running the tool. For example, you can use ffmpeg like this:
   ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le input.wav
   ```
1. Setup and run whisper.json:
   ```sh
   # Clone whisper.json and navigate into it’s directory:
   git clone https://github.com/stenofm/whisper.json.git && cd whisper.json/
   
   # Convert an SRT into a JSON file:
   python whisper.json.py <input.srt>
   ```
