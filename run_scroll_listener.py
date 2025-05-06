# run_scroll_listener.py
from load_audio_chunks import chunk_audio
from transcribe_chunk import transcribe_audio
from analyze_transcript import interpret_whale_transcript
from log_scroll_entry import log_entry

def run_scroll_pipeline(file_path):
    chunks = chunk_audio(file_path)
    for chunk_path in chunks:
        transcript = transcribe_audio(chunk_path)
        interpretation = interpret_whale_transcript(transcript)
        log_entry(transcript, interpretation)

# Example use
# run_scroll_pipeline("humpback_recording.mp3")
