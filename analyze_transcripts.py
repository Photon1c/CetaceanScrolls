# analyze_transcript.py
from openai import OpenAI

client = OpenAI()

def interpret_whale_transcript(transcript_text):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "developer", "content": "Analyze the following whale song transcription for motifs, patterns, or anomalies."},
            {"role": "user", "content": transcript_text}
        ]
    )
    return response.choices[0].message.content
