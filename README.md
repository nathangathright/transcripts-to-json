# Transcripts to JSON

Whisper.cpp supports [word-by-word timestamps](https://github.com/ggerganov/whisper.cpp#word-level-timestamp), but doesn’t support exporting them in the [Podcast Namespace JSON structure](https://github.com/Podcastindex-org/podcast-namespace/blob/main/transcripts/transcripts.md#json). This is a quick guide on how to do that.

## Transcribing with Whisper.cpp
1. Setup whisper.cpp:
   ```sh
   # Clone whisper.cpp and navigate into it’s directory:
   git clone https://github.com/ggerganov/whisper.cpp.git && cd whisper.cpp/

   # Download a language model:
   bash ./models/download-ggml-model.sh base.en

   # Build the project:
   make
   ```
1. Transcribe an audio file with the `--output-json` and `--max-len` arguments:
   ```sh
   ./main -m ./models/ggml-base.en.bin -f <input.wav> -oj -ml 1
   
   # **Warning**
   # The main example currently runs only with 16-bit WAV files, so make sure to convert your input before running the tool. For example, you can use ffmpeg like this:
   ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le input.wav
   ```

## Using transcripts-to-json
1. Setup transcripts-to-json:
   ```sh
   # Clone transcripts-to-json and navigate into it’s directory:
   git clone https://github.com/nathangathright/transcripts-to-json.git && cd transcripts-to-json/
2. Convert
   ```
   # SRT to JSON
   python srt-to-json.py <input.srt>

   # JSON to JSON
   python json-to-json.py <input.json>
   ```