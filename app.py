from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

language = {
    "bn": "Bangla", "en": "English", "ko": "Korean", "fr": "French",
    "de": "German", "he": "Hebrew", "hi": "Hindi", "it": "Italian",
    "ja": "Japanese", "la": "Latin", "ms": "Malay", "ne": "Nepali",
    "ru": "Russian", "ar": "Arabic", "zh": "Chinese", "es": "Spanish",
    "ur": "Urdu" 
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    pronunciation = ""
    source_lang = ""
    selected_language = request.form.get("language")

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if selected_language and text:
            try:
                
                result = translator.translate(text, dest=selected_language)

                translated_text = result.text
                pronunciation = result.pronunciation or "N/A"
                source_lang = language.get(result.src, result.src)
            except Exception as e:
                translated_text = f"Translation failed: {e}"

    return render_template("index.html", languages=language, translated_text=translated_text,
                           pronunciation=pronunciation, source_lang=source_lang, selected_language=selected_language)

if __name__ == "__main__":
    app.run(debug=True)