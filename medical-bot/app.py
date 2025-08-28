
# app.py
import os
import tempfile
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request

# Third-party
from pydub import AudioSegment
import speech_recognition as sr
import pyttsx3

# Your project imports (keep as in your project)
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import system_prompt
from langchain_community.llms import Ollama

# Load env
load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY missing in environment")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Optional ffmpeg path - set FFMPEG_PATH in .env if ffmpeg is not on PATH
FFMPEG_PATH = os.environ.get("FFMPEG_PATH")  # e.g. C:\ffmpeg\bin\ffmpeg.exe
if FFMPEG_PATH:
    AudioSegment.converter = FFMPEG_PATH

# Optional: server-side TTS toggle
ENABLE_SERVER_TTS = os.environ.get("ENABLE_SERVER_TTS", "false").lower() in ("1", "true", "yes")

# Initialize Flask
app = Flask(__name__)

# Initialize Pinecone retriever & embeddings (kept as your project)
embeddings = download_hugging_face_embeddings()
index_name = "hexanovabot"
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Ollama LLM
llm = Ollama(model="mistral", temperature=0.4)

# Prompt + RAG chain
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# TTS engine (server-side optional)
tts_engine = pyttsx3.init()
def speak_text(text: str):
    if not ENABLE_SERVER_TTS:
        return
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        app.logger.exception("TTS error: %s", e)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat_text():
    msg = request.form.get("msg", "")
    app.logger.info("User text: %s", msg)
    if not msg.strip():
        return jsonify({"answer": "Please type something."})

    try:
        response = rag_chain.invoke({"input": msg})
        answer = response.get("answer") if isinstance(response, dict) else response
        if not answer:
            answer = "Sorry, I couldn't find an answer."
    except Exception as e:
        app.logger.exception("RAG error")
        answer = f"Error processing request: {e}"

    app.logger.info("Bot: %s", answer)
    speak_text(answer)
    return jsonify({"answer": answer})

@app.route("/voice", methods=["POST"])
def chat_voice():
    audio_file = request.files.get("audio")
    if not audio_file:
        return jsonify({"question": "", "answer": "No audio file received."})

    # Save incoming blob (likely webm/ogg)
    temp_in = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
    audio_file.save(temp_in.name)
    temp_in.close()

    # Convert to WAV for speech_recognition
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_wav.close()
    try:
        # pydub will use ffmpeg; ensure ffmpeg is installed or set FFMPEG_PATH
        AudioSegment.from_file(temp_in.name).export(temp_wav.name, format="wav")
    except Exception as e:
        app.logger.exception("Conversion error")
        return jsonify({"question": "", "answer": f"Speech recognition error (conversion): {e}"})

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(temp_wav.name) as source:
            audio_data = recognizer.record(source)
            try:
                # Using Google STT (online). If you want offline (vosk), adapt accordingly.
                text = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                return jsonify({"question": "", "answer": "Sorry, I couldn't understand your speech."})
            except Exception as e:
                app.logger.exception("STT error")
                return jsonify({"question": "", "answer": f"STT error: {e}"})
    except Exception as e:
        app.logger.exception("Audio read error")
        return jsonify({"question": "", "answer": f"Speech recognition error: {e}"})

    app.logger.info("User (voice): %s", text)

    # Run RAG
    try:
        response = rag_chain.invoke({"input": text})
        answer = response.get("answer") if isinstance(response, dict) else response
        if not answer:
            answer = "Sorry, I couldn't find an answer."
    except Exception as e:
        app.logger.exception("RAG error")
        answer = f"Error processing request: {e}"

    app.logger.info("Bot: %s", answer)
    speak_text(answer)
    return jsonify({"question": text, "answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

