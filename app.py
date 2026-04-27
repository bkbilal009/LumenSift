# ================================
# IMPORTS
# ================================
from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import gradio as gr
from groq import Groq
import re
import os

# ================================
# CONFIG
# ================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # 🔐 Use HF secrets
client = Groq(api_key=GROQ_API_KEY)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Global store
vector_store = None
stored_chunks = []

# ================================
# UTIL: EXTRACT VIDEO ID
# ================================
def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

# ================================
# STEP 1: GET TRANSCRIPT
# ================================
def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "❌ Invalid YouTube URL"

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        full_text = " ".join([t.text for t in transcript])
        return full_text

    except Exception as e:
        return f"❌ Transcript Error: {str(e)}"

# ================================
# STEP 2: CHUNKING
# ================================
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# ================================
# STEP 3: VECTOR STORE
# ================================
def create_vector_store(chunks):
    global vector_store, stored_chunks

    embeddings = embed_model.encode(chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    vector_store = index
    stored_chunks = chunks

# ================================
# STEP 4: RETRIEVAL
# ================================
def retrieve(query, top_k=3):
    query_embedding = embed_model.encode([query])
    distances, indices = vector_store.search(np.array(query_embedding), top_k)

    results = [stored_chunks[i] for i in indices[0]]
    return "\n".join(results)

# ================================
# STEP 5: LLM
# ================================
def generate_answer(query, context):
    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

# ================================
# HANDLERS
# ================================
def handle_process(url):
    transcript = get_transcript(url)

    if transcript.startswith("❌"):
        return transcript, "", []

    chunks = chunk_text(transcript)
    create_vector_store(chunks)

    preview = transcript[:500]

    return "✅ Video processed successfully!", preview, []

def handle_chat(query, chat_history):
    if vector_store is None:
        return "", chat_history + [(query, "❌ Process a video first")]

    context = retrieve(query)
    answer = generate_answer(query, context)

    chat_history.append((query, answer))
    return "", chat_history

# ================================
# UI
# ================================
with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("# 🎥 YouTube Video Assistant")
    gr.Markdown("Paste a YouTube link → process → chat with the video")

    with gr.Row():
        url_input = gr.Textbox(label="🔗 YouTube URL", scale=4)
        process_btn = gr.Button("🚀 Process", scale=1)

    status_output = gr.Markdown("")

    transcript_preview = gr.Textbox(
        label="📄 Transcript Preview",
        lines=5,
        interactive=False
    )

    gr.Markdown("---")

    chatbot = gr.Chatbot(label="💬 Chat with Video")

    with gr.Row():
        query_input = gr.Textbox(
            placeholder="Ask something about the video...",
            scale=4
        )
        send_btn = gr.Button("Send", scale=1)

    process_btn.click(
        handle_process,
        inputs=url_input,
        outputs=[status_output, transcript_preview, chatbot]
    )

    send_btn.click(
        handle_chat,
        inputs=[query_input, chatbot],
        outputs=[query_input, chatbot]
    )

app.launch()