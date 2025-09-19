from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from tools.translation import translate_text
from tools.tts import text_to_speech_stream

app = FastAPI(title="Text-to-Speech Translation API")

    
@app.get("/")
def home():
    text = "Welcome to the Text-to-Speech Translation API"
    return text

class TranslationRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

@app.post("/translate-speech")
def translate_speech(request: TranslationRequest):
    try:
        # Step 1: Translation
        translated_text = translate_text(
            text=request.text,
            source_lang=request.source_lang,
            target_lang=request.target_lang
        )

        # Step 2: TTS (returns both memory + file)
        audio_buffer, file_path = text_to_speech_stream(
            translated_text, lang=request.target_lang
        )

        headers = {
            "X-Source-Text": request.text,
            "X-Translated-Text": translated_text
        }

        # Return audio stream (playable in browser)
        return StreamingResponse(
            audio_buffer,
            media_type="audio/mpeg",
            headers=headers
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)