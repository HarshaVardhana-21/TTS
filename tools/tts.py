import os
from gtts import gTTS
from io import BytesIO

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def text_to_speech_stream(text: str, lang: str = "fr"):
    """
    Convert text to speech using gTTS.
    Returns both in-memory audio (BytesIO) and file path.
    """
    file_path = os.path.join(OUTPUT_DIR, f"speech_{lang}.mp3")
    tts = gTTS(text=text, lang=lang)

    # Save to file
    tts.save(file_path)

    # Save to memory (for streaming)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return audio_buffer, file_path
