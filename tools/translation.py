from langchain_core.tools import StructuredTool
from langchain_community.llms import HuggingFaceHub

# Available HuggingFace models for translation
MODEL_MAP = {
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    # Extend with more pairs as needed
}

def translate_text(text: str, source_lang: str = "en", target_lang: str = "fr") -> str:
    """Dynamically select translation model and translate text."""
    key = (source_lang, target_lang)
    if key not in MODEL_MAP:
        raise ValueError(f"Translation model not available for {source_lang} -> {target_lang}")

    repo_id = MODEL_MAP[key]
    translator_model = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={"temperature": 0.3, "max_length": 200}
    )
    return translator_model.invoke(text)

translation_tool = StructuredTool.from_function(
    func=translate_text,
    name="TextTranslation",
    description="Translate text dynamically from source language to target language"
)
