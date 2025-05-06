# load_audio_chunks.py
import os
from pydub import AudioSegment

def chunk_audio(file_path, chunk_length_ms=300000, overlap_ms=30000):
    audio = AudioSegment.from_file(file_path)
    chunks = []

    step = chunk_length_ms - overlap_ms
    for start in range(0, len(audio) - chunk_length_ms + 1, step):
        chunk = audio[start:start + chunk_length_ms]
        output_path = f"{file_path}_chunk_{start // 1000}s.mp3"
        chunk.export(output_path, format="mp3")
        chunks.append(output_path)

    return chunks
