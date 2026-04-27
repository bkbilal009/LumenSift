---
title: LumenSift AI
emoji: 💡
colorFrom: blue
colorTo: cyan
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
short_description: Sifting clarity and intelligence from video streams.
---

# 💡 LumenSift AI: Video Intelligence & Clarity Engine

> **"Filtering the noise, illuminating the core."**
> 
> LumenSift is a high-precision RAG (Retrieval-Augmented Generation) system engineered by **Muhammad Bilal** to distill deep insights from any YouTube video with surgical accuracy.

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-f34f29?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Deployed-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

---

## 🏛️ Project Vision

Video content asaan lagta hai, magar usme se specific information nikalna mushkil hota hai. **LumenSift** ko **Muhammad Bilal** ne isliye develop kiya hai taake lambi videos ko "Searchable Databases" mein badla ja sakay. Ye app sirf transcript nahi parhti, balkay video ke context ko "Sift" (filter) kar ke sirf wahi jawab deti hai jo user dhoond raha hota hai.

---

## 🏗️ Technical Architecture (The Engine)

LumenSift ka architecture modern AI engineering ke 3 pillars par khara hai:

### 1. Intelligence Extraction (The Sifter)

* **Authenticated Fetching:** `youtube-transcript-api` ke sath `cookies.txt` handling use ki gayi hai taake YouTube ke security protocols ko bypass kiya ja sakay aur 100% uptime milay.
* **Stream-to-Text:** Video audio se text data nikal kar usay structured format mein store karna.

### 2. Semantic Memory (The Vault)

* **Recursive Chunking:** `RecursiveCharacterTextSplitter` ke zariye text ko 1000 characters ke chunks mein toda jata hai taake financial ya technical tutorials ke tables aur points break na hon.
* **Vectorization:** `all-MiniLM-L6-v2` transformer model har chunk ko vector embeddings mein badalta hai.
* **FAISS Indexing:** Facebook ka industry-standard FAISS database use kiya gaya hai for ultra-fast similarity search.

### 3. Contextual Reasoning (The Core)

* **Llama 3.3 (70B) via Groq:** Duniya ka fast-est inference engine (Groq) use kiya gaya hai taake user ko 1 second se kam waqt mein jawab milay.
* **Strict RAG Protocol:** AI ko strictly limit kiya gaya hai ke wo sirf video transcript se jawab de, taake hallucination ka khatra na ho.

---

## 🛠️ Tech Stack (How it's Built)

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Orchestration** | LangChain (LCEL) | Logic & Chain Management |
| **Reasoning Model** | Llama 3.3 70B | Human-level comprehension |
| **Vector Database** | FAISS | Efficient Context Retrieval |
| **Embeddings** | HuggingFace (Transformers) | Semantic Text Understanding |
| **Infrastructure** | Groq Cloud | Ultra-low latency Inference |
| **Frontend UI** | Gradio (Blue & Cyan Theme) | Premium & Clean Interface |

---

## 🚀 Key Features

* **Lightning Fast:** Groq LPUs ke zariye instant transcript analysis.
* **Sift & Sort:** Lambi videos (1hr+) se specific timestamps ka data nikalna.
* **Professional Grade UI:** Indigo, Blue aur Cyan theme jo Stanford application ke liye perfect hai.
* **Secure Connection:** Cookie-based session handling for uninterrupted service.

---

## 🔮 Future Roadmap

* **Multi-Video Synthesis:** Ek sath poori YouTube playlist ko analyze karna.
* **Sentiment Analysis:** Video ke speaker ka tone aur mood analyze karna.
* **Auto-Summarization:** Video ka automatic structured summary (Bullet points) banana.

---

## 👨‍💻 Developer Profile

**Muhammad Bilal**
*Aspiring AI Developer | Data Structures & Algorithms (DSA) Expert | RAG Specialist.*
Focused on building reliable AI applications that solve real-world efficiency problems. Active participant in HEC Generative AI Training (Cohort 3).

### 🌐 Contact & Links:
* **GitHub:** [📂 bkbilal009](https://github.com/bkbilal009)
* **LinkedIn:** [💼 Muhammad Bilal](https://www.linkedin.com/in/muhammad-bilal-dev/)
* **Live App:** [🚀 LumenSift Space](https://huggingface.co/spaces/bkbilal09/LumenSift)

---
*Clarity. Intelligence. Speed.*
